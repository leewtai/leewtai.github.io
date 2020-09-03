from collections import Counter
import re

import requests
from bs4 import BeautifulSoup
from glob import glob
from py2neo import Graph

import cypher_queries

neo4j_cred = json.load(open('neo4j_login.json', 'r'))
graph = Graph('localhost', password=neo4j_cred['password'])

pdf_files = glob('prod_files/*.pdf')


def grab_names(tei_author):
    return {'given_name': tei_author.persname.forename.text,
            'family_name': tei_author.persname.surname.text}


def process_biblio(biblstruct, current_paper_title, cite_count):
    grobid_id = biblstruct.get('xml:id')
    weight = cite_count[grobid_id]
    authors = biblstruct.find_all('author')
    author_names = [grab_names(author) for author in authors]
    title = biblstruct.title.text
    source = biblstruct.monogr
    producer = source.title.text
    year = source.date.get('when')

    return {'grobid_id': grobid_id,
            'authors': author_names,
            'title': title,
            'source': 'citation',
            'producer': producer,
            'year': year}


# Running the Grobid service (depends on JVM8, gradle, grobid)
# https://grobid.readthedocs.io/en/latest/Grobid-service/
grobid_url = 'http://localhost:8070/api/processFulltextDocument'
for i, pdf_file in enumerate(pdf_files[:4]):
    files = {'input': open(pdf_file, 'rb'),
             'consolidateCitations': 1}

    out = requests.post(url=grobid_url, files=files)
    with open('xml_{}.txt'.format(i), 'w') as f:
        f.write(out.text)

    soup = BeautifulSoup(out.text, 'lxml')
    header = soup.teiheader
    pub_year = int(re.sub('.*([0-9]{4})', '\\1', header.find('date').text))
    authors = header.findChildren('author')
    author_names = [grab_names(author) for author in authors]
    title = header.find('title').text
    graph.run(cypher_queries.paper_creation_query.format(
        title=title.lower(), source='paper'))
    # Create the authors
    _ = [graph.run(cypher_queries.author_creation_query.format(
        given_name=a['given_name'], family_name=a['family_name'])
        for a in author_names if len(a['given_name']) > 1]
    # Create the authored relationship
    _ = [graph.run(cypher_queries.authored_creation_query.format(
        given_name=a['given_name'], family_name=a['family_name'],
        title=title, pub_year=pub_year)
        for a in author_names if len(a['given_name']) > 1]

    # If we want to do NLP in the future
    # abstract = header.find('abstract').text
    # paragraphs = soup.find_all('p')

    citations = soup.find_all('ref', type='bibr')
    cite_count = Counter([citation.get('target') for citation in citations])
    # FYI, BeautifulSoup will lower case all the tags
    biblio = soup.find_all('biblstruct')
    # first biblio is the paper itself
    for biblstruct in biblio:
        process_biblio(, title, cite_count)

        cited_by = entry.contents[1].contents
        cited_by_href = cited_by[0].get('href')
        if cited_by_href:
            paper_id = get_paper_id(cited_by_href)
            graph.run(cypher_queries.gs_paper_id_update_query.format(
                gs_id=paper_id, title=title))

