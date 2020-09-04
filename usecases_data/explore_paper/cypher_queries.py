import logging
import re


def merge_author(graph, family_name, given_name, google_scholar_id=''):
    family_name = re.sub('[^a-z_ ]', '', family_name.lower())
    given_name = re.sub('[^a-z_ ]', '', given_name.lower())

    assert len(given_name) > 0 and len(family_name) > 1

    return_cypher = """
    RETURN a.family_name AS family_name,
           a.given_name AS given_name,
           a.google_scholar_id as gs_id"""
    match_last_name = "MATCH (a:Author {{family_name: '{family_name}'}})"
    results = graph.run(
        match_last_name.format(family_name=family_name)
        + return_cypher).data()
    full_name_match = [a['given_name'] for a in results
                       if a['given_name'].lower() == given_name]
    initial_match = [a for a in results
                     if (a['given_name'].lower()[0] == given_name[0]
                         and len(a['given_name']) <= 2)]
    if (not results) or (not full_name_match and not initial_match):
        logging.info('no match or matched family name but not given name')
        logging.info('creating new author {} {}'.format(
            given_name, family_name))
        graph.run("""
        CREATE (:Author {{family_name: '{family_name}',
                          given_name: '{given_name}'}})""".format(
            family_namme=family_name, given_name=given_name))
    elif (not full_name_match
          and len(initial_match) == 1
          and len(given_name) > len(initial_match[0]['given_name'])):
        logging.info('Detecting a single shortened name like J Smith')
        record_name = initial_match[0]
        logging.warning('Updating {} {} to {} {}'.format(
            record_name['given_name'], record_name['family_name'],
            given_name, family_name))
        graph.run(
            match_last_name.format(family_name=family_name)
            + "SET a.given_name = '{given_name}'".format(
                given_name=given_name))
    elif not full_name_match and len(initial_match) > 1:
        logging.warning('multiple shortened names detected '
                        'and require manual input')
        logging.warning('detected names')
        _ = [logging.warning('{} {}'.format(a['given_name'], a['family_name']))
             for a in initial_match]
        logging.warning('and name not added was: {} {}'.format(
            given_name, family_name))
    if google_scholar_id:
        graph.run("""
        MATCH (a:Author {{family_name: '{family_name}',
                          given_name: '{given_name}'}})
        SET a.google_scholar_id = '{gs_id}'""".format(gs_id=google_scholar_id))


paper_creation_query = """
MERGE (p:Paper {{title: '{title}',
                 source: '{source}'}})
"""
producer_creation_query = """
MERGE (p:Producer {{name: '{name}'}})
"""
authored_creation_query_by_gs = """
MATCH (a:Author {{google_scholar_id: '{gs_id}'}})
MATCH (p:Paper {{title: '{title}'}})
MERGE (a)-[:AUTHORED {{year: {pub_year}}}]->(p)
"""
authored_creation_query = """
MATCH (a:Author {{given_name: '{given_name}', family_name: '{family_name}'}})
MATCH (p:Paper {{title: '{title}'}})
MERGE (a)-[:AUTHORED {{year: {pub_year}}}]->(p)
"""
# Assumes if older references will be concatenated by Google
gs_paper_id_update_query = """
MATCH (p:Paper {{title: '{title}'}})
SET p.google_scholar_paper_id = '{gs_id}'
"""
published_paper_creation_query = """
MATCH (j:Producer {{name: '{name}'}})
MATCH (p:Paper {{title: '{title}'}})
MERGE (j)-[:PUBLISHED {{year: {pub_year}}}]->(p)
"""
published_author_creation_query = """
MATCH (j:Producer {{name: '{name}'}})
MATCH (a:Author {{google_scholar_id: '{gs_id}'}})
MERGE (j)-[:PUBLISHED {{year: {pub_year}}}]->(a)
"""
