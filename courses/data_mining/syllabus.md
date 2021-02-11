# Applied Data Mining
UN3106 - Spring 2021

### Learning outcomes
- Gain an intuitive understanding of basic machine learning methods
- Understand how fitting models can help explore patterns in data
- Assess model accuracy or clustering in different usecases

## Overview
This course is meant to be a machine learning course for students on the
applied track but the title implies some emphasis on merging multiple
data sources and discovering patterns within them.

### People
Instructor:
Wayne Tai Lee: wtl2109

Teaching Assistant(s):
- Jaesung Son: 

### Timeline
I reserve the right to change the ordering and the content for the course throughout the semester.

|Date|Topic|Reference|Due|
|---|---|---|---|
|2021-01-12|[Intro to data mining](https://docs.google.com/presentation/d/1LRXc0v-mawZdvVYDJQXQ7MuG2_dCCOH8c2sW4aCerMs/edit?usp=sharing)|slides 1||
|2021-01-14|[The rise of machine learning](https://docs.google.com/presentation/d/17hPTelOmM_2OhsQnN1pEvUvf_p61rhyUVtSeNX_UHJc/edit?usp=sharing)|slides 2 + ISL Chapter 2.2|Have [R](https://cran.rstudio.com/) installed|
|2021-01-19|[Using regression to explore the data - NYC salary](https://docs.google.com/presentation/d/1RweE3ajD5pGn-FnPp-0tf_0iMWRHlMzUaTpp4utvmN8/edit?usp=sharing)|slides 3 + [Paper on Why Biased Estimators given Stein Estimator + Gauss Markov Theorem](https://www.jstor.org/stable/1268284?seq=1#metadata_info_tab_contents) + ISL Chapter 2.2 continued||
|2021-01-21|[Optimization and objective functions](https://docs.google.com/presentation/d/1RKi4H1kxhtwPyP6l1lTSFTAYjDHeE7umpvkc8cMD4F4/edit?usp=sharing)|Slide 5 + ISL Chapter 3.1.1 + 3.3.3|[Homework 1](homeworks/hw1.md) Due|
|2021-01-26|[Beyond classification accuracy](https://docs.google.com/presentation/d/1Dff7Et1pejUNyRzdyXwjDvoqCK9OGTq2RDODVUUZYPU/edit?usp=sharing)|Slides 6||
|2021-01-28|[Resampling techniques - accuracy vs robustness](https://docs.google.com/presentation/d/1dEpri9RjpqPSop5SBNv-TneoO0QYKMcyS0E5SEgueoQ/edit?usp=sharing)|Slides 7 + [Resampling from ISL](https://link.springer.com/chapter/10.1007/978-1-4614-7138-7_5)|- Read paper on [Stability](https://arxiv.org/abs/1310.0150)|
|2021-02-02|[Automated Model Selection](https://docs.google.com/presentation/d/1dEpri9RjpqPSop5SBNv-TneoO0QYKMcyS0E5SEgueoQ/edit?usp=sharing)|Slides 7 + [caret library](https://topepo.github.io/caret/index.html) + [ISL on resampling](https://link.springer.com/chapter/10.1007/978-1-4614-7138-7_5)||
|2021-02-04|[feature engineering - with text](https://docs.google.com/presentation/d/1BzfHDaGuvM2Vv6Vbi8YF55ZjzFAYFCcaAGcjpl9XkPE/edit?usp=sharing)|[Pre-processing Text](https://www.cambridge.org/core/journals/political-analysis/article/text-preprocessing-for-unsupervised-learning-why-it-matters-when-it-misleads-and-what-to-do-about-it/AA7D4DE0AA6AB208502515AE3EC6989E) + [Speech and Language Chapter 6.5](https://web.stanford.edu/~jurafsky/slp3/) |[Homework 2](homeworks/hw2.md) Due|
|2021-02-09|Working with text data continued|||
|2021-02-11|[Ridge + Lasso Regression](https://docs.google.com/presentation/d/1W_xNZ5aty4V8sGnc9nBpeVlfY4ws0tkH-fZGm2kngfI/edit?usp=sharing)|Slides 9 + ISL 6.2||
|2021-02-16|Principal Component Analysis||[Project 1](homeworks/proj1.md) Due|
|2021-02-18|Principal Component Analysis continued|Slides 10 + 17||
|2021-02-23|Weather data revisited|||
|2021-02-25|Weather data revisited|||
|2021-03-02|Spring Break|||
|2021-03-04|Spring Break|||
|2021-03-09|Splines|Slides 11|Homework 3 Due|
|2021-03-11|Splines vs Local Regression|Slides 11||
|2021-03-16|Regression Trees and random forests|Slides 13||
|2021-03-18|Variable importance revisited|||
|2021-03-23|Support Vector Machine||[Project 2](homeworks/proj2.md) Due|
|2021-03-25|Clustering|||
|2021-03-30|k-Means |||
|2021-04-01|Hierarchical clustering||Homework 4 Due|
|2021-04-06|DBSCAN|||
|2021-04-08|Dealing with missing values and cold starts|||
|2021-04-13|TBD||Homework 5 Due|
|2021-04-15|TBD|||
|2021-04-20|TBD|||
|2021-04-22|TBD|Project 3 Due||


### Logistics
Lectures:
  [TuTh 4:10pm - 5:25pm, Zoom Link on Canvas](https://vergil.registrar.columbia.edu/#/courses/APPLIED%20STATISTICAL%20COMPUTING)

Office Hours:
  - Wayne: by appointment via Google Invites

### Grading
If your final grade is in [93-100], you will earn at least an A, [90-93) will earn at least an A-, [87-90) will earn at least a B+, etc. A grading curves may occur depending on the class performance but I will not curve downwards. I may not give out A+'s in this class.

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
- An introductory statistics class
  - Basic probability distributions (e.g. Gaussian, binomial distributions and their likelihoods)
  - Basic hypothesis testing (e.g. t-test)
  - Summary statistics
  - Histograms, boxplots, etc
- A computing course involving data wrangling and visualization
- A modeling course that estimated parameters from data

### Textbooks / References
- [An Introduction to Statistical Learning with Applications in R](https://link.springer.com/book/10.1007%2F978-1-4614-7138-7) by Gareth James, Daniela Witten, Trevor Hastie, and Robert Tibshirani
- To collaborate on coding projects, here's a bare minimum [GitHub tutorial](https://leewtai.github.io/setup/git_for_beginniners.html). If you ever work officially with code, you should also look into the concept of branches and reviews which are not covered in the tutorial.

### Acknowledgement
A lot of these materials are based off the materials from Prof Thibault Vatter and Prof Gabriel Young.
