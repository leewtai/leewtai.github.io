author_creation_query = """
MERGE (a:Author {{given_name: '{given_name}', family_name: '{family_name}'}})
"""
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
