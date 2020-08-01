# Applied Statistical Methods
UN3105 - Fall 2020

### Expectations
#### - Learning outcomes
- Students should be able to critique data-based studies
- Students should be able to articulate the difference between their ideal dataset and feasible dataset
- Students should be able to collect/wrangle/clean/transform their data
- Students should be able to diagnose the model and understand its shortcoming
- Students should be able to identify the classic models for different types of data
- Students should be able to simulate/hypothesize alternative scenarios that can explain the same patterns in the data


#### - Your Job
  - Come to class, bring your laptop, take chances!
  - Give feedback in office hours or e-mail, I don't want to waste your time.
  - Avoid e-mailing if possible
  - Participate and ask questions, this is not easy!
    - In class: forecast what should be done, compare with what is happening, then summarize the difference.
    - Canvas: describe what you observe, describe what you expect, communicate clearly.
    - To each other: summarize the conversation to ensure you're listening and think constructively before criticizing.
  - Academic honesty: https://www.cs.columbia.edu/education/honesty/

### People
Instructor:
Wayne Tai Lee (wtl2109)

Teaching Assistant(s):
TBD

### Timeline
I reserve the right to change the ordering and the content for the course throughout the semester.

|Date|Topic|Reading|Due|
|---|---|---|---|
|2020-09-08|[Introductions and expectations](https://docs.google.com/presentation/d/15cUnejYtpbJF0fm7oPUj1gW16BoGw4WKl59J5ktfnX0/edit?usp=sharing)|syllabus||
|2020-09-10|[Revisiting data collection and common errors](https://docs.google.com/presentation/d/11m03-LRNIH53WvOVrVeXbk9NIzHw5DdnCKxgJayg50Q/edit?usp=sharing)|[Sampling: Design and Analysis](https://clio.columbia.edu/catalog/2402697) Chap 1-2.2||
|2020-09-15|Practice with [NHANES](https://wwwn.cdc.gov/nchs/nhanes/tutorials/module3.aspx) and Discussion on Paper||- Read [Modeling Ideology and Predicting Policy Change with Social Media](https://dl-acm-org.ezproxy.cul.columbia.edu/doi/10.1145/2702123.2702193) by Zhang and Counts<br>- Homework 0 due|
|2020-09-17|[Introduction to Data Quality](https://docs.google.com/presentation/d/19IId2fnQ9dtqfA7uvwWDeIW4cHPjD-emYHY00yvI6bM/edit?usp=sharing)|||
|2020-09-22|How to start a problem? discussion on reading||[The Silent Sex: Gender, Deliberation, and Institutions, Mendelberg and Karpowitz, Chapter 3](https://www-jstor-org.ezproxy.cul.columbia.edu/stable/j.ctt7zvffd)|
|2020-09-24|Discussion on [EDA](https://docs.google.com/presentation/d/1MqQaUIA4Fkwsu7JlWTm1R7205OQtoQB5UrqMQjgU9cU/edit?usp=sharing) with focus on NYTimes Comments||Homework 1 - NYTimes EDA|
|2020-09-29|[Regression Refresher with R](https://docs.google.com/presentation/d/1FPe7kA40qkHUSP2ZJeU1CdofNsYZplD8V4RkS4tGu7Y/edit?usp=sharing)|A Modern Approach to Regression with R||
|2020-10-01|Regression with NYTimes based on Reading||Exploring characteristics of online news comments and commenters with machine learning approaches by Lee and Ryu|
|2020-10-06|[Crash course in Bayesian Statistics](https://docs.google.com/presentation/d/1xHXP7YkbhTw_aHWJS4CKhQwOE1sFZPKL1FvnJxhSpWk/edit?usp=sharing)|Doing Bayesian Data Analysis by John Kruschke|Project 1 Due|
|2020-10-08|[Contrasting Bayesian Methods with Classical Methods](https://docs.google.com/presentation/d/14r8G-DP_P_m6aqcml_EFMFb2De2BKVYs9nIPCDDadio/edit?usp=sharing)|||
|2020-10-13|[Dependent Data - Time Series and Kalman Filters](https://docs.google.com/presentation/d/1LmREGERJCS5GzmmvR0WFLTxILFC_NBsyugsbCeHdptc/edit?usp=sharing)|[Chapter 1 on this dissertation](https://escholarship.org/uc/item/89f9z0tj)|Homework 2|
|2020-10-15|Practice - Forecasting Temperature|||
|2020-10-20|[Dependent Data - Spatial Statistics](https://docs.google.com/presentation/d/1p2niILw17C0aN4Jmn7LjJRb8qClX-_QLc58dBAkpZzY/edit?usp=sharing)|For manipulating spatial data in R: [rspatial.org](https://rspatial.org/)||
|2020-10-22|Practice with Kriging|[Interpolation of Spatial Data: Some Theory for Kriging - Ch 1.2](https://clio.columbia.edu/catalog/11310671)||
|2020-10-27|Discussion on spatial data privacy||[Twelve Million Phones, One Dataset, Zero Privacy](https://www.nytimes.com/interactive/2019/12/19/opinion/location-tracking-cell-phone.html)|
|2020-10-29|[Survival data and the issue of censoring](https://docs.google.com/presentation/d/1Wdn8OYMl7D2r969LBHCRZU8zQN3APpXW3CBGtvPfiow/edit?usp=sharing)|[Survival analysis: models and applications Chapter 1](https://clio.columbia.edu/catalog/10052476?counter=2)||
|2020-11-03|**NO CLASS - Election day**|||
|2020-11-05|Simulations with survival analysis|[Vignette on R package survival](https://cran.r-project.org/web/packages/survival/vignettes/survival.pdf), [vignette on time dependent survival analysis](https://cran.r-project.org/web/packages/survival/vignettes/timedep.pdf), and [Survival analysis: models and applications Chapter 2.1.1 + 2.1.2 + 5.1](https://clio.columbia.edu/catalog/10052476?counter=2)|Project 2 Due|
|2020-11-10|Practice with survival analysis||Framingham nurses study|
|2020-11-12|[Missing data](https://docs.google.com/presentation/d/1zAhlALXWzXGoXpDC3eLZ_2RJFwC0UdrRXTNxzhJfheY/edit?usp=sharing)||[The prevention and handling of the missing data](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3668100/)|
|2020-11-17|Discussion - flaws in randomized control studies||[Randomization in the tropics revisited: a theme and eleven variations](https://scholar.princeton.edu/sites/default/files/deaton/files/deaton_randomization_revisited_v2_2019_01.pdf) <br> Statistical Models and Shoe Leather by David Freedman 1991|
|2020-11-19|[Causal inference - AB testing in tech and traps](https://docs.google.com/presentation/d/1ovVGmmFS7C4kVYPFYt2RSatZEROM7dp_WaivB6n4XOA/edit?usp=sharing)|||
|2020-11-24|Causal Inference - matching algorithms||Modern Algorithms for Matching in Observational Studies by Paul Rosenbaum, 2020|
|2020-11-26|**NO CLASS - Thanksgiving Holiday**|||
|2020-12-01|Causal Inference - difference-in-differences||Joshua D. Angrist and Jörn-Steffen Pischke (2015). Mastering ’Metrics: The Path from Cause to Effect, chapter 5.|
|2020-12-03|Critique||[Associati on  between  consumption of vegetables and COVID-19 mortality at a country level in Europe](https://www.medrxiv.org/content/10.1101/2020.07.17.20155846v1.full.pdf)|
|2020-12-08|Critiques|||
|2020-12-10|Critiques||Project 3 Due|
|TBD|Measure understanding|Final Exam|You!|



### Logistics
Lectures:
  [TuTh 11:40-12:55](https://vergil.registrar.columbia.edu/#/courses/applied%20statistical%20methods)
Office Hours:
  TBD


### Grading
If your final grade is in [93-100), you will earn at least an A, [90-93) will earn you at least an A-, [87-90) will earn you at least a B+, etc. A grading curves may occur depending on the class performance but your grade will not be curved downwards. "At least" implies that there's a possibility to earn a grade higher than your actual percentage.

A+ will be rewarded only on exceptional cases. 

#### - Projects (90%)
  - Late projects will be penalized by 50% for each day it's late.
  - Projects should be submitted on Canvas
#### - Participation (10%)
  - Instead of attendance, in class activities is how we'll grade this.

### Prerequisites
  - Exposure to foundational statistics and probability: conditional expectation,
  - Course in computing with data
  - Linear regression

### Textbooks / Supplies
No textbook but papers will be shared with the class for reading.
