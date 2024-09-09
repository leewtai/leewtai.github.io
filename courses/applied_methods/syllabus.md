# Applied Statistical Methods
UN3105 - Fall 2024

This course is meant to give you a survey of various applied statistic methods beyond linear regression.
This can vary drastically depending on the instructor's background.

|Topic|What Problems Does It Solve?|
|---|---|
|Bayesian Statistics|How do we introduce prior knowledge into modeling?|
|Kalman Filters + Kriging |How do we deal with temporally or spatially dependent data?|
|Sampling and data quality |How do you get relevant data to your problem?|
|Survival analysis |How do we deal with censored data?|
|Causal inference|What else can quantify the impact besides randomized controlled trials?|
|(if time allows) Sequential analysis|Can we use the data sequentially without cheating?|


## - Your Job
  - AI tools like ChatGPT are generally allowed unless explicitly banned for the assignment. You are strongly discouraged from using them for intro courses but this is not one of them.
    However, it is best that you prompt ChatGPT to ask you questions rather than having it provide you
    with solutions. You are still responsible for the correctness of your work. Here's an example prompt you could try:

    """
    You are a college instructor helping students with an assignment. Your job is to help clarify
    and guide my thinking by asking questions back without giving me the answers to the problem.
    Here are 2 examples:
    Question: create a simulation that demonstrates the sample average is unbiased for estimating the population mean.
    Your answer: What does unbiased mean? Would you expect a single sample average to be exactly the same as the population mean?
    
    Question: how should we evaluate a model?
    Answer: What is the purpose of the model? How would you know if the model was bad? What is the model being compared to?
    """

  - Bring your laptop, take notes!
  - Avoid e-mailing if possible, share your thoughts on the discussion board instead.
  - Participate and ask questions, this is not easy!
    - In class: forecast what could be done, compare with what is happening, then summarize the difference.
    - Ed Discussions: describe the problem: what you observed vs what you expected to see.
    - To each other: summarize the conversation to ensure you're listening and think constructively before criticizing.
  - Upholding the honor code: https://www.cs.columbia.edu/education/honesty/

### People
Instructor:
Wayne Tai Lee (wtl2109)

Teaching Assistant:
Yizi Zhang (yz4123)

### Timeline
I reserve the right to change the ordering and the content for the course throughout the semester.

