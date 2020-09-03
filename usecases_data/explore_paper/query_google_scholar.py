import json
import logging
import re
import time

import requests
from bs4 import BeautifulSoup
from py2neo import Graph

import cypher_queries

logging.basicConfig(format="%(asctime)-15s %(message)s",
                    filename='query_google_scholar.log',
                    level=logging.INFO)
neo4j_cred = json.load(open('neo4j_login.json', 'r'))
graph = Graph('localhost', password=neo4j_cred['password'])

auth_citation_url = 'https://scholar.google.com/citations'

# TODO source this from faculty page -> google scholar
# author_id = '88cU_4UAAAAJ'
# graph.run("""
# MATCH (auth:Author {given_name: 'John', family_name: 'Cunningham'})
# SET auth.google_scholar_id = '%s'
# """ % author_id)


cql_out = graph.run("""
MATCH (auth:Author)
WHERE EXISTS(auth.google_scholar_id)
RETURN auth""")
auths = cql_out.data()
cql_out.close()
assert auths
logging.info('Identified {} authors to query'.format(len(auths)))

scholar_params = {
    'sortby': 'pubdate',
    'pagesize': 100}

author_list = []


def parse_journal(journal_str):
    # "bioRxiv, 354340, 2019" -> "bioRxiv"
    # "arXiv preprint arXiv:2002.08563" -> "arXiv preprint"
    # "Neurons, Behavior, Data analysis, and Theory 1 (7), 13476"
    #     -> "Neurons, Behavior, Data analysis, and Theory"
    return re.sub('[^A-Za-z]* [^ ]*[0-9].*$', '', journal_str)


def get_paper_id(cited_by_str):
    return re.sub('.*cites=([0-9]+)', '\\1', cited_by_str)


def log_db_size(graph):
    producer_count = graph.run("""
        MATCH (prod:Producer)
        RETURN count(*) AS total""").data()[0]['total']
    paper_count = graph.run("""
        MATCH (paper:Paper)
        RETURN count(*) AS total""").data()[0]['total']
    auth_count = graph.run("""
        MATCH (:Author)-[auth:AUTHORED]->(:Paper)
        RETURN count(*) AS total""").data()[0]['total']

    logging.info(('We have {} producers, {} papers,'
                 'and {} authored relationships').format(
                     producer_count, paper_count, auth_count))


logging.info('Before querying Google Scholar')
log_db_size(graph)

for auth in auths:
    # TODO, page through using cstart=100, pagesize is limited at 100
    gs_id = auth['auth'].get('google_scholar_id')
    scholar_params.update({'user': gs_id})
    out = requests.get(url=auth_citation_url, params=scholar_params)
    time.sleep(2)
    if not out.status_code == 200:
        continue
    soup = BeautifulSoup(out.text, 'html.parser')
    citations = soup.find_all('tr', 'gsc_a_tr')
    for i, entry in enumerate(citations):
        logging.debug('author: {} {}'.format(
            auth['auth'].get('given_name'), auth['auth'].get('family_name')))
        logging.debug('citation count {}'.format(i))
        citation = entry.find_all('td', 'gsc_a_t')[0]
        citation_content = [cont.text for cont in citation.contents]
        paper = entry.contents[0]
        title, _, journal_str = (meta.text for meta in paper.contents)
        pub_year = entry.contents[-1].text
        graph.run(cypher_queries.paper_creation_query.format(
            title=title, source='google_scholar'))
        journal = parse_journal(journal_str)
        graph.run(cypher_queries.producer_creation_query.format(
            name=journal.lower()))
        # Authors are sourced from the database so should exist already
        graph.run(cypher_queries.authored_creation_query_by_gs.format(
            gs_id=gs_id, year=pub_year, title=title, pub_year=pub_year))
        graph.run(cypher_queries.published_paper_creation_query.format(
            name=journal, title=title, pub_year=pub_year))
        graph.run(cypher_queries.published_paper_creation_query.format(
            name=journal, title=title, pub_year=pub_year))
        graph.run(cypher_queries.published_author_creation_query.format(
            name=journal, gs_id=gs_id, pub_year=pub_year))

        cited_by = entry.contents[1].contents
        cited_by_href = cited_by[0].get('href')
        if cited_by_href:
            paper_id = get_paper_id(cited_by_href)
            graph.run(cypher_queries.gs_paper_id_update_query.format(
                gs_id=paper_id, title=title))

logging.info('ending google scholar query')
log_db_size(graph)
