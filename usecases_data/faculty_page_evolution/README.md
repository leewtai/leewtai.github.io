# Faculty changes over time

One of the key initiatives to advance our diversity, equity, and
inclusion targets is to collect data on the faculty population.

The ideal statistics would be comparable to other schools and national
statistics. However, these statistics are likely self-reported (to be
verified).

One way is to scrape faculty pages for different departments, then
use image classifiers to identify the gender of different faculty
members. The pages archived on [wayback machine](http://wayback.archive.org)
could be used to infer the changes of faculty composition over time.

## Flow
- Scrape University faculty pages
- Get data from Wayback on the same faculty page
- Infer last update for department page
- Parser for faculty images, names, titles, and contact information
- Labeler for faculty attributes

For each faculty

## Data model

#### University
- university_id
- year_founded
- name
- departments
- url
- state
- city

#### Departments
- university_id
- department_name
- department_url
- faculty_url
- last_updated
