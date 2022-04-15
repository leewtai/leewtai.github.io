import json
import logging
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
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
auth_titles = ['' for _ in auth_ids]
ref_titles = ['' for _ in ref_ids]
for citation in citations:
    row_ind = [i for i, aid in enumerate(auth_ids)
               if aid == citation['auth_id']]
    col_ind = [i for i, rid in enumerate(ref_ids) if rid == citation['ref_id']]
    if not col_ind or not row_ind:
        continue
    citation_df[row_ind[0], col_ind[0]] = citation['ref_count']
    auth_titles[row_ind[0]] = citation['auth_title']
    ref_titles[col_ind[0]] = citation['ref_title']


citation_cnt = np.apply_along_axis(lambda x: np.sum(x > 0), 0, citation_df)
citation_act = np.apply_along_axis(lambda x: np.sum(x > 0), 1, citation_df)

np.savetxt('{}_{}_citation.csv'.format(target_author.get('given_name'),
                                       target_author.get('family_name')),
           citation_df, delimiter=',')
json.dump({'auth_titles': auth_titles, 'ref_titles': ref_titles},
          Path('{}_{}_citation_titles.json'.format(
              target_author.get('given_name'),
              target_author.get('family_name'))).open('w'))



# np.min(citation_cnt)
# np.max(citation_cnt)  # 4
# 
# max_cit_cnt = np.apply_along_axis(np.max, 1, citation_df)
# plt.hist(max_cit_cnt)
# plt.title('Dist of reference count of most popular article')
# plt.savefig('dist_ref_cnt_most_popular.png')
# plt.close()
# 
# # 2 things could impact the citation frequency, the length of the
# # article, the importance of the citation, and the base-citation
# # rate of the authors. citations ~ Poisson(t * (p + p_i))
# std_cit_cnt = np.apply_along_axis(
#     lambda x: x / max_cit_cnt,
#     0, citation_df)
# np.apply_along_axis(np.max, 1, std_cit_cnt)
# np.apply_along_axis(np.min, 1, std_cit_cnt)
# 
# 
# std_sum = np.apply_along_axis(np.sum, 0, std_cit_cnt)
# # popular_ind = np.where(citation_cnt == 4)
# popular_ind = np.where(std_sum > 1.3)
# # popular_ind = np.where(citation_cnt > 3)
# popular_refs = np.array(ref_ids)[popular_ind]
# {(c['ref_id'], c['ref_title'])
#  for c in citations if c['ref_id'] in popular_refs.tolist()}
# 
# # There is some correlation between the references
# citation_df[:, popular_ind]
# 
# # Normalizing by total reference count helps a lot
# # Normalizing by mean and std hurts given most citations are 0
# X = np.apply_along_axis(lambda x: (x - np.mean(x)) / np.std(x), 0, citation_df)
# X = std_cit_cnt
# u, s, vh = np.linalg.svd(X)
# eigen_vals = np.power(s, 2)
# plt.scatter([i for i in range(u.shape[0])],
#             np.cumsum(eigen_vals) / np.sum(eigen_vals))
# plt.savefig('max_std_pca_eigen_values.png')
# plt.close()
# 
# tot_cols = 4
# fig, axes = plt.subplots(3, tot_cols)
# for i in range(3 * tot_cols):
#     col_ind = i % tot_cols
#     row_ind = int(np.floor(i / tot_cols))
#     axes[row_ind, col_ind].scatter([i for i in range(len(ref_ids))],
#                                    vh[i, :])
#     axes[row_ind, col_ind].set_title('EigVec{}'.format(i))
#     axes[row_ind, col_ind].plot([1, len(ref_ids)], [0, 0], color='black')
# plt.savefig('max_std_pca_citation_loading.png')
# plt.close()
# 
# 
# # Add in fake values to then see its impact
# n_sim = 1000
# vh_sims = []
# for i in range(n_sim):
#     X_sim = X
#     p = X.shape[1]
#     n = X.shape[0]
#     rand_ind = np.random.choice(p, 1, replace=False)[0]
#     X_sim[:, rand_ind] = np.random.permutation(X_sim[:, rand_ind])
# 
#     _, _, vh_sim = np.linalg.svd(X_sim)
#     vh_sims.append(vh_sim[:n, rand_ind].reshape((-1, 1)))
# 
# vh_array = np.concatenate(vh_sims, axis=1)
# thresholds = np.apply_along_axis(lambda x: np.percentile(np.abs(x), 99), 1, vh_array)
# for j in range(vh_array.shape[0]):
#     popular_ind = np.where(np.abs(vh[j, :]) >= thresholds[j])
#     popular_refs = np.array(ref_ids)[popular_ind]
#     popular_articles = {
#         (str(vh[j, np.where(np.array(ref_ids) == c['ref_id'])][0][0]), c['ref_title'])
#         for c in citations if any(popular_refs == c['ref_id'])}
#     _ = [art[1] for art in popular_articles]
#     logging.info('EigenVector{}'.format(j))
#     _ = [logging.info(art) for art in popular_articles]
# 
# tot_cols = 4
# fig, axes = plt.subplots(3, tot_cols)
# for i in range(3 * tot_cols):
#     col_ind = i % tot_cols
#     row_ind = int(np.floor(i / tot_cols))
#     axes[row_ind, col_ind].scatter([i for i in range(len(ref_ids))],
#                                    vh[i, :])
#     axes[row_ind, col_ind].set_title('loadings for EigVec{}'.format(i))
#     axes[row_ind, col_ind].plot([0, p], [thresholds[i], thresholds[i]], color="black")
#     axes[row_ind, col_ind].plot([0, p], [-thresholds[i], -thresholds[i]], color="black")
# plt.savefig('citation_mat_first_eigen_val_perm_thresh.png')
# plt.close()
#
#
#
# # Look how the papers breakdown per-citation component
# trans_df = X @ vh[:len(auth_ids), :].T
# fig, axes = plt.subplots(1, 2)
# axes[0].imshow(trans_df)
# axes[0].set_title('trans citation')
# axes[1].imshow(np.abs(trans_df))
# axes[1].set_title('abs trans citation')
# plt.savefig('trans_citation.png')
# plt.close()
#
# # Looking at
# np.apply_along_axis(np.mean, 0, np.abs(trans_df[:, :5]))
#
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
