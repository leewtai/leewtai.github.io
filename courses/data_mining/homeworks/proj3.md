# Final Project for applied machine learning

### Overview

The final project in this class is an open-ended **machine learning** project. Key deliverables are
- A **written report**, in a PDF format. There is no page limit but you must address all of the requirements below and produce a cohesive report.
- You can form groups of up to 2 people
- Your code should be on Github and it cannot be a single notebook. An example separation would be:
  - Data Ingestion and basic quality checks
  - Feature generation and applying algorithms
  - Comparing performance


### Written report

Overall, your report should fit the general description of "applied machine learning". In spirit, the project should have 
- at least one hypothetical audience (applied problems do not exist if there are no people)
- data that is big (in n or p) enough to warrant machine learning methods
- an assessment whether the machine learning method sufficiently answered the problem (this does not have to be conclusive)


Here are more concrete specifications (some are flexible given the nature of the project)
- There needs to be a clear applied machine learning problem, e.g.
  - Data mining
    - Generate a non-obvious insights from the data that can be leads for
      further investigations (similar to the observation step in the
      scientific method). The most common way to do this is by merging
      datasets from different sources.
    - A metric or (ranking) algorithm that quickly filters or sorts large amounts of data for people.
  - Large-scale decision making
    - Anomaly detection
    - Auto-labeling/tagging
  - Please talk to the instructor if you're not sure if your project would qualify.
    - A model that is inferring relationships between variables is not machine learning. An exception exists for machine learning models embedded in a causal inference framework.
- You must identify an audience and articulate the potential value for that audience in the report.
  - Your audience can be an individual or an institution but should have some level of detail like "recent college grad" or "think tank for public policy on housing" rather than a hypothetical person/institution.
  - Value can be realized in the form of saved time, decreased uncertainty, or increased reward. I'm open to hearing other forms of value definition.
- Your data should be big, i.e. at least 2 datasets or a single large dataset for your project.
  - If you have two datasets you should articulate how the datasets complement each other, for example
    - One dataset could provide complementing features (e.g. one dataset may have the activities and another may have the user demographic data).
    - One dataset could provide more resolution (e.g. detailed surveys tend to be done less frequently so they're often complemented with surveys that are less detailed but collected more frequently).
    - One dataset could provide more data from a different population (e.g. a system change has made historical patent data to be stored in a different system).
    - You should not call a dataset collected from a different time point but from the same source as a different dataset.
  - For single datasets that are truly large or complex, you should articulate
    why it is considered large/complex relative to the standards your audience
    is used to.
- Please engineer at least one feature and evaluate its usefulness in the context of your project.
- You must perform some sort of exploratory data analysis that checks the completion and/or quality of the data or the existence of the problem (e.g. market size assessment).
  - You must identify the source of the data and summarize the datasets.
    - Ideally, the data source should come from the entity that manages the data. Management is defined by the entity responsible if the data has quality issues. For example, data aggregators like Kaggle do not manage the data it posts on its challenges but Twitter manages Twitter data. Some exceptions exist like platforms like [NYC OpenData](https://opendata.cityofnewyork.us/data/) allow you to report data quality issues and will be considered a manager of the data.
  - This exploration should perform basic checks for quality (e.g. returns should have positive and negative values, population values should match expectations etc). This step should convince the reader that the data is correct.
- You must use a machine learning algorithm (this does not have to be one we covered)
  - Please have at least one graphical summary that highlights how your algorithm is working.
  - You must quantitatively evaluate how your algorithm fits to the data. For example, correlations are meaningful if they're close to -1 or 1,
    clustering and supervised learning methods all have different metrics associated with them.
- Please verify the results whether is due to chance or likely a real pattern.
  - For example, you may have to subset the data to see if the result is due to an outlier. You can also quote external sources to help
    understand the data.
  - Please make sure you quantitatively address the question "if you had a different dataset, how robust are the results from the algorithm?" (CV can address this)
  - You should compare to a "dumb yet reasonable" approach

Layout recommendation:
- State the problem
- Highlight your most impressive result
- Introduce data and/or model
  - Explain your approach and alternatives
  - Explain the data at hand
- Explain why your approach was best
- Talk about risks/limitations
- Restate the conclusion


### Github Code
- You should have a README page
  - A at most 5 sentence summary of the project
  - An general explanation of the different files/folders if someone were to replicate your study.
- No data should be on Github but your README should explain how the data can be obtained.
- Your written report and code should both exist on Github.
  - You do not have to check in the PDF version of your report on Github but your Rmarkdown or LaTeX
    file should exist on Github.
  - If you use Word as a text editor. Make sure you have a link from your README to this document.
