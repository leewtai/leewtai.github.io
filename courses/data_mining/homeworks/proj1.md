# Project 1: Mining NYCOpen Data

## Overview
This project is meant for you to mine for insights in the [NYC 311](https://www.ny.gov/agencies/nyc-311) data set published on the [NYC OpenData](https://nycopendata.socrata.com/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9) platform along with the [NYC Payroll](https://data.cityofnewyork.us/City-Government/Citywide-Payroll-Data-Fiscal-Year-/k397-673e) dataset.

A starting question to prompt you to explore the data, which may not be your final question, is whether NYC is allocating its resources efficiently. Payroll tends to be the largest expense for most public services and if the service demand is matched by an equivalent supply, then one would say the process is efficient. This can be tackled from different angles such as absolute staffing, money spent on payroll, timing, etc.

You should write this report treating your peers as your target audience.

While the project is somewhat open-ended, your project must cover the following requirements:
- A description of the your data collection and various downstream processes.
  - This should include how your initial data pull is different from the entire dataset. This is necessarily a subset because downloading "all data" is in general a bad practice. Multiple attempts is encouraged but please document your decision processes.
  - From your data pull to your analysis, any data processing like handling missing values, summarizing data across regions or time periods, filtering out bad data points, recoding titles, etc should also be documented.
  - Who was mainly responsible for which dataset.
  - I recommend you to leverage the Socrata API that provides simple SQL capabilities against the databases. This allows you to trim down the dataset significantly before it hits your computer.
  - If you add other data sources to the project, you should do the same for each of them.
  - A description how you're comparing or combining the various datasets (e.g. merging by date and zip code?)
- You must engineer a feature that does not already exist in the data
  - This cannot be a linear combination of the other features, e.g. total pay is often sum of bonus plus base salary.
  - Please explain your reasoning for creating this feature.
  - Please discuss whether your feature was useful in your report.
- Some visualizations of the data
  - One visualization must summary at least one of the key features of the data sources
  - One visualization must summarize or highlight the insight
- Use at least one algorithm to identify patterns that were not obvious at first.
  - A short reason why the pattern was not obvious at first, e.g. people who work longer get paid more is considered an obvious fact. Articulating your expectation before exploring the data would often help this requirement.
  - Please investigate and comment on whether you think the pattern is "by chance" or likely a real pattern. This should be supported by further data exploration or external sources of information like a major journal or academic literature.
- A introduction and conclusion for your report so an undergraduate student outside of statistics can understand the overall report and insight you have found.

Some restrictions:
  - You cannot drop the 311 or the payroll datasets but you may replace them with other data sources.
