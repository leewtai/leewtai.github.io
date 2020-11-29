# Applied Statistical Methods
UN3105 - Fall 2020

This course is meant to give you a survey of various applied statistic methods. This can
vary drastically depending on the instructor's background.

|Topic|What Problems Does It Solve?|
|---|---|
|Sampling and data quality |How do you get the data relevant to your problem?|
|Bayesian Statistics|How do we introduce prior knowledge into modeling?|
|Kalman Filters + Kriging |How do we deal with temporally or spatially dependent data?|
|Survival analysis |How do we deal with censored data?|
|Causal inference|What else can quantify the impact besides randomized controlled trials?|
|(if time allows) Sequential analysis|Can we use the data sequentially without cheating?|

### Expectations
#### - Learning outcomes
- Students should be able to critique data-based studies
- Students should be able to articulate the difference between their ideal dataset and feasible dataset
- Students should be able to collect/wrangle/clean/transform their data
- Students should be able to diagnose models and understand their strength/weaknesses
- Students should be able to identify the classic models for certain types of data/problem
- Students should be able to simulate/hypothesize alternative scenarios that can explain the same patterns in the data


#### - Your Job
  - Come to class, bring your laptop, take chances!
  - Give feedback in office hours or e-mail, I don't want to waste your time.
  - Avoid e-mailing if possible, share your thoughts on the discussion board instead.
  - Participate and ask questions, this is not easy!
    - In class: forecast what should be done, compare with what is happening, then summarize the difference.
    - Canvas: describe what you observe then describe what you expect.
    - To each other: summarize the conversation to ensure you're listening and think constructively before criticizing.
  - Academic honesty: https://www.cs.columbia.edu/education/honesty/

### People
Instructor:
Wayne Tai Lee (wtl2109)

Teaching Assistant(s):
Navid Ardeshir (na2844)

### Timeline
I reserve the right to change the ordering and the content for the course throughout the semester.

