# Linear Regression Model
GU4205/5205 - Fall 2019

### Expectations
#### - Learning outcomes
- Understand when linear regression is used for a descriptive, predictive, or prescriptive purpose
- Understand the linear algebra behind linear regression
- Be able to run, diagnose, and improve your linear regression models using common methodologies
- Be able to construct counter examples for linear regression to fail
- Be able to simulate and confirm the mathematical derivations

#### - Your Job
  - Come to class, bring your laptop, take chances!
    - Run through the code and derivations in lecture
    - Take notes that augment the lectures
  - Give feedback in office hours or e-mail, I don't want to waste your time.
  - Participate and ask questions, this is not easy!
    - In class: forecast what should be done, compare with what is happening, then summarize the difference.
    - Online: describe what you observe, describe what you expect, communicate clearly.
    - To each other: summarize the conversation to ensure you're listening and think constructively before criticizing.
  - Academic honesty: https://www.cs.columbia.edu/education/honesty/

### People
Instructor:
Wayne Tai Lee: wtl2109

Teaching Assistant(s):
Yian Huang: yh3209
Navid Ardeshir: na2844

### Timeline
  I reserve the right to change the ordering and the content for the course throughout the semester.

  |Date|Topic|Reference|Due|
  |---|---|---|---|
  |2019-09-04|[Introduction, expectations, and transitions oh my!](https://docs.google.com/presentation/d/1dxcAYHB4ZBEf95U7uzv_dQf2LJIUBTBXoYTtBgvNbyc/edit?usp=sharing)|Textbook Chapter 1.1 + 1.2 + 1.5 + 1.6.1||
  |2019-09-09|[Programming for simulations](https://drive.google.com/open?id=1hRqErJ5nl0U3-kxm58yBqwaPF8DiEfgiPMS9tS56eyk)|Any R Tutorial Videos on For-Loop|Reading if you don't know R: [R Tutorial Videos](https://www.stat.berkeley.edu/share/rvideos/R_Videos/R_Videos.html)|
  |2019-09-11|[From optimizing objective functions to modeling data generation](https://drive.google.com/open?id=1rXLGotjE9PR5LtiFw9ijYAuv4VbFWPQl63rva95w2Zc)|Textbook Chapter 1.3 + 1.6|Homework 1: Pre-requisites|
  |2019-09-16|[Purpose 1 - inference on the model](https://drive.google.com/open?id=1RZA2ZhE4FQQJKPH_-SoUdJ9LQ_QqgJJDYou_RXHeqA4)|Textbook Chapter 2.3||
  |2019-09-18|[Purpose 2 - predictions](https://drive.google.com/open?id=16G-S4F-WgjrQdnaygN-bxD7ZV5JkH-FBo1SxctZe0i4)|Textbook Chapter 2.4-2.6|Homework 2: Simulations|
  |2019-09-23|[Same estimation but different uncertainties](https://drive.google.com/open?id=1psSekpOGOsMwVCEXFydWdH-2unMZhaOyuAnlTPe4fjQ) |All previous references||
  |2019-09-25|[Diagnostics of SLR](https://drive.google.com/open?id=1YjfV4Z-E22tn05KV6sN1vLcUqkRs8892vjGM4ViyliM)|Textbook Chapter 3.1-3.3||
  |2019-09-30|[Two extremes: likelihoods and various bootstrap methods](https://drive.google.com/open?id=1IprAddqBQRXSRuUJ0XlgAQQ_hlsM4ypwLaci4n6PwPQ)|Textbook Chapter 1.8|Homework 3: Inference and Prediction|
  |2019-10-02|Midterm review|||
  |2019-10-07|Midterm||Homework 4: Diagnostics|
  |2019-10-09|[Categorical variables and transformations](https://drive.google.com/open?id=1TPwcQk2rWFaQwTGt5d9_ATNH82a9L0CT8770hM00wr0)|Textbook Chapter 14.1-14.3||
  |2019-10-14|[Linear algebra review and more](https://drive.google.com/open?id=18lMRfyZrKGzR680wwEZXmNMEJBHxFSFxaULD0MqA3yw)|Textbook Chapter 5.1-5.8||
  |2019-10-16|[Multivariate linear regression](https://drive.google.com/open?id=1NPUTOPzMzLWI3FFxKSy5cMdXPgdFwbrMaTrfN7NFEZU)|Textbook Chapter 6.1-6.7 (not 6.5)||
  |2019-10-21|[Simultaneous inference](https://docs.google.com/presentation/d/105WS1sROIdLEx9iBGtYoOvEjsFPTjwDMLF4q6uPwpT4/edit?usp=sharing) <br> and <br>  [Impact of adding a variable and interactions](https://drive.google.com/open?id=1cV-HUlNh_fBnF4hTR4HlP8UM1rySLvYb4ZUdQFQMCwk)|Textbook Chapter 7.1, 8.2, 8.4||
  |2019-10-23|[Ecological correlation and WLS](https://drive.google.com/open?id=1djTQEOfKZYs5OlFEAR02tvcWiERP9kWpzr337GCxcyQ)|Textbook Chapter 11.1|Homework 5: categorical data and bootstrap|
  |2019-10-28|[BLUE and James-Stein](https://drive.google.com/open?id=1YtDmBqObb4jF88nP3mtVZha09tFf95Meee1jXpJErU0)|Textbook Theorem 1.11||
  |2019-10-30|[F-test, ANOVA, and regression](https://docs.google.com/presentation/d/1C1urySWh9IZ02wC0sjJv1PQpJa1m93r_ILAeiudtEcU/edit?usp=sharing)|Textbook Chapter 6.5|Homework 6: multivariate regression|
  |2019-11-04|No Class - Election Day|||
  |2019-11-06|[Significance changing when adding/deleting features](https://docs.google.com/presentation/d/1hEePP7d1oRVqgaSYZn5lA1bz4_o_aY0nqThzT3deIJw/edit?usp=sharing)|||
  |2019-11-11|Practice||Homework 7: WLS and Biased Estimators|
  |2019-11-13|Midterm 2|||
  |2019-11-18|[PCA regression](https://docs.google.com/presentation/d/18yJoSdWcC5MR05pszZ6mKgDfwIpuJ77T0_KU9LwlS60/edit?usp=sharing)|||
  |2019-11-20|[Regularization](https://docs.google.com/presentation/d/1cQU9tlle-OrM7Qhi6b-5de4q3L9DEKYM63Nb12-Uh4A/edit?usp=sharing)|||
  |2019-11-25|[Wrong models in linear regression + instrumental variables](https://docs.google.com/presentation/d/1pk5hOWi1vET_QOCvlcG5PZWIJ7uPVyDV1LrQSoXrmQA/edit?usp=sharing)||Homework 8: simulating counter examples|
  |2019-11-27|No Class|||
  |2019-12-02|[Variable Selection & Delta Method](https://docs.google.com/presentation/d/1HHI9MTf2QWy_B6DpF-LuOFSlwR68FCcsVfrtr3BYd3I/edit?usp=sharing)|||
  |2019-12-04|Linear model workflow + Review|||
  |2019-12-09|Review and wrap-up!||Homework 9: Something easy|
  |[Final Schedule](https://ssol.columbia.edu/cgi-bin/ssol/JDhtDfHHWFu6UL1DanlwaB/?p%.5Fr%.5Fid=JDhtDfHHWFu6UL1DanlwaB&p%.5Ft%.5Fid=1&tran%.5B1%.5D%.5Fletter=S&tran%.5B1%.5D%.5Fterm%.5Fid=20193&tran%.5B1%.5D%.5Ftran%.5Fname=scex)||Final Exam|You!|


### Logistics
Lectures:
  [MW 2:40pm - 3:55pm, Location: 301 Pupin Laboratories](https://www.vergil.registrar.columbia.edu/#/courses/48472)
Office Hours:
  Tu 2:00pm - 4:30pm, Location 610 Watson Hall (612 W 115th St 6F), led by Wayne
  Th 2:00pm - 4:30pm, Location 610 Watson Hall (612 W 115th St 6F), led by Wayne
  F 9:00am-12:00pm, Location 10th floor School of Social Works lounge area, led by Yian Huang
  Tu 12:30-3:20pm (sharp, not delayed), Location 10th floor School of Social Works lounge area, led by Navid Ardeshir

### Grading
If your final grade is in [93-97), you will earn at least an A, [90-93) will earn at least an A-, [87-90) will earn at least a B+, etc. A grading curves may occur depending on the class performance but will not curve downwards.

#### - Homeworks (15%)
  - Late homeworks will receive 0 credit
  - Homework solutions will exist in R
  - Your lowest homework grade will be dropped
  - No make-up homeworks will be granted even if you registered late to the class
#### - Exams (80%)
  - Midterms (25% each)
  - Final (30%)
#### - Participation (5%)
  - This will be based on in-class online activities
#### - Possible recovery
  Your final percentage grade will be the maximum of the following 4 values, the idea is that your final can cover part of your midterm grade:
  - Homework * 0.15 + Midterm1 * 0.25 + Midterm2 * 0.25 + Final * 0.3 + Surveys * 0.05
  - Homework * 0.15 + Midterm1 * 0.15 + Midterm2 * 0.15 + Final * 0.5 + Surveys * 0.05
  - Homework * 0.15 + Midterm1 * 0.15 + Midterm2 * 0.25 + Final * 0.4 + Surveys * 0.05
  - Homework * 0.15 + Midterm1 * 0.25 + Midterm2 * 0.15 + Final * 0.4 + Surveys * 0.05

### Prerequisites
  - Some familiarity with R or Python
    - Need to know how to write a loop and visualize data
  - An introductory statistics class
    - Basic probability distributions (e.g. Gaussian, binomial distributions and their likelihoods)
    - Basic hypothesis testing (e.g. t-test)
    - Summary statistics
  - Basic linear algebra  

### Textbooks / Supplies
Applied Linear Regression Models 4th Edition by Kutner, Nachtscheim, and Neter
Statistical Models Theory and Practice by David A. Freedman


### Acknowledgement
A lot of these materials are based off the materials from Prof Ronald Neath and Prof Gabriel Young.
