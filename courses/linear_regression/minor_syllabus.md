# UN2103 - Applied Linear Regression Model

This class introduces linear regression as a foundational tool for
prediction and inference with an emphasis on simulations and challenges
faced in application.

### Expectations
#### - Learning outcomes
- Transition from learning via imitation to working backwards from the question
- Understand when to use linear regression for prediction vs inference
- Be able to articulate counter examples for linear regression to "fail"
- Be able to simulate and confirm basic mathematical results for regression

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

### Teaching team
Wayne Tai Lee (instructor, wtl2109):
Office hours:
- Wed 9:30-11:30am at Watson Hall (612 W 115th St)
- By appointment (email wtl2109) if
  - it's personal
  - there are 3 or more of you
  (Remember to check Google calendar availability)

Teaching Assistant:
Shunan Sheng (TA, ss6574):
Office hours:
- TBD

[Statistics daily help room](https://stat.columbia.edu/help-room/)

### Timeline
  I reserve the right to change the ordering and the content for the course throughout the semester.

  |Date|Topic|Reference|Due|
  |---|---|---|---|
  |2022-09-07|[Introduction, expectations, and transitions oh my!](https://drive.google.com/open?id=12GIwf8KVtYc7KN7C6eVC8c3R41LiQNtQlVBHTNv4HmA)|||
  |2022-09-12|[Reviewing Hypothesis Testing with R Simulations](https://drive.google.com/open?id=1zBjQ9G508s4PBlmMWR2_fofictjvj3Achw30BBCVmnc)|[How to simulate the LLN](https://leewtai.github.io/courses/stat_computing/lectures/learning_r_lln.html)|Make sure R is installed and running|
  |2022-09-14|[Deriving simple linear regression](https://docs.google.com/presentation/d/15m8XkAKZaDA4lsTJxvTaHekrFPXFVv22qZ6j5MDrBrg/edit?usp=sharing)|Text 2.1.1|[Homework 1](homeworks/applied/hw1_prerequisites.md)|
  |2022-09-19|[Linking regression coefficients to the data generation process](https://docs.google.com/presentation/d/1NalZQ2EWSt3Z7ojP0iPOt902VyJfRrP-MsEyc8qXoE0/edit?usp=sharing)|Text 2.7.1|Read [Global Evidence on Economic Preferences](https://doi.org/10.1093/qje/qjy013) until Chapter IV.A|
  |2022-09-21|[Linking math to simulations](https://docs.google.com/presentation/d/1-TaFO-3j1-een-w3pjExEbKQXdrJqV6ZI-AOZc9ZQHM/edit?usp=sharing)|Text 2.7.3||
  |2022-09-26|[Properties of the regression coefficients](https://docs.google.com/presentation/d/1IpFAEOFCMSw5cP-0_ldHx4xxDCljdJCPyngexhTAMSk/edit?usp=sharing)|Text 2.7.2 + 2.7.3||
  |2022-09-28|[Properties of the regression coefficients](https://docs.google.com/presentation/d/1IpFAEOFCMSw5cP-0_ldHx4xxDCljdJCPyngexhTAMSk/edit?usp=sharing)|Text 2.7.2 + 2.7.3|[Homework 2](homeworks/applied/hw2_optimization.md)|
  |2022-10-03|[Diagnostics of SLR](https://docs.google.com/presentation/d/1_ydaxURpK2F-YkuGXKHxYF9rJ4bRAi6B9ftnyh_LXrM/edit?usp=sharing)|Text 3.1|Read [Statistical Models and Shoe Leather](https://psychology.okstate.edu/faculty/jgrice/psyc5314/Freedman_1991A.pdf)|
  |2022-10-05|[Inferring the true line](https://docs.google.com/presentation/d/1FvUqbEnp21BQuWU3I0UaeeL5qG7EBoTirjVlTxckYXY/edit?usp=sharing)|Text 2.3||
  |2022-10-10|[Predicting new data points](https://docs.google.com/presentation/d/1FvUqbEnp21BQuWU3I0UaeeL5qG7EBoTirjVlTxckYXY/edit?usp=sharing)|Text 2.4|[Homework 3](homeworks/applied/hw3_simple_lin_reg.md)|
  |2022-10-12|Midterm 1|||
  |2022-10-17|[Bootstrapping](https://docs.google.com/presentation/d/1A_K6gVhFnxoh71oNSbrwIJgJO5zORxYVgv2bM2wJQjg/edit?usp=sharing)|[Stanford Notes](http://statweb.stanford.edu/~tibs/sta305files/FoxOnBootingRegInR.pdf)||
  |2022-10-19|[Issues with multiple variables](https://docs.google.com/presentation/d/1h4NDHN1ipJ-QpAvC3GUHvEK9Wooxf9u4wB8R2RxOKgI/edit?usp=sharing) and [lecture - can bad features hurt](https://vimeo.com/398651931) and [lecture - collinearity](https://vimeo.com/398652055)|Text 5.2||
  |2022-10-24|[Simultaneous inference on coefficients](https://docs.google.com/presentation/d/1MRwyjDs-77l99HT0Mp4uFvFbzivt-fT9kmKVzSPPpPE/edit?usp=sharing)|||
  |2022-10-26|Catch-up!||[Homework 4](homeworks/applied/hw4_pred_inference.md)|
  |2022-10-31|[Interactions, polynomials, and categorical variables for X](https://docs.google.com/presentation/d/1Mn_XMrKua-7kJRiesSFA43zqtXSxVcsAM23P0UkwQVA/edit?usp=sharing):<br>- [part1 on categorical X](https://vimeo.com/403745129)<br>- [part2 on polynomials](https://vimeo.com/403753144)<br>- [part3 on interactions](https://vimeo.com/403773071)|||
  |2022-11-02|[Cross Validation](https://docs.google.com/presentation/d/1egvYy9Z73FTOXAIFIfP4qhldMUoAFS5-j2fozhNdd4g/edit?usp=sharing) and [lecture](https://vimeo.com/398680410)|||
  |2022-11-07|US ELECTIONS - NO CLASS|||
  |2022-11-09|[Logistic regression](https://docs.google.com/presentation/d/17VV5oyTYfwNl_1dKBg4DdXwB69qP3mSb9e2BNITRTtA/edit?usp=sharing) with [vimeo link](https://vimeo.com/403816949)|Text 4.1|[Homework 5](homeworks/applied/hw5_adding_features.md)|
  |2022-11-14|[DAGs: Changing significance when adding/deleting features](https://docs.google.com/presentation/d/1N8Bm-aFaFlJ4LQ02swUOmfAcTmfuaQZTQZEgVW80b2E/edit?usp=share_link) with [vimeo link](https://vimeo.com/403836156)|||
  |2022-11-16|Review|||
  |2022-11-21|Midterm 2|||
  |2022-11-23|THANKSGIVING HOLIDAY - NO CLASS|||
  |2022-11-28|[Variable selection day 1](https://us.edstem.org/courses/182/lessons/1060/slides/5022), no video|||
  |2022-11-30|[Variable selection day 2](https://us.edstem.org/courses/182/lessons/1060/slides/5031), no video||[Homework 6](homeworks/applied/hw6_final_project.md)|
  |2022-12-05|[Wrong models in linear regression + instrumental variables](https://us.edstem.org/courses/182/lessons/1110/slides/5285), no video|||
  |2022-12-07|[Weighted Least squares](https://us.edstem.org/courses/182/lessons/1112/slides/5309), no video|||
  |2022-12-12|What we don't know||[Homework 7]|
  |TBD|[Final project](homeworks/applied/final_proj_reproduce.md)|||



### Logistics
Lectures:
  [MW 2:40pm - 3:55pm, Location: 702 Hamilton Hall](https://vergil.registrar.columbia.edu/#/courses/APPLIED%20LINEAR%20REG%20ANALYSIS)


### Grading
If your final grade is in \[93-100], you will earn at least an A, \[90-93) will earn at least an A-, \[87-90) will earn at least a B+, etc. A grading curves may occur depending on the class performance but will not curve downwards. I may not give out A+

#### - Homeworks (15%)
  - Late homeworks will receive 0 credit
  - Homework solutions will exist in R
  - Your lowest homework grade will be dropped
  - No make-up homeworks will be granted even if you registered late to the class
  - Please export all homeworks in PDF files following these [instructions](../../setup/math_and_code.md)
#### - Exams (80%)
  - Midterms (15% for midterm 1 and 30% for Midterm 2)
  - Final Exam or Project (35%)
#### - Participation (5%)
  - This will be based on in-class online activities
  - You will receive the full 5% if you obtain 75% of this.

### Prerequisites
  - Some familiarity with R or UN2102 Applied Statistical Computing
    - Need to know how to write a loop and simulate data from known distributions
  - An introductory statistics class
    - Basic probability distributions (e.g. Gaussian, binomial distributions and their likelihoods)
    - Basic hypothesis testing (e.g. t-test)
    - Properties of summary statistics

### Textbooks / Supplies
- Our text: [A modern approach to regression with R by Simon J. Sheather, available via CLIO](https://clio.columbia.edu/catalog/7900489)
- For mathematically curious students: [Statistical models: theory and practice](https://clio.columbia.edu/catalog/10285295)

### Acknowledgement
A lot of these materials are based off the materials from Prof Ronald Neath and Prof Gabriel Young.
