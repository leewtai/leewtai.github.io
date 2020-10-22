# Explore the key papers to read before starting to work with a Professor

## Motivation
To diversify the applicant pool of Statistics graduate programs, one approach is
to engage students during their undergraduate studies with realistic research
experience. Many undergraduate research experiences, however, provide a poor
reference to actual statistical research. Students often lack the necessary
technical skills to perform actual research and endup simply collecting data
or writing summary papers. While both of these tasks are essential, they rarely
mimic the actual research environment.

One obstacle to a more realistic undergraduate research experience is the lack of
familiarity in the professor's research domain. Undergraduate education focuses
on the established core knowledge within the field that is routinely applied but
rarely goes to the depths of modern statistical research. To quickly learn the
necessary skills, a natural starting point is to read the recent publications
by the professors and the common papers cited in their research. This approach
becomes overwhelming quickly without proper guidance from the professor.

The goal of this project is to analyze the papers and citation pattern of professors
within the department to quickly identify key papers for the students to read. Desirable
properties of this project is to recommend the smallest set of papers that are foundational
and provide the widest coverage in topics.

This project is meant to help students navigate the research space
and understand how to approach a professor when wanting to do research.


## Methodology Sketch:
- Within the department, collect the professors' recent research papers (2019 and on).
  - This list is available from the Professor's website or on Google Scholar
- From each paper, obtain a PDF copy of the file and extract
  - Co-authors
  - Text
  - Citations made and the authors of those papers
- Baseline model:
  - Each citation is basically a topic
  - Use shared references to establish the correlation between papers
  - Weighted references as importance

## Requirements:
- A running neo4j instance
- A running Grobid service if you want to parse PDF files
- `conda create -n explore python=3.7 ipykernel requests bs4 py2neo lxml`

## Data model for graph
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

