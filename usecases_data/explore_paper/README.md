# Explore the key papers to read to start research

This project is meant to help students navigate the research space
and understand how to approach a professor when wanting to do research.


# Requirements:
- A running neo4j instance
- A running Grobid service if you want to parse PDF files
- `conda create -n explore python=3.7 ipykernel requests bs4 py2neo lxml`

# Data model for graph
There are 3 node types: `Author`, `Producer`, `Paper`
```
(:Author
  {given_name: '',
   family_name: '',
   middle_name: '',
   google_scholar_id: '',
   last_update: date()}
)
(:Producer
  {name: ''})
(:Paper
  {title: '',
   content: '',
   file_name: '',
   google_scholar_paper_id: '',
   last_update: date()})
```

There are 4 different types of relationships: `REFERENCED`, `CITED_BY`, `AUTHORED`, `PUBLISHED` 
```
(:Paper)-[:REFERENCED {year: INT, ref_count: INT}]->(:Paper)  
(:Author)-[:AUTHORED {year: INT}]->(:Paper)
(:Producer)-[:PUBLISHED {year: INT}]->(:Paper)
(:Producer)-[:PUBLISHED {year: INT}]->(:Author)
```
- Default ref count is 1 for `[:REFERENCED]`, but the more one paper mentions the other paper, the more this value will be.
