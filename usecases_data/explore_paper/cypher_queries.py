import logging
import time


def cln_title(title):
    return title.strip().capitalize()


def parse_name(family_name, given_name='', middle_name=''):
    family_name = family_name.strip()
    given_name = given_name.strip()
    middle_name = middle_name.strip()

    if not given_name:
        split_name = family_name.split(' ')
        if len(split_name) == 3:
            given_name, middle_name, family_name = split_name
        elif len(split_name) == 2:
            given_name, family_name = split_name
        else:
            logging.warning('need manual help with parsing {}'.format(
                family_name))
    if not middle_name and given_name.isupper() and len(given_name) == 2:
        middle_name = given_name[1]
        given_name = given_name[0]
    return family_name, given_name, middle_name


def match_family_name(graph, family_name, given_name='', middle_name=''):
    family_name, given_name, middle_name = parse_name(
            family_name, given_name, middle_name)

    assert len(given_name) > 0 and len(family_name) > 1

    return_cypher = """
    RETURN a.family_name AS family_name,
           a.given_name AS given_name,
           a.middle_name AS middle_name,
           a.google_scholar_id as gs_id"""
    match_last_name = """MATCH (a:Author {{family_name: '{family_name}'}})
                         WHERE a.given_name STARTS WITH '{first_initial}'"""
    results = graph.run(
        match_last_name.format(family_name=family_name,
                               first_initial=given_name[0])
        + return_cypher).data()
    full_name_match = [a for a in results
                       if (a['given_name'] == given_name
                           and a['middle_name'] == middle_name)]
    return (results, full_name_match,
            family_name, given_name, middle_name)


def merge_author(graph, family_name, given_name='',
                 middle_name='', google_scholar_id=''):
    (results, full_name_match, family_name,
     given_name, middle_name) = match_family_name(
             graph, family_name, given_name, middle_name)

    if not results:
        logging.info('no matches')
        logging.info('creating new author {} {}'.format(
            given_name, family_name))
        graph.run("""
        CREATE (:Author {{family_name: '{family_name}',
                          given_name: '{given_name}',
                          middle_name: '{middle_name}',
                          last_update: date()}})""".format(
            family_name=family_name, given_name=given_name,
            middle_name=middle_name))
    elif (not full_name_match
          and len(results) == 1
          and len(given_name) >= len(results[0]['given_name'])):
        logging.info('Detecting a single shortened name like J Smith')
        record_name = results[0]
        logging.warning('Updating {} {} to {} {}'.format(
            record_name['given_name'], record_name['family_name'],
            given_name, family_name))
        best_m_name = middle_name if middle_name else results[0]['middle_name']
        graph.run("""
        MATCH (a:Author {{family_name: '{og_family_name}',
                          given_name: '{og_given_name}'}})
        SET a.given_name='{given_name}', a.last_update=date(),
            a.middle_name='{middle_name}'""".format(
               og_family_name=results[0]['family_name'],
               og_given_name=results[0]['given_name'],
               given_name=given_name, middle_name=best_m_name))
    elif not full_name_match and len(results) > 1:
        logging.warning('multiple shortened names detected '
                        'and require manual input')
        logging.warning('detected names')
        [logging.warning('{} {}'.format(a['given_name'], a['family_name']))
            for a in results]
        logging.warning('and name not added was: {} {}'.format(
            given_name, family_name))
    elif full_name_match:
        assert len(full_name_match) == 1
        logging.info('Existing full name match exists for {} {}'
                     ', not updating'.format(given_name, family_name))
    else:
        logging.warning('No match but not creating author {} {},'
                        'please check the logic'.format(
                            given_name, family_name))
    if google_scholar_id:
        graph.run("""
        MATCH (a:Author {{family_name: '{family_name}',
                          given_name: '{given_name}',
                          middle_name: '{middle_name}'}})
        SET a.google_scholar_id='{gs_id}', a.last_update=date()""".format(
            family_name=family_name, given_name=given_name,
            middle_name=middle_name, gs_id=google_scholar_id))


