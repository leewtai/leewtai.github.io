import logging
import re


def cln_str_input(input):
    return input.lower().strip()


def merge_author(graph, family_name, given_name, google_scholar_id=''):
    family_name = re.sub('[^a-z-_ ]', '', cln_str_input(family_name))
    given_name = re.sub('[^a-z-_ ]', '', cln_str_input(given_name))

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
                       if a['given_name'] == given_name]
    initial_match = [a for a in results
                     if (a['given_name'][0] == given_name[0]
                         and len(a['given_name']) <= 2)]
    if (not results) or (not full_name_match and not initial_match):
        logging.info('no match or matched family name but not given name')
        logging.info('creating new author {} {}'.format(
            given_name, family_name))
        graph.run("""
        CREATE (:Author {{family_name: '{family_name}',
                          given_name: '{given_name}',
                          last_update: date()}})""".format(
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
            + "SET a.given_name='{given_name}', a.last_update=date()".format(
                given_name=given_name))
    elif not full_name_match and len(initial_match) > 1:
        logging.warning('multiple shortened names detected '
                        'and require manual input')
        logging.warning('detected names')
        [logging.warning('{} {}'.format(a['given_name'], a['family_name']))
            for a in initial_match]
        logging.warning('and name not added was: {} {}'.format(
            given_name, family_name))
    elif full_name_match:
        assert len(full_name_match) == 1
    else:
        logging.warning('No match but not creating author {} {},'
                        'please check the logic'.format(
                            given_name, family_name))

    if google_scholar_id:
        graph.run("""
        MATCH (a:Author {{family_name: '{family_name}',
                          given_name: '{given_name}'}})
        SET a.google_scholar_id='{gs_id}', a.last_update=date()""".format(
            family_name=family_name, given_name=given_name,
            gs_id=google_scholar_id))


def merge_paper(graph, title, content='', google_scholar_paper_id='',
                file_name=''):
    title = cln_str_input(title)
    graph.run("MERGE (p:Paper {{title: '{title}'}})")
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
                         title=title, file_name=cln_str_input(file_name)))


def merge_producer(graph, name):
    name = cln_str_input(name)
    graph.run("MERGE (p:Producer {{name: '{name}'}})".format(
        name=name))
    graph.run("""MATCH (p:Producer {{name: '{name}'}})
                 SET p.last_update=date()""".format(
                    name=name))


def parse_name(family_name, given_name='', middle_name=''):
    if not given_name:
        split_name = family_name.split(' ')
        if len(split_name) == 3:
            given_name, middle_name, family_name = split_name
        elif len(split_name) == 2:
            given_name, family_name = split_name
    if not middle_name and given_name.isupper() and len(given_name) == 2:
        middle_name = given_name[1]
        given_name = given_name[0]
    return family_name, given_name, middle_name


def match_family_name(graph, family_name, given_name='', middle_name=''):
    family_name, given_name, middle_name = parse_name(
            family_name, given_name, middle_name)

    return_cypher = """
    RETURN a.family_name AS family_name,
           a.given_name AS given_name,
           a.google_scholar_id as gs_id"""
    match_last_name = "MATCH (a:Author {{family_name: '{family_name}'}})"
    results = graph.run(
        match_last_name.format(family_name=family_name)
        + return_cypher).data()
    full_name_match = [a['given_name'] for a in results
                       if a['given_name'] == given_name]
    initials_match = [a for a in results
                     if (a['given_name'][0] == given_name[0]
                         and len(a['given_name']) <= 2)]
    return results, full_name_match, initials_match


def merge_authored(graph, title, gs_id='', given_name='',
                   family_name='', year=2020):
    title = cln_str_input(title)
    given_name = cln_str_input(given_name)
    family_name = cln_str_input(family_name)

    if family_name and given_name:
        match_auth_name = """
        MATCH (a:Author {{given_name: '{given_name}',
                          family_name: '{family_name}'}})
        """.format(given_name=given_name,
                   family_name=family_name)
    elif gs_id:
        match_auth_name = """
        MATCH (a:Author {{google_scholar_id: '{gs_id}'}})".format(gs_id=gs_id))
        """.format(gs_id=gs_id)
    else:
        logging.error('you need to specify a name or google scholar id')
    graph.run(match_auth_name
              + " MATCH (p:Paper {{title: '{title}'}})".format(title=title)
              + "MERGE (a)-[:AUTHORED {{year: {pub_year}}}]->(p)".format(
                  pub_year=year))


def merge_published(graph, name, title, year):
    graph.run("""
    MATCH (j:Producer {{name: '{name}'}})
    MATCH (p:Paper {{title: '{title}'}})
    MERGE (j)-[:PUBLISHED {{year: {pub_year}}}]->(p)
    """.format(name=cln_str_input(name),
               title=cln_str_input(title),
               pub_year=year))


def merge_pubished_author(graph, name, gs_id, given_name, family_name, year):
    name = name.lower().strip()
    given_name = given_name.lower().strip()
    family_name = family_name.lower().strip()

    if family_name and given_name:
        match_auth_name = """
        MATCH (a:Author {{given_name: '{given_name}',
                          family_name: '{family_name}'}})
        """.format(given_name=given_name.lower(),
                   family_name=family_name.lower())
    elif gs_id:
        match_auth_name = """
        MATCH (a:Author {{google_scholar_id: '{gs_id}'}})".format(gs_id=gs_id))
        """.format(gs_id=gs_id)
    graph.run("MATCH (j:Producer {{name: '{name}'}})".format(name=name.lower())
              + match_auth_name
              + "MERGE (j)-[:PUBLISHED {{year: {pub_year}}}]->(a)".format(
                  pub_year=year))


def merge_referenced(graph, title, ref_title, year=0):
    title = cln_str_input(title)
    ref_title = cln_str_input(ref_title)
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


