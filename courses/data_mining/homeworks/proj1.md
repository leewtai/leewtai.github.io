# Project 1: Exploring the NYC municipal churn

## Overview

This project is meant for you to explore the NYC Citywide Payroll Data published on [NYC OpenData](https://data.cityofnewyork.us/City-Government/Citywide-Payroll-Data-Fiscal-Year-/k397-673e). The dataset contains the payroll information for all municipal workers in recent years.

A starting question to prompt you to explore the data, which may not be your final question, is how well can we predict if someone will stop working for an agency after 1 or 2 years? Turnover in workers is very costly because training is costly and it can lead to low morale on the team.

You can work on a different dataset or work on a different problem but please clear it with the instructor before doing so.

You should write this report treating Freshmen students as your target audience.

While the project is somewhat open-ended, your project must cover the following requirements:
- A description and exploration of the data
  - If you decide to work on a subset of data, you should explain how that subset is selected
  - Your exploration should give the readers a sense of the complexity and nuance in the dataset
  - If you process the data like handling missing values, summarizing data across regions or time periods, filtering out bad data points, recoding titles, etc you should documente these.
  - Any assumptions you may make about the fields should be stated.
  - Your exploration should cover whether you have collinearity in your data
- You must engineer at least 2 features that do not already exist in the data
  - At least one feature should be related to the agency level characteristic, e.g. manager to worker ratio, last year's growth, female/male ratio, etc
  - The other feature(s) have certain restrictions:
    - They cannot be a linear combination of the other features, e.g. the sum of column 1 vs column 2
    - They cannot be random non-linear transforms without justification, e.g. simply squaring or exponentiating another column
  - The features can be sourced from another dataset.
  - This should be reasonable, please explain your reasoning for creating this feature.
  - Please discuss whether your features were useful for your question
- Some visualizations of the data
  - One visualization must summarize at least one of the key features of the data sources
  - One visualization must summarize or highlight the interaction between features in your data
- Use at least one algorithm to predict the churn
  - A description of what algorithm, features, and/or data filtering was used
  - You should compare the algorithm's prediction to the "base rate" of natural turnover 
  - You must do some sort of validation for this prediction
- Use at least one algorithm to explore any patterns (or lack of patterns) in the data that may not be obvious
  - This can be the same algorithm as your prediction
  - A short reason why the pattern was not obvious at first, e.g. people who work longer get paid more is considered an obvious fact. Articulating your expectation before exploring the data would often help this requirement.
  - A description on how the algorithm helped you identify this pattern (or lack of pattern)
  - Please investigate and comment on whether you think the pattern (or lack of pattern) is "by chance" or likely a real phenomenon. This should be supported by further data exploration or external sources of information like a major journal or academic literature.
- A introduction and conclusion for your report so a Freshmen student outside of statistics can understand the overall report and insight you have found.
