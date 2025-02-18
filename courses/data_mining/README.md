# Applied machine learning

This course will expose students to a variety of data mining applications
using machine learning methods.

Students who finish this class should:

- Gain an intuitive understanding of basic machine learning methods
- Understand how fitting models can help explore patterns in data
- Understand how to assess models and clustering in different usecases

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

### Timeline
I reserve the right to change the ordering and the content for the course throughout the semester.

|Date|Topic|Reference|Due|
|---|---|---|---|
|2025-01-21|[Intro to data mining](https://docs.google.com/presentation/d/1LRXc0v-mawZdvVYDJQXQ7MuG2_dCCOH8c2sW4aCerMs/edit?usp=sharing)|- [Brazilian e-commerce on Kaggle](https://www.kaggle.com/olistbr/brazilian-ecommerce)<br>- ISL Chapter 2.2||
|2025-01-23|[Data mining with basic statistics and regression review](https://docs.google.com/presentation/d/17hPTelOmM_2OhsQnN1pEvUvf_p61rhyUVtSeNX_UHJc/edit?usp=sharing)|ISL Chapter 3|- Have [R studio](https://cran.rstudio.com/) installed<br>- Informal exploration with the Brazilian e-commerce dataset|
|2025-01-28|Regression review continued|ISL Chapter 3||
|2025-01-30|[Principal Component Analysis](https://docs.google.com/presentation/d/19C31WjmOkdca-Nm4LBn5rLLadH138BESV4F_gyXgON8/edit?usp=sharing)|ISL 6.3.1|[Homework 1](homeworks/hw1.md) Due|
|2025-02-04|Principal Component Analysis Applications|ISL 6.3.1 + ISL 10.2||
|2025-02-06|[Logistic regression + Naive Bayes](https://docs.google.com/presentation/d/1U7yQPTLVIe-e9W70gHKFapB8XfohsnnUr56kTuESOHQ/edit?usp=sharing) and [notes](https://colab.research.google.com/drive/1e-ums4i27XyeMBIFYtrhX9kIipZz7aSa?usp=sharing)|ISL 6.3.1 + ISL 10.2||
|2025-02-11|[Rise of machine learning and "wrong" models - some history](https://docs.google.com/presentation/d/1RweE3ajD5pGn-FnPp-0tf_0iMWRHlMzUaTpp4utvmN8/edit?usp=sharing)|[Paper on Why Biased Estimators given Stein Estimator + Gauss Markov Theorem](https://www.jstor.org/stable/1268284?seq=1#metadata_info_tab_contents) + ISL Chapter 2.2 continued||
|2025-02-13|[Ridge + Lasso Regression](https://docs.google.com/presentation/d/1W_xNZ5aty4V8sGnc9nBpeVlfY4ws0tkH-fZGm2kngfI/edit?usp=sharing) and [notebook](https://colab.research.google.com/drive/1BWEiRjmH8i0kQBsXhmPBFDmWpxRi56RD?usp=sharing)|ISL 6.2|[Homework 2](homeworks/hw2_pca.md) Due Date Delayed Slightly|
|2025-02-18|[Ridge + Lasso Simulations](https://docs.google.com/presentation/d/1yktXlOcSGVHkoPBFiqkE1KiWk4aZ8gNzAAbXG4ixl64/edit?usp=sharing)|ISL 6.2||
|2025-02-20|[Tree Methods](https://docs.google.com/presentation/d/1tFOm3dSSBV7-PtYAAQgLYkAAp8bVMeUYiPZlP0rCtpE/edit?usp=sharing) and [notebook](https://colab.research.google.com/drive/1DMgY6wt5lMoSL2WZD0-SvlnJSGCT604Q?usp=sharing)|ISL 8.1||
|2025-02-25|[Tree Methods continued](https://docs.google.com/presentation/d/1tFOm3dSSBV7-PtYAAQgLYkAAp8bVMeUYiPZlP0rCtpE/edit?usp=sharing)|ISL 8.1||
|2025-02-27|[Trees + forests with real data](https://docs.google.com/presentation/d/1_yNVafSSJCs0KT_MKcVgbxio419NDCGDDeAVDZ05S7s/edit?usp=sharing)|ISL 8.2<br> [bias in random forest variable importance](https://www.jstor.org/stable/27594202)|[Homework 3](homeworks/hw3.md)|
|2025-03-04|[Optimization and objective functions](https://docs.google.com/presentation/d/1RKi4H1kxhtwPyP6l1lTSFTAYjDHeE7umpvkc8cMD4F4/edit?usp=sharing)|Slide 5 + ISL Chapter 3.1.1 + 3.3.3||
|2025-03-06|[Beyond classification accuracy](https://docs.google.com/presentation/d/1Dff7Et1pejUNyRzdyXwjDvoqCK9OGTq2RDODVUUZYPU/edit?usp=sharing)|Slides 6||
|2025-03-11|[Resampling techniques - accuracy vs robustness](https://docs.google.com/presentation/d/1dEpri9RjpqPSop5SBNv-TneoO0QYKMcyS0E5SEgueoQ/edit?usp=sharing)|Slides 7 + [Resampling from ISL](https://link.springer.com/chapter/10.1007/978-1-4614-7138-7_5)|- Read paper on [Stability](https://arxiv.org/abs/1310.0150)|
|2025-03-13|[Automated Model Selection](https://docs.google.com/presentation/d/1dEpri9RjpqPSop5SBNv-TneoO0QYKMcyS0E5SEgueoQ/edit?usp=sharing)|Slides 7 + [caret library](https://topepo.github.io/caret/index.html) + [ISL on resampling](https://link.springer.com/chapter/10.1007/978-1-4614-7138-7_5)|[Project 1] Due|
|2025-03-18|Spring Break|||
|2025-03-20|Spring Break|||
|2025-03-25|[Clustering - Kmeans](https://docs.google.com/presentation/d/1DoWbNOEZGeZkNr4wb9u198GlnS45rxWFoaOwEvMPn-E/edit?usp=sharing)|ISL 10.2||
|2025-03-27|[Clustering - Kmeans continued](https://docs.google.com/presentation/d/1RAzfwkMSzoEgLT8hYw0zL7KxCAM4jnjbCyxZgb84QxU/edit?usp=sharing)|ISL 10.2||
|2025-04-01|K-means with real data|ISL 10.2||
|2025-04-03|[Hierarchical clustering](https://docs.google.com/presentation/d/1b-iWZSg5w9dm-01miUvtIIShjctAYKQo2tFMzX3OiXI/edit?usp=sharing)|ISL 10.2|[Homework 4]|
|2025-04-08|[Hierarchical clustering with real data](https://docs.google.com/presentation/d/15lNq4NQrEOzcsR0uhkltQfJrSiFQcx-FQPCh_7g9KRQ/edit?usp=sharing)|ISL 10.2||
|2025-04-10|[DBSCAN](https://docs.google.com/presentation/d/18exR7A0qTMJsclSOFJz4_IaOhvEFPhzqo4MuW6rYVmI/edit?usp=sharing)|[DBSCAN from KDNuggets](https://www.kdnuggets.com/2020/04/dbscan-clustering-algorithm-machine-learning.html)||
|2025-04-15|[feature engineering - with text](https://docs.google.com/presentation/d/1BzfHDaGuvM2Vv6Vbi8YF55ZjzFAYFCcaAGcjpl9XkPE/edit?usp=sharing)|[Pre-processing Text](https://www.cambridge.org/core/journals/political-analysis/article/text-preprocessing-for-unsupervised-learning-why-it-matters-when-it-misleads-and-what-to-do-about-it/AA7D4DE0AA6AB208502515AE3EC6989E) + [Speech and Language Chapter 6.5](https://web.stanford.edu/~jurafsky/slp3/)||
|2025-04-17|Working with text data continued|||
|2025-04-22|[Independent Component Analysis](https://docs.google.com/presentation/d/141-Q9FFzFjAZr32RXv4D5cBd0SK38DmEzZnxVdGOma0/edit?usp=sharing)|[Stanford ICA Slides](http://statweb.stanford.edu/~tibs/sta306bfiles/ica.pdf)||
|2025-04-24|[Models on text including Wordfish](https://docs.google.com/presentation/d/1so4mBtaC2f881o2-20RKPyOi_xdxcXm_psQ5UPPECnw/edit?usp=sharing)||[Homework 5]|
|2025-04-29|Going over final projects in class|||
|2025-05-01|Going over final projects in class + what we didn't teach||[Project 2]|


### Logistics
Lectures:
  TuTh 2:40pm - 3:55pm, 602 Hamilton Hall

### Teaching Team

- Wayne Tai Lee (wtl2109)
  - OH: TuTh 12-2pm at 324 Uris Hall
- Matt Shen (ms7079)
  - OH: Monday 11:30-1:30pm at 324 Uris Hall

#### Online Discussion
The TA and grader will check the online discussion for 30 minutes each weekday.
Do not expect an immediate response so please start your work early and understand
that you should post your questions more clearly.

### Grading
If your final grade is in [93-100], you will earn at least an A, [90-93) will earn at least an A-, [87-90) will earn at least a B+, etc. A grading curves may occur depending on the class performance but I will not curve downwards. I may not give out A+'s in this class.

#### - Homeworks (20%)
  - Late homeworks will receive 0 credit
  - Homeworks will receive 0 credit if the code + write up is not submitted in both the .ipynb/.Rmd AND the knitted PDF or HTML form.
#### - Projects (70%)
  - Late projects will be penalized by 50% for each day it's late.
  - Projects should be submitted on Canvas
#### - Participation (10%)
  - Instead of attendance, in class activities, recorded through Canvas, is how we'll grade this.
  - If you surpass 75% here, you'll receive the full credit for participation.

### Acknowledgement
A lot of these materials are based off the materials from Prof Vincent Dorie.
