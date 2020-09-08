import json
import logging
from collections import Counter

import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
from py2neo import Graph

logging.basicConfig(format="%(asctime)-15s %(message)s",
                    filename='doc_search.log',
                    level=logging.INFO)
neo4j_cred = json.load(open('neo4j_login.json', 'r'))
graph = Graph('localhost', password=neo4j_cred['password'])

# Pull paper based on author
author = {'given_name': 'John', 'family_name': 'Cunningham',
          'middle_name': 'P'}
papers = graph.run((
    "MATCH (:Author {{given_name: '{given_name}',"
    "                 family_name: '{family_name}',"
    "                 middle_name: '{middle_name}'}})"
    "-[a:AUTHORED]->(p:Paper)-[r:REFERENCED]->(p2:Paper)"
    " RETURN id(p) AS auth_id, p.title AS auth_title,"
    "        id(p2) AS ref_id, p2.title AS ref_title").format(
        **author)).data()

# Is there internal referencing?
auth_ids = {p['auth_id'] for p in papers}
ref_ids = {p['ref_id'] for p in papers}
# Overlaps are from self-referencing, grobid's first reference is
# the original article
len(auth_ids) + len(ref_ids) == len(auth_ids.union(ref_ids))

ref_count = Counter([p['ref_title'] for p in papers])
paper_edges = [(p['auth_id'], p['ref_id']) for i, p in enumerate(papers)
               if (ref_count[p['ref_title']] > 3
                   and p['auth_id'] != p['ref_id'])]

paper_graph = nx.DiGraph()
paper_graph.add_edges_from(paper_edges)
# auth_pos = {i: [0.1, j/len(auth_ids)] for j, i in enumerate(auth_ids)}
# ref_pos = {i: [0.9, np.random.uniform(0, 1)]
#            for i in ref_ids if i in paper_graph.nodes()}
# init_pos = {**ref_pos, **auth_pos}
pos = nx.shell_layout(
    paper_graph,
    nlist=[list(auth_ids), list(ref_ids.difference(auth_ids))])
pos = nx.spring_layout(paper_graph, pos=pos, iterations=50)
node_list = [i for i in auth_ids.union(ref_ids) if i in paper_graph.nodes()]
node_colors = ['blue' if i in auth_ids else 'red' for i in node_list]

nx.drawing.nx_pylab.draw_networkx(
    paper_graph, pos=pos, nodelist=node_list, node_color=node_colors)
plt.savefig('test_draw_nx.png')
plt.close()


# Calculate connection weights

# Plot based on connections
