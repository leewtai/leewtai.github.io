# Explore the key papers to read to start research

This project is meant to help students navigate the research space
and understand how to approach a professor when wanting to do research.


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
(:Paper)-[:REFERENCED {year: INT}]->(:Paper)
(:Author)-[:AUTHORED {year: INT}]->(:Paper)
(:Producer)-[:PUBLISHED {year: INT}]->(:Paper)
(:Producer)-[:PUBLISHED {year: INT}]->(:Author)
```
