import json
import logging

# import matplotlib.pyplot as plt
# import networkx as nx
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
    " WHERE a.year >= 2020"
    " RETURN p2.title AS paper, count(r) AS ref_count").format(
        **author)).data()

investigate = graph.run((
    "MATCH (p1:Paper)-[:REFERENCED]->(p2:Paper)"
    " WHERE p2.title = 'Preprint repository arxiv achieves milestone million uploads'"
    " RETURN p1.title")).data()
# Calculate connection weights

# Plot based on connections
