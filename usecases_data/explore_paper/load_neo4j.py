import json
import logging
import re
from collections import Counter
from pathlib import Path

from bs4 import BeautifulSoup
from glob import glob
from py2neo import Graph

import cypher_queries as cq


logging.basicConfig(format="%(asctime)-15s %(message)s",
                    filename='parse_pdf.log',
                    level=logging.INFO)

neo4j_cred = json.load(open('neo4j_login.json', 'r'))
graph = Graph('localhost', password=neo4j_cred['password'])

dir_path = 'grobid_xml/'
xml_files = glob(dir_path + '*.xml')


def grab_names(tei_author):
    persname = tei_author.find('persname')
    if not persname:
        # This happens when institutions are in the author field
        return
    given_name = persname.find('forename', type='first')
    middle_name = persname.find('forename', type='middle')
    family_name = persname.find('surname')
    if not family_name or not given_name:
        return
    return {'given_name': given_name.text,
            'middle_name': middle_name.text if middle_name else '',
            'family_name': family_name.text}


def process_biblio(graph, biblstruct, current_paper_title, cite_count,
                   current_year):
    grobid_id = biblstruct.get('xml:id')
    ref_count = cite_count.get('#{}'.format(grobid_id), 1)
    authors = biblstruct.find_all('author')
    author_names = [grab_names(author) for author in authors]
    [cq.merge_author(graph, **a) for a in author_names if a]

    ref_title = cq.cln_property(biblstruct.title.text)
    logging.info('adding citation from {} to {}'.format(
        current_paper_title, ref_title))
    cq.merge_paper(graph, title=ref_title)

    source = biblstruct.monogr
    if source.date and source.date.get('when'):
        year = re.findall('[0-9]{4}', source.date.get('when'))[0]
    elif source.date and source.date.text and source.date.text != 'null':
        year = re.findall('[0-9]{4}', source.date.text)[0]
    else:
        year = 0
        logging.warning('Cannot find published year for {}'.format(ref_title))
        logging.warning('Here is what is listed under date tag'.format(
            source.date))

    producer = source.title
    if producer:
        prod_name = cq.cln_property(producer.text)
        cq.merge_producer(graph, name=prod_name)
        cq.merge_published(graph, title=ref_title,
                           name=prod_name, year=year)
        [cq.merge_published_author(graph, name=prod_name, year=year, **a)
         for a in author_names if a]

    [cq.merge_authored(graph, title=ref_title, year=year, **a)
     for a in author_names if a]
    cq.merge_referenced(graph, title=current_paper_title,
                        ref_title=ref_title, year=current_year,
                        ref_count=ref_count)


for i, xml_file in enumerate(xml_files):
    print(i)
    fp = Path(xml_file)

    logging.info('parsing file {}'.format(fp.name))
    with fp.open() as f:
        xml = '\n'.join(f.readlines())

    soup = BeautifulSoup(xml, 'lxml')
    header = soup.teiheader
    # FYI, BeautifulSoup will lower case all the tags
    biblio = soup.find_all('biblstruct')
    year_tag = header.find('date')
    if year_tag and year_tag.text:
        pub_year = int(re.sub('.*((19|20)[0-9]{2}).*', '\\1', year_tag.text))
    else:
        # Take the latest referenced date as the date of publication
        mentioned_years = [
            int(re.findall('[0-9]{4}', d['when'])[0])
            for d in soup.find_all('date')[:36] if d.get('when')]
        pub_year = max(mentioned_years) if mentioned_years else 0
    authors = header.findChildren('author')
    author_names = [grab_names(author) for author in authors]
    title = cq.cln_property(header.find('title').text)
    if not title or not pub_year or not author_names:
        logging.warning('skipping {} - missing title'.format(fp.name))
        continue

    # Create the authors
    [cq.merge_author(graph, **a) for a in author_names if a]
    # Create paper
    abstract = cq.cln_property(header.find('abstract').text)
    paragraph_text = '\n'.join([cq.cln_property(pi.text.strip())
                                for pi in soup.find_all('p')])
    if "BAD_INPUT_DATA" in paragraph_text:
        paragraph_text = ''
    # Avoids short words in title for renaming the file
    title_words = [w
                   for w in re.sub('[^A-Za-z-]', ' ', title.strip()).split(' ')
                   if len(w) > 2]
    new_file_name = '{lead_auth_family_name}_{year}_{title}'.format(
        lead_auth_family_name=author_names[0]['family_name'],
        year=pub_year, title='_'.join([title_words[0], title_words[-1]]))
    sim_file_names = glob(dir_path + new_file_name + '*')
    new_file_name += '_{}'.format(len(sim_file_names)) + '.pdf'
    fp.rename(dir_path + new_file_name)
    # Need to replace double quotes with 2 single quotes because the cypher
    # query uses double quotes
    text = abstract + paragraph_text
    cq.merge_paper(graph, title=title, content=text,
                   file_name=fp.name)
    # Create the authored relationship
    [cq.merge_authored(graph, given_name=a['given_name'],
                       family_name=a['family_name'],
                       middle_name=a['middle_name'],
                       title=title, year=pub_year)
     for a in author_names if a]

    citations = soup.find_all('ref', type='bibr')
    cite_count = Counter([citation.get('target') for citation in citations])
    # fir=st biblio is the paper itself
    for biblstruct in biblio[1:]:
        try:
            process_biblio(graph, biblstruct, title, cite_count, pub_year)
        except Exception as e:
            ref_title = cq.cln_property(biblstruct.title.text)
            logging.error(e)
            logging.error('Problems with citation: {} to paper: {}'.format(
                ref_title), title)
    logging.info('{} loaded to neo4j'.format(fp.name))
