# UN2103 - Applied Linear Regression Model

This class is designed for students without a linear algebra background who will
need to understand linear regression and its underlying properties.

### Expectations
#### - Learning outcomes
- Transition from learning via imitation to working backwards from the question
- Understand when to use linear regression for prediction or inference
- Be able to articulate counter examples for linear regression to fail
- Be able to simulate and confirm the mathematical derivations

#### - Your Job
  - Come to class, bring your laptop, take chances!
    - Run through the code and derivations in each lecture
    - Take summarized notes that augment the lectures
  - Give feedback in office hours or email, I don't want to waste your time
  - Participate and ask questions, this is not easy!
    - In class: forecast what should be done, compare with what is happening, then summarize the difference.
    - Online: describe what you observe, describe what you expect, communicate clearly.
    - To each other: summarize the conversation to ensure you're listening and think constructively before criticizing.
  - Academic honesty: https://www.cs.columbia.edu/education/honesty/

### People
Instructor:
Wayne Tai Lee: wtl2109

Teaching Assistant:
TBD

### Timeline
  I reserve the right to change the ordering and the content for the course throughout the semester.

  |Date|Topic|Reference|Due|
  |---|---|---|---|
  |2020-01-21|[Introduction, expectations, and transitions oh my!](https://drive.google.com/open?id=12GIwf8KVtYc7KN7C6eVC8c3R41LiQNtQlVBHTNv4HmA)|||
  |2020-01-23|[Reviewing Hypothesis Testing with R Simulations](https://drive.google.com/open?id=1zBjQ9G508s4PBlmMWR2_fofictjvj3Achw30BBCVmnc)|Any R Tutorial Videos on For-Loop, e.g. [R Tutorial Videos](https://www.stat.berkeley.edu/share/rvideos/R_Videos/R_Videos.html)|Make sure R is installed and running|
  |2020-01-28|[Deriving simple linear regression](https://docs.google.com/presentation/d/15m8XkAKZaDA4lsTJxvTaHekrFPXFVv22qZ6j5MDrBrg/edit?usp=sharing)|Text 2.1.1|[Homework 1](homeworks/hw1_prerequisites.md)|
  |2020-01-30|[Linking regression coefficients to the data generation process](https://docs.google.com/presentation/d/1NalZQ2EWSt3Z7ojP0iPOt902VyJfRrP-MsEyc8qXoE0/edit?usp=sharing)|Text 2.7.1||
  |2020-02-04|[Linking math to simulations](https://docs.google.com/presentation/d/1-TaFO-3j1-een-w3pjExEbKQXdrJqV6ZI-AOZc9ZQHM/edit?usp=sharing)|Text 2.7.3||
  |2020-02-06|[Properties of the regression coefficients](https://us.edstem.org/courses/182/lessons/670/slides/2979)|Text 2.7.2 + 2.7.3||
  |2020-02-11|[Properties of the regression coefficients](https://us.edstem.org/courses/182/lessons/670/slides/2979)|Text 2.7.2 + 2.7.3|[Homework 2](homeworks/hw2_optimization.md)|
  |2020-02-13|[Diagnostics of SLR](https://docs.google.com/presentation/d/1_ydaxURpK2F-YkuGXKHxYF9rJ4bRAi6B9ftnyh_LXrM/edit?usp=sharing)|Text 3.1||
  |2020-02-18|Midterm 1|||
  |2020-02-20|[Bootstrapping](https://us.edstem.org/courses/182/lessons/724/slides/3287)|[Stanford Notes](http://statweb.stanford.edu/~tibs/sta305files/FoxOnBootingRegInR.pdf)||
  |2020-02-25|[Inferring the true line](https://us.edstem.org/courses/182/lessons/688/slides/3343)|Text 2.3||
  |2020-02-27|[Predicting new data points](https://us.edstem.org/courses/182/lessons/688/slides/3357)|Text 2.4||
  |2020-03-03|[Linear algebra view of linear regression](https://us.edstem.org/courses/182/lessons/765/slides/3496)|Text 5.2|[Homework 3](homeworks/hw3_simple_lin_reg.md)|
  |2020-03-05|[Simultaneous inference on coefficients](https://us.edstem.org/courses/182/lessons/767/edit/slides/3504)|||
  |2020-03-10|Class suspended due to coronavirus|||
  |2020-03-12|[Issues with multiple variables](https://us.edstem.org/courses/182/lessons/770/slides/3524) and [lecture - can bad features hurt](https://vimeo.com/398651931) and [lecture - collinearity](https://vimeo.com/398652055)||[Homework 4](homeworks/hw4_pred_inference.md)|
  |2020-03-17|Spring Recess No Class|||
  |2020-03-19|Spring Recess No Class|||
  |2020-03-24|Class cancelled due to COVID|||
  |2020-03-26|[Cross Validation](https://us.edstem.org/courses/182/lessons/734/slides/3362) and [lecture](https://vimeo.com/398680410)|||
  |2020-03-31|Review session||[Homework 5](homeworks/hw5_adding_features.md)|
  |2020-04-02|Midterm 2|||
  |2020-04-07|[Interactions, polynomials, and categorical variables for X](https://us.edstem.org/courses/182/lessons/865/slides/3953):<br>- [part1 on categorical X](https://vimeo.com/403745129)<br>- [part2 on polynomials](https://vimeo.com/403753144)<br>- [part3 on interactions](https://vimeo.com/403773071)|||
  |2020-04-09|[Logistic regression](https://us.edstem.org/courses/182/lessons/906/slides/4169) with [vimeo link](https://vimeo.com/403816949)|Text 4.1||
  |2020-04-14|[DAGs: Changing significance when adding/deleting features](https://us.edstem.org/courses/182/lessons/912/slides/4193) with [vimeo link](https://vimeo.com/403836156)||[Homework 6](homeworks/hw6_challenges.md)|
  |2020-04-16|[Variable selection day 1](https://us.edstem.org/courses/182/lessons/1060/slides/5022), no video|||
  |2020-04-21|[Variable selection day 2](https://us.edstem.org/courses/182/lessons/1060/slides/5031), no video|||
  |2020-04-23|[Wrong models in linear regression + instrumental variables](https://us.edstem.org/courses/182/lessons/1110/slides/5285), no video|||
  |2020-04-28|[Weighted Least squares](https://us.edstem.org/courses/182/lessons/1112/slides/5309), no video||[Homework 7](homeworks/hw7_extended_topics.md)|
  |2020-04-30|What we don't know|||
  |2020-05-08|||Final Exam|


### Logistics
Lectures:
  [TuTh 8:40pm - 9:55pm, Location: 627 Seeley W. Mudd Building](https://www.vergil.registrar.columbia.edu/)

Office Hours:
- Owen: M 3-4pm and W 4-5pm at the School of Social Works 10th Floor Lounge (1255 Amsterdam Ave)
- Wayne: Th 10am-Noon at 715 Watson Hall (612 W 115th St)


### Grading
If your final grade is in \[93-97), you will earn at least an A, \[90-93) will earn at least an A-, \[87-90) will earn at least a B+, etc. A grading curves may occur depending on the class performance but will not curve downwards. I may not give out A+

#### - Homeworks (10%)
  - Late homeworks will receive 0 credit
  - Homework solutions will exist in R
  - Your lowest homework grade will be dropped
  - No make-up homeworks will be granted even if you registered late to the class
  - Please export all homeworks in PDF files following these [instructions](../../setup/math_and_code.md)
#### - Exams (85%)
  - Midterms (15% for midterm 1 and 30% for Midterm 2)
  - Final (40%)
#### - Participation (5%)
  - This will be based on in-class online activities

### Prerequisites
  - Some familiarity with R or UN2102 Applied Statistical Computing
    - Need to know how to write a loop and simulate data from known distributions
  - An introductory statistics class
    - Basic probability distributions (e.g. Gaussian, binomial distributions and their likelihoods)
    - Basic hypothesis testing (e.g. t-test)
    - Properties of summary statistics

### Textbooks / Supplies
[A modern approach to regression with R by Simon J. Sheather, available via CLIO](https://clio.columbia.edu/catalog/7900489)

### Acknowledgement
A lot of these materials are based off the materials from Prof Ronald Neath and Prof Gabriel Young.