|Date|Topic|Follow-up|Before-Class|
|---|---|---|---|
|2020-09-08|[Introductions and expectations](https://docs.google.com/presentation/d/15cUnejYtpbJF0fm7oPUj1gW16BoGw4WKl59J5ktfnX0/edit?usp=sharing)|syllabus||
|2020-09-10|[Revisiting data collection and common errors](https://docs.google.com/presentation/d/11m03-LRNIH53WvOVrVeXbk9NIzHw5DdnCKxgJayg50Q/edit?usp=sharing)|[Sampling: Design and Analysis](https://clio.columbia.edu/catalog/2402697) Chap 1-2.2||
|2020-09-15|[Sampling](https://docs.google.com/presentation/d/11m03-LRNIH53WvOVrVeXbk9NIzHw5DdnCKxgJayg50Q/edit?usp=sharing) and practice with [NHANES](https://wwwn.cdc.gov/nchs/nhanes/tutorials/module3.aspx) and Discussion on Paper|[Sampling: Design and Analysis](https://clio.columbia.edu/catalog/2402697) Chap 1-2.2|[Homework 0](homeworks/hw0.md) due|
|2020-09-17|[Introduction to Data Quality](https://docs.google.com/presentation/d/19IId2fnQ9dtqfA7uvwWDeIW4cHPjD-emYHY00yvI6bM/edit?usp=sharing)||Read [Modeling Ideology and Predicting Policy Change with Social Media](https://dl-acm-org.ezproxy.cul.columbia.edu/doi/10.1145/2702123.2702193) by Zhang and Counts|
|2020-09-22|How to start a problem? discussion on reading||[The Silent Sex: Gender, Deliberation, and Institutions, Mendelberg and Karpowitz, Chapter 3](https://www-jstor-org.ezproxy.cul.columbia.edu/stable/j.ctt7zvffd)|
|2020-09-24|Discussion on [EDA](https://docs.google.com/presentation/d/1MqQaUIA4Fkwsu7JlWTm1R7205OQtoQB5UrqMQjgU9cU/edit?usp=sharing) with focus on NYTimes Comments||[Homework 1 - NYTimes EDA](homeworks/hw1.md)|
|2020-09-29|[Regression Refresher with R](https://docs.google.com/presentation/d/1FPe7kA40qkHUSP2ZJeU1CdofNsYZplD8V4RkS4tGu7Y/edit?usp=sharing)|A Modern Approach to Regression with R||
|2020-10-01|Regression with NYTimes based on Reading||Exploring characteristics of online news comments and commenters with machine learning approaches by Lee and Ryu|
|2020-10-06|[Crash course in Bayesian Statistics](https://docs.google.com/presentation/d/1xHXP7YkbhTw_aHWJS4CKhQwOE1sFZPKL1FvnJxhSpWk/edit?usp=sharing)|Doing Bayesian Data Analysis by John Kruschke|[Project 1](homeworks/proj1.md) Due|
|2020-10-08|[Contrasting Bayesian Methods with Classical Methods](https://docs.google.com/presentation/d/14r8G-DP_P_m6aqcml_EFMFb2De2BKVYs9nIPCDDadio/edit?usp=sharing)|||
|2020-10-13|[Dependent Data - Problems with Temporal Data](https://docs.google.com/presentation/d/1LmREGERJCS5GzmmvR0WFLTxILFC_NBsyugsbCeHdptc/edit?usp=sharing)||[Homework 2](homeworks/hw2.md)|
|2020-10-15|[Dependent Data Continued - Time Series and Kalman Filters](https://docs.google.com/presentation/d/1LmREGERJCS5GzmmvR0WFLTxILFC_NBsyugsbCeHdptc/edit?usp=sharing)|[Chapter 1 on this dissertation](https://escholarship.org/uc/item/89f9z0tj)||
|2020-10-20|Practice - Forecasting Temperature|For manipulating spatial data in R: [rspatial.org](https://rspatial.org/)||
|2020-10-22|[Dependent Data - GIS View of Spatial Data](https://docs.google.com/presentation/d/1p2niILw17C0aN4Jmn7LjJRb8qClX-_QLc58dBAkpZzY/edit?usp=sharing)|||
|2020-10-27|[Dependent Data continued - Spatial Statistics](https://docs.google.com/presentation/d/1p2niILw17C0aN4Jmn7LjJRb8qClX-_QLc58dBAkpZzY/edit?usp=sharing)|[Interpolation of Spatial Data: Some Theory for Kriging - Ch 1.2](https://clio.columbia.edu/catalog/11310671)|[Homework3](homeworks/hw3.md)|
|2020-10-29|Practice with Kriging|||
|2020-11-03|**NO CLASS - Election day**|||
|2020-11-05|Discussion on spatial data privacy||[Twelve Million Phones, One Dataset, Zero Privacy](https://www.nytimes.com/interactive/2019/12/19/opinion/location-tracking-cell-phone.html)|
|2020-11-10|[Survival data and the issue of censoring](https://docs.google.com/presentation/d/1Wdn8OYMl7D2r969LBHCRZU8zQN3APpXW3CBGtvPfiow/edit?usp=sharing)|[Survival analysis: models and applications Chapter 1](https://clio.columbia.edu/catalog/10052476?counter=2)||
|2020-11-12|Simulating challenges from censored data|[Vignette on R package survival](https://cran.r-project.org/web/packages/survival/vignettes/survival.pdf), [Vignette on time dependent survival analysis](https://cran.r-project.org/web/packages/survival/vignettes/timedep.pdf), and [Survival analysis: models and applications Chapter 2.1.1 + 2.1.2 + 5.1](https://clio.columbia.edu/catalog/10052476?counter=2)|[Project 2 Due](homeworks/proj2.md)|
|2020-11-17|[Survival curves and the Kaplan-Meier Estimator](https://docs.google.com/presentation/d/1Wdn8OYMl7D2r969LBHCRZU8zQN3APpXW3CBGtvPfiow/edit?usp=sharing)|||
|2020-11-19|Practice with survival analysis |Framingham Heart Study (Study description on Canvas)||
|2020-11-24|[Missing data](https://docs.google.com/presentation/d/1zAhlALXWzXGoXpDC3eLZ_2RJFwC0UdrRXTNxzhJfheY/edit?usp=sharing)||- [The prevention and handling of the missing data](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3668100/) <br> - [Homework4](homeworks/hw4.md)|
|2020-11-26|**NO CLASS - Thanksgiving Holiday**|||
|2020-12-01|Discussion - flaws in randomized control studies||[Randomization in the tropics revisited: a theme and eleven variations](https://scholar.princeton.edu/sites/default/files/deaton/files/deaton_randomization_revisited_v2_2019_01.pdf)|
|2020-12-03|[Causal inference - AB testing in tech and traps](https://docs.google.com/presentation/d/1ovVGmmFS7C4kVYPFYt2RSatZEROM7dp_WaivB6n4XOA/edit?usp=sharing)||[Homework5](homeworks/hw5.md)|
|2020-12-08|Causal Inference - matching algorithms, difference-in-differences||- Joshua D. Angrist and Jörn-Steffen Pischke (2015). Mastering ’Metrics: The Path from Cause to Effect, chapter 5 (see Canvas) <br> - [Modern Algorithms for Matching in Observational Studies by Paul Rosenbaum, 2020](https://www-annualreviews-org.ezproxy.cul.columbia.edu/doi/10.1146/annurev-statistics-031219-041058)|
|2020-12-10|Wrap-up||[Project 3](homeworks/proj3.md) Due|
|TBD|Measure understanding|Final Exam|You!|


### Logistics
Lectures:
  [TuTh 11:40-12:55 Eastern](https://vergil.registrar.columbia.edu/#/courses/applied%20statistical%20methods) on Zoom (links on Canvas)
Office Hours:
  No office hours for TA, use discussion board for questions
  Instructor office hours by appointment only

### Computer Setup
  - I encourage you to setup your computing environment through [Anaconda and Jupyter Notebooks](../../setup/conda_and_navigator_setup.md) since we'll be using Jupyter Notebooks in class.
    - Here's how you typeset [math and code in Jupyter Notebooks](../../setup/jupyter_typeset_pdf.md)
    - The common commands for math and code are [here](../../setup/math_and_code.md)
  - Please have your photo posted on Zoom

### Grading
If your final grade is in [93-100), you will earn at least an A, [90-93) will earn you at least an A-, [87-90) will earn you at least a B+, etc. A grading curve may be applied depending on the class performance but your grade will not be curved downwards. "At least" implies that there's a possibility to earn a grade higher than your actual percentage.

A+ will be rewarded only on exceptional cases. 

#### - Homeworks (20%)
  - Late homeworks will receive 0 credit
  - Your lowest homework grade will be dropped. If you missed Homework0 because you enrolled late, this prevents you from receiving 0.
#### - Projects (70%)
  - Late projects will be penalized by 50% for each day it's late.
  - Projects should be submitted on Canvas
#### - Participation (10%)
  - Instead of attendance, in class activities, recorded through Canvas, is how we'll grade this.
  - To pass the class, you must have at least 50% here.

### Prerequisites
  - Exposure to foundational statistics and probability
  - Course in computing that manipulated data
  - Linear regression

### Textbooks / Supplies
No textbook but references are available on the syllabus.
