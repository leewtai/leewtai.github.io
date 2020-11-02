import json
import logging

import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
from py2neo import Graph

logging.basicConfig(format="%(asctime)-15s %(message)s",
                    filename='doc_search.log',
                    level=logging.INFO)
neo4j_cred = json.load(open('neo4j_login.json', 'r'))
graph = Graph('localhost', password=neo4j_cred['password'])

# User would start with an author then want to see their
# Publications then citation dependence

# Pull paper based on author
target_author = {'given_name': 'John', 'family_name': 'Cunningham',
                 'middle_name': 'P'}

# Grobid by default cites the original paper as the first reference
# so we exclude references that are identical to the paper itself.
citations = graph.run((
    "MATCH (:Author {{given_name: '{given_name}',"
    "                 family_name: '{family_name}',"
    "                 middle_name: '{middle_name}'}})"
    "-[a:AUTHORED]->(p:Paper)-[r:REFERENCED]->(p2:Paper)"
    " WHERE NOT id(p) = id(p2) "
    " RETURN id(p) AS auth_id, p.title AS auth_title,"
    "        id(p2) AS ref_id, p2.title AS ref_title,"
    "        r.ref_count AS ref_count").format(
        **target_author)).data()

# Is there internal referencing?
bad_titles = ['Preprint repository arxiv achieves milestone million uploads',
              '',  # empty title
              ]
papers = {p['auth_id']: p['auth_title'] for p in citations}
auth_ids = [p for p in papers]
ref_ids = list({p['ref_id'] for p in citations
                if not p['ref_title'] in bad_titles})
len([rid for rid in ref_ids if rid in auth_ids])
# Some authored papers are referenced by other papers

citation_df = np.zeros((len(auth_ids), len(ref_ids)))
for citation in citations:
    row_ind = [i for i, aid in enumerate(auth_ids)
               if aid == citation['auth_id']]
    col_ind = [i for i, rid in enumerate(ref_ids) if rid == citation['ref_id']]
    if not col_ind or not row_ind:
        continue
    citation_df[row_ind[0], col_ind[0]] = citation['ref_count']


citation_cnt = np.apply_along_axis(lambda x: np.sum(x > 0), 0, citation_df)
citation_act = np.apply_along_axis(lambda x: np.sum(x > 0), 1, citation_df)


np.min(citation_cnt)
np.max(citation_cnt)  # 4

max_cit_cnt = np.apply_along_axis(np.max, 1, citation_df)
std_cit_cnt = np.apply_along_axis(lambda x: x / max_cit_cnt, 0, citation_df)
norm_cit_cnt = np.apply_along_axis(lambda x: (x - np.mean(x)) / np.std(x), 0, std_cit_cnt)
# norm_cit_cnt = np.apply_along_axis(lambda x: x / citation_act, 0, citation_df)

popular_ind = np.where(citation_cnt == 4)
popular_refs = np.array(ref_ids)[popular_ind]
{(c['ref_id'], c['ref_title'])
 for c in citations if c['ref_id'] in popular_refs.tolist()}

# The correlation is quite high
citation_df[:, popular_ind]

# Normalizing by total reference count helps a lot
# u, s, vh = np.linalg.svd(citation_df)
u, s, vh = np.linalg.svd(norm_cit_cnt)
eigen_vals = np.power(s, 2)
plt.scatter([i for i in range(u.shape[0])],
            np.cumsum(eigen_vals) / np.sum(eigen_vals))

tot_cols = 4
fig, axes = plt.subplots(3, tot_cols)
for i in range(3 * tot_cols):
    col_ind = i % tot_cols
    row_ind = int(np.floor(i / tot_cols))
    axes[row_ind, col_ind].scatter([i for i in range(len(ref_ids))],
                                   vh[i, :])
    axes[row_ind, col_ind].set_title('loadings for EigVec{}'.format(i))
plt.savefig('citation_mat_first_eigen_val.png')
plt.close()

trans_df = norm_cit_cnt @ vh[:len(auth_ids), :].T
fig, axes = plt.subplots(1, 2)
axes[0, 0].imshow(trans_df)
axes[0, 1].set_title('trans citation')
axes[0, 1].imshow(np.abs(trans_df))
axes[0, 1].set_title('abs trans citation')
plt.savefig('trans_citation.png')
plt.close()

# paper_edges = [(p['auth_id'], p['ref_id']) for i, p in enumerate(papers)
#                if (ref_count[p['ref_title']] > 3
#                    and p['auth_id'] != p['ref_id'])]
#
#paper_graph = nx.DiGraph()
#paper_graph.add_edges_from(paper_edges)
## auth_pos = {i: [0.1, j/len(auth_ids)] for j, i in enumerate(auth_ids)}
## ref_pos = {i: [0.9, np.random.uniform(0, 1)]
##            for i in ref_ids if i in paper_graph.nodes()}
## init_pos = {**ref_pos, **auth_pos}
#pos = nx.shell_layout(
#    paper_graph,
#    nlist=[list(auth_ids), list(ref_ids.difference(auth_ids))])
#pos = nx.spring_layout(paper_graph, pos=pos, iterations=50)
#node_list = [i for i in auth_ids.union(ref_ids) if i in paper_graph.nodes()]
#node_colors = ['blue' if i in auth_ids else 'red' for i in node_list]
#
#nx.drawing.nx_pylab.draw_networkx(
#    paper_graph, pos=pos, nodelist=node_list, node_color=node_colors)
#plt.savefig('test_draw_nx.png')
#plt.close()
#

# Calculate connection weights

# Plot based on connections