def match_best_author(graph, family_name, given_name, middle_name=''):
    match_results = match_family_name(
        graph, family_name, given_name, middle_name)
    if match_results[1]:
        return (match_results[1][0]['family_name'],
                match_results[1][0]['given_name'],
                match_results[1][0]['middle_name'])
    elif len(match_results[0]) == 1:
        return (match_results[0][0]['family_name'],
                match_results[0][0]['given_name'],
                match_results[0][0]['middle_name'])
    else:
        logging.warning('Cannot find best match for {} {}'.format(
            given_name, family_name))
    return match_results[2], match_results[3], match_results[4]


def match_best_author_query(graph, gs_id='', family_name='',
                            given_name='', middle_name=''):
    if family_name or given_name:
        (family_name, given_name, middle_name) = match_best_author(
                 graph, family_name, given_name, middle_name)
        match_query = """
        MATCH (a:Author {{given_name: '{given_name}',
                          family_name: '{family_name}',
                          middle_name: '{middle_name}'}})
        """.format(given_name=given_name,
                   family_name=family_name, middle_name=middle_name)
    elif gs_id:
        match_query = """
        MATCH (a:Author {{google_scholar_id: '{gs_id}'}})
        """.format(gs_id=gs_id)
    else:
        logging.error('you need to specify a name or google scholar id')
    return match_query


def merge_paper(graph, title, content='', google_scholar_paper_id='',
                file_name=''):
    title = cln_title(title)
    graph.run("MERGE (p:Paper {{title: '{title}'}})".format(title=title))
    if content:
        graph.run("""MATCH (p:Paper {{title: '{title}'}})
                     SET p.content='{content}', p.last_update=date()""".format(
                         title=title, content=content))
    if google_scholar_paper_id:
        graph.run("""MATCH (p:Paper {{title: '{title}'}})
                     SET p.google_scholar_id = '{gs_id}',
                         p.last_update=date()""".format(
                         title=title, gs_id=google_scholar_paper_id))
    if file_name:
        graph.run("""MATCH (p:Paper {{title: '{title}'}})
                     SET p.file_name = '{file_name}',
                     p.last_update=date()""".format(
                         title=title, file_name=file_name.strip()))


def merge_producer(graph, name):
    name = cln_title(name)
    graph.run("MERGE (p:Producer {{name: '{name}'}})".format(
        name=name))
    graph.run("""MATCH (p:Producer {{name: '{name}'}})
                 SET p.last_update=date()""".format(
                    name=name))


def merge_authored(graph, title, gs_id='', family_name='',
                   given_name='', middle_name='',
                   year=time.localtime().tm_year):
    # gs_id is google scholar id, i got lazy typing
    title = cln_title(title)
    match_query = match_best_author_query(graph, gs_id, family_name,
                                          given_name, middle_name)
    graph.run(match_query
              + " MATCH (p:Paper {{title: '{title}'}})".format(title=title)
              + " MERGE (a)-[:AUTHORED {{year: {pub_year}}}]->(p)".format(
                  pub_year=year))


def merge_published(graph, name, title, year=time.localtime().tm_year):
    graph.run("""
    MATCH (j:Producer {{name: '{name}'}})
    MATCH (p:Paper {{title: '{title}'}})
    MERGE (j)-[:PUBLISHED {{year: {pub_year}}}]->(p)
    """.format(name=cln_title(name),
               title=cln_title(title),
               pub_year=year))


def merge_published_author(graph, name, gs_id='', family_name='',
                           given_name='', middle_name='',
                           year=time.localtime().tm_year):
    name = cln_title(name)
    match_query = match_best_author_query(graph, gs_id, family_name,
                                          given_name, middle_name)

    graph.run("MATCH (j:Producer {{name: '{name}'}})".format(name=name)
              + match_query
              + "MERGE (j)-[:PUBLISHED {{year: {pub_year}}}]->(a)".format(
                  pub_year=year))


def merge_referenced(graph, title, ref_title, year=0):
    title = cln_title(title)
    ref_title = cln_title(ref_title)
    graph.run("""
    MATCH (p1:Paper {{title: '{title}'}})
    MATCH (p2:Paper {{title: '{ref_title}'}})
    MERGE (p1)-[:REFERENCED]->(p2)
    """.format(title=title, ref_title=ref_title))
    if year:
        graph.run("MATCH (:Paper {{title: '{title}'}})"
                  "-[r:REFERENCED]->"
                  "(:Paper {{title: '{ref_title}'}})"
                  "SET r.year={year}".format(
                      title=title, ref_title=ref_title,
                      year=year))