|Date|Topic|Follow-up|Before-Class|
|---|---|---|---|
|2024-09-04|[Introductions and expectations](https://docs.google.com/presentation/d/15cUnejYtpbJF0fm7oPUj1gW16BoGw4WKl59J5ktfnX0/edit?usp=sharing)|syllabus||
|2024-09-09|[Regression Refresher with R](https://docs.google.com/presentation/d/1FPe7kA40qkHUSP2ZJeU1CdofNsYZplD8V4RkS4tGu7Y/edit?usp=sharing) |A Modern Approach to Regression with R|Have your R computing setup ready|
|2024-09-11|[Challenges for regression](https://docs.google.com/presentation/d/1JfoqE9f33XuympxlTWFkmzXVzy0c73bZMpxP722-J0A/edit?usp=sharing)|[Linear Mixed Models](https://m-clark.github.io/mixed-models-with-R/random_intercepts.html)|[Homework 0](homeworks/hw0.md) due;<br>Skim over [Trustworthiness of crowds is gleaned in half a second](https://static1.squarespace.com/static/5daf65330e17a4220c7707ce/t/64378dd57efb4b7d3b265a54/1681362389720/ChweFreemanSPPS.pdf)<br>Download `trustworthiness.zip` and extract the files from CourseWorks|
|2024-09-16|Crash course in Bayesian Statistics <!--- (https://docs.google.com/presentation/d/1xHXP7YkbhTw_aHWJS4CKhQwOE1sFZPKL1FvnJxhSpWk/edit?usp=sharing) --->     |Doing Bayesian Data Analysis by John Kruschke|<!---Read [Modeling Ideology and Predicting Policy Change with Social Media](https://dl-acm-org.ezproxy.cul.columbia.edu/doi/10.1145/2702123.2702193) by Zhang and Counts--->|
|2024-09-18|Contrasting Bayesian Methods with Classical Methods <!--- (https://docs.google.com/presentation/d/14r8G-DP_P_m6aqcml_EFMFb2De2BKVYs9nIPCDDadio/edit?usp=sharing)--->|||
|2024-09-23|Introduction to Data Quality <!--- (https://docs.google.com/presentation/d/19IId2fnQ9dtqfA7uvwWDeIW4cHPjD-emYHY00yvI6bM/edit?usp=sharing)--->       ||Homework 1 <!--- NYTimes EDA](homeworks/hw1.md)--->|
|2024-09-25|Introduction to Data Quality Part 2   |<!--- [Chapter 1 on this dissertation](https://escholarship.org/uc/item/89f9z0tj)--->||
|2024-09-30|Dependent Data - Problems with Temporal Data <!---(https://docs.google.com/presentation/d/1LmREGERJCS5GzmmvR0WFLTxILFC_NBsyugsbCeHdptc/edit?usp=sharing)--->   |||
|2024-10-02|Dependent Data Continued - Time Series and Kalman Filters <!--- (https://docs.google.com/presentation/d/1LmREGERJCS5GzmmvR0WFLTxILFC_NBsyugsbCeHdptc/edit?usp=sharing) --->    ||[Project 1](homeworks/proj1.md) Due|
|2024-10-07|Practice - Forecasting Temperature|||
|2024-10-09|Dependent Data - GIS View of Spatial Data <!--- (https://docs.google.com/presentation/d/1p2niILw17C0aN4Jmn7LjJRb8qClX-_QLc58dBAkpZzY/edit?usp=sharing) --->||Homework 2 <!--- ](homeworks/hw2.md) --->|
|2024-10-14|Dependent Data continued - Spatial Statistics <!--- (https://docs.google.com/presentation/d/1p2niILw17C0aN4Jmn7LjJRb8qClX-_QLc58dBAkpZzY/edit?usp=sharing)--->|For manipulating spatial data in R: [rspatial.org](https://rspatial.org/)||
|2024-10-16|Interpolation of Spatial Data| [Some Theory for Kriging - Ch 1.2](https://clio.columbia.edu/catalog/11310671)||
|2024-10-21|Practice with Kriging|||
|2024-10-23|Discussion on spatial data privacy||[Twelve Million Phones, One Dataset, Zero Privacy](https://www.nytimes.com/interactive/2019/12/19/opinion/location-tracking-cell-phone.html)<br>Homework3 <!---(homeworks/hw3.md)--->|
|2024-10-28|Sampling <!---(https://docs.google.com/presentation/d/11m03-LRNIH53WvOVrVeXbk9NIzHw5DdnCKxgJayg50Q/edit?usp=sharing) and practice with [NHANES](https://wwwn.cdc.gov/nchs/nhanes/tutorials/module3.aspx) and Discussion on Paper--->|[Sampling: Design and Analysis](https://clio.columbia.edu/catalog/2402697) Chap 1-2.2||
|2024-10-30|Revisiting data collection and common errors <!---(https://docs.google.com/presentation/d/11m03-LRNIH53WvOVrVeXbk9NIzHw5DdnCKxgJayg50Q/edit?usp=sharing) --->||<!---The Silent Sex: Gender, Deliberation, and Institutions, Mendelberg and Karpowitz, Chapter 3](https://www-jstor-org.ezproxy.cul.columbia.edu/stable/j.ctt7zvffd)--->|
|2024-11-04|**NO CLASS - Election day**|||
|2024-11-06|Discussion on EDA <!---(https://docs.google.com/presentation/d/1MqQaUIA4Fkwsu7JlWTm1R7205OQtoQB5UrqMQjgU9cU/edit?usp=sharing) with focus on NYTimes Comments <br> How to start a problem? discussion on reading--->|Exploring characteristics of online news comments and commenters with machine learning approaches by Lee and Ryu||
|2024-11-11|Survival data and the issue of censoring <!---(https://docs.google.com/presentation/d/1Wdn8OYMl7D2r969LBHCRZU8zQN3APpXW3CBGtvPfiow/edit?usp=sharing)--->|[Vignette on R package survival](https://cran.r-project.org/web/packages/survival/vignettes/survival.pdf), [Vignette on time dependent survival analysis](https://cran.r-project.org/web/packages/survival/vignettes/timedep.pdf), and [Survival analysis: models and applications Chapter 1 + 2.1.1 + 2.1.2 + 5.1](https://clio.columbia.edu/catalog/10052476?counter=2)|Project 2 Due] <!---(homeworks/proj2.md)--->|
|2024-11-13|Survival curves and the Kaplan-Meier Estimator <!---(https://docs.google.com/presentation/d/1Wdn8OYMl7D2r969LBHCRZU8zQN3APpXW3CBGtvPfiow/edit?usp=sharing)--->|||
|2024-11-18|Practice with survival analysis |Framingham Heart Study (Study description on CourseWorks)||
|2024-11-20|Issues with missing data <!---(https://docs.google.com/presentation/d/1zAhlALXWzXGoXpDC3eLZ_2RJFwC0UdrRXTNxzhJfheY/edit?usp=sharing)--->||- [The prevention and handling of the missing data](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3668100/) <br> - Homework 4 <!---(homeworks/hw4.md)--->|
|2024-11-25|Discussion - flaws in randomized control studies||[Randomization in the tropics revisited: a theme and eleven variations](https://scholar.princeton.edu/sites/default/files/deaton/files/deaton_randomization_revisited_v2_2019_01.pdf)|
|2024-11-27|**NO CLASS - Thanksgiving Holiday**|||
|2024-12-02|Causal inference - AB testing in tech and traps <!---(https://docs.google.com/presentation/d/1ovVGmmFS7C4kVYPFYt2RSatZEROM7dp_WaivB6n4XOA/edit?usp=sharing)--->||Homework 5 <!---(homeworks/hw5.md)--->|
|2024-12-04|Causal Inference - matching algorithms, difference-in-differences||- Joshua D. Angrist and Jörn-Steffen Pischke (2015). Mastering ’Metrics: The Path from Cause to Effect, chapter 5 (see CourseWorks) <br> - [Modern Algorithms for Matching in Observational Studies by Paul Rosenbaum, 2020](https://www-annualreviews-org.ezproxy.cul.columbia.edu/doi/10.1146/annurev-statistics-031219-041058)|
|2024-12-09|Wrap-up||Project 3 Due<!---(homeworks/proj3.md) --->|


### Logistics
Lectures:
  MW 2:40-4:00pm Eastern
Office Hours:
  - Instructor office hours: Thursday 9:30am-11:30am Uris 324 (previously the facuty lounge)
  - TA office hours 4-5pm on [Zoom](https://columbiauniversity.zoom.us/j/6349551141)


### Computer Setup
  - I encourage you to setup your computing environment through [Anaconda and Jupyter Notebooks](../../setup/conda_and_navigator_setup.md) or use [RStudio](https://posit.co/download/rstudio-desktop/).
    - Here's how you typeset [math and code in Jupyter Notebooks](../../setup/jupyter_typeset_pdf.md)
    - The common commands for math and code are [here](../../setup/math_and_code.md)

### Grading
If your final grade is in [93-100), you will earn at least an A, [90-93) will earn you at least an A-, [87-90) will earn you at least a B+, etc. A grading curve may be applied depending on the class performance but your grade will not be curved downwards. "At least" implies that there's a possibility to earn a grade higher than your actual percentage.

A+ will be rewarded only on exceptional cases. 

#### - Homeworks (25%)
  - Late homeworks will receive 0 credit
  - The TA can grant extensions for these
#### - Projects (70%)
  - Late projects will be penalized by 50% for **each day** it's late.
  - Projects should be submitted on Gradescope
  - The likely distribution is a 20/20/30 split across the 3 projects
#### - Participation (5%)
  - Instead of attendance, in class activities, recorded through Canvas, is how we'll grade this.
  - To pass the class, you must have at least 50% here.
  - You will get the full 5% if you have at least 75% of these.

### Prerequisites

  - Exposure to foundational statistics and probability
  - Course in computing that manipulated data
  - Linear regression

### Textbooks / Supplies

No textbook but references are available on the syllabus.
