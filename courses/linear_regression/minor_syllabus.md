# UN2103 - Applied Linear Regression Model

This class introduces linear regression as a foundational tool for
prediction and inference with an emphasis on simulations and challenges
faced in application.

### Expectations
#### - Learning outcomes
- Transition from learning via imitation to working backwards from the question
- Understand when to use linear regression for data mining, prediction, or inference
- Be able to articulate counter examples for linear regression to "fail"
- Be able to fit, evaluate, and improve models
- Learn to simulate and confirm basic mathematical results

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

### How to get help
- Office hours:
  - Mon/Wed 10-Noon with Wayne Tai Lee (wtl2109) at 324 Uris Hall (except 11/1)
  - Th 10-noon with Irene Chang (bnc2119) at 201 Uris Hall
- [Statistics daily help room](https://stat.columbia.edu/help-room/)

### Timeline
  I reserve the right to change the ordering and the content for the course throughout the semester.

  |Date|Topic|Reference|Due|
  |---|---|---|---|
  |2023-09-06|[Introduction, expectations, and transitions oh my!](https://drive.google.com/open?id=12GIwf8KVtYc7KN7C6eVC8c3R41LiQNtQlVBHTNv4HmA)|||
  |2023-09-11|[Intro Stat Review Slides](https://docs.google.com/presentation/d/1XOCRjs4RgbjKfUD07R7cXZJ-CjZ1mnC0FRzUDwdR3Y0/edit?usp=sharing)|[Intro Stat Review Notes](lectures/modules/prereq-intro-stat.md)||
  |2023-09-13|[Quick R crash course](lectures/intro_R_crash.Rmd) (if you've taken 2102 you can skip)|[How to simulate the LLN](https://leewtai.github.io/courses/stat_computing/lectures/learning_r_lln.html)|[Homework 0](homeworks/applied/hw0_prerequisites_stat.md)|
  |2023-09-18|[Reviewing Hypothesis Testing with R Simulations](https://drive.google.com/open?id=1zBjQ9G508s4PBlmMWR2_fofictjvj3Achw30BBCVmnc) and [code template](lectures/hypoth_with_r_sim.Rmd)|[How to simulate the LLN](https://leewtai.github.io/courses/stat_computing/lectures/learning_r_lln.html)||
  |2023-09-20|[Deriving simple linear regression](https://docs.google.com/presentation/d/15m8XkAKZaDA4lsTJxvTaHekrFPXFVv22qZ6j5MDrBrg/edit?usp=sharing) and [code template](lectures/Regression_line_fitting.Rmd)|Text 2.1.1||
  |2023-09-25|[Linking regression coefficients to the data generation process](https://docs.google.com/presentation/d/1NalZQ2EWSt3Z7ojP0iPOt902VyJfRrP-MsEyc8qXoE0/edit?usp=sharing) and [code template](lectures/line_fit_to_linear_model.Rmd)|Text 2.7.1 + 2.7.2|[Homework 1](homeworks/applied/hw1_prerequisites.md)|
  |2023-09-27|[Linking math to simulations](https://docs.google.com/presentation/d/1-TaFO-3j1-een-w3pjExEbKQXdrJqV6ZI-AOZc9ZQHM/edit?usp=sharing) and [code template](lectures/clt_coefficients.Rmd)|Text 2.7.2 + 2.7.3|Read [Global Evidence on Economic Preferences](https://doi.org/10.1093/qje/qjy013) until Chapter IV.A|
  |2023-10-02|[Diagnostics of SLR - inference](https://docs.google.com/presentation/d/1_ydaxURpK2F-YkuGXKHxYF9rJ4bRAi6B9ftnyh_LXrM/edit?usp=sharing); if time allows then [Properties of the regression coefficients](https://docs.google.com/presentation/d/1IpFAEOFCMSw5cP-0_ldHx4xxDCljdJCPyngexhTAMSk/edit?usp=sharing)|Text 2.7.2 + 2.7.3 + 3.1||
  |2023-10-04|[code template for diagnostics](lectures/diagnostics.Rmd); [Diagnostics of SLR - prediction](https://docs.google.com/presentation/d/1_ydaxURpK2F-YkuGXKHxYF9rJ4bRAi6B9ftnyh_LXrM/edit?usp=sharing);||[Homework 2](homeworks/applied/hw2_optimization.md); Read [Statistical Models and Shoe Leather](https://psychology.okstate.edu/faculty/jgrice/psyc5314/Freedman_1991A.pdf)|
  |2023-10-09|Review|Text 2.3||
  |2023-10-11|Midterm 1|||
  |2023-10-16|[Inferring the true line](https://docs.google.com/presentation/d/1FvUqbEnp21BQuWU3I0UaeeL5qG7EBoTirjVlTxckYXY/edit?usp=sharing) and [Predicting new data points](https://docs.google.com/presentation/d/1FvUqbEnp21BQuWU3I0UaeeL5qG7EBoTirjVlTxckYXY/edit?usp=sharing); [code template](lectures/conf_vs_pred_intervals_for_the_line.Rmd)|Text 2.4||
  |2023-10-18|[Bootstrapping](https://docs.google.com/presentation/d/1A_K6gVhFnxoh71oNSbrwIJgJO5zORxYVgv2bM2wJQjg/edit?usp=sharing) and [code template](lectures/bootstrap.Rmd)|[Stanford Notes](http://statweb.stanford.edu/~tibs/sta305files/FoxOnBootingRegInR.pdf)||
  |2023-10-23|[Interactions, polynomials, and categorical variables for X](https://docs.google.com/presentation/d/1Mn_XMrKua-7kJRiesSFA43zqtXSxVcsAM23P0UkwQVA/edit?usp=sharing):<br>- [part1 on categorical X](https://vimeo.com/403745129)<br>- [part2 on polynomials](https://vimeo.com/403753144)<br>- [part3 on interactions](https://vimeo.com/403773071); [code_template](lectures/common_multivar.R)||[Homework 3](homeworks/applied/hw3_simple_lin_reg.md)|
  |2023-10-25|[Issues with multiple variables](https://docs.google.com/presentation/d/1h4NDHN1ipJ-QpAvC3GUHvEK9Wooxf9u4wB8R2RxOKgI/edit?usp=sharing) and [lecture - can bad features hurt](https://vimeo.com/398651931) and [lecture - collinearity](https://vimeo.com/398652055); [code template](lectures/high_dim.Rmd)|Text 2.6 + Text 5.2||
  |2023-10-30|[Simultaneous inference on coefficients](https://docs.google.com/presentation/d/1MRwyjDs-77l99HT0Mp4uFvFbzivt-fT9kmKVzSPPpPE/edit?usp=sharing); [code template](lectures/simultaneous_inference.Rmd)|||
  |2023-11-01|[Cross Validation](https://docs.google.com/presentation/d/1egvYy9Z73FTOXAIFIfP4qhldMUoAFS5-j2fozhNdd4g/edit?usp=sharing) and [lecture](https://vimeo.com/398680410) & [Logistic regression](https://docs.google.com/presentation/d/17VV5oyTYfwNl_1dKBg4DdXwB69qP3mSb9e2BNITRTtA/edit?usp=sharing) with [vimeo link](https://vimeo.com/403816949); [code template](lectures/logistic_reg.R)|Text 4.1|[Homework 4](homeworks/applied/hw4_pred_inference.md)|
  |2023-11-06|US ELECTIONS - NO CLASS|||
  |2023-11-08|Guest Speaker: John Andrew Chwe from Psychology & Review||[Trustworthiness of crowds is gleaned in half a second](https://static1.squarespace.com/static/5daf65330e17a4220c7707ce/t/64378dd57efb4b7d3b265a54/1681362389720/ChweFreemanSPPS.pdf); |
  |2023-11-13|[DAGs: Changing significance when adding/deleting features](https://docs.google.com/presentation/d/1N8Bm-aFaFlJ4LQ02swUOmfAcTmfuaQZTQZEgVW80b2E/edit?usp=share_link) with [vimeo link](https://vimeo.com/403836156); [simulation code](lectures/dag.R)|||
  |2023-11-15|Review||[Homework 5](homeworks/applied/hw5_applied.md)|
  |2023-11-20|Midterm 2|||
  |2023-11-22|THANKSGIVING HOLIDAY - NO CLASS|||
  |2023-11-27|Midterm retro & [WLS](https://docs.google.com/presentation/d/1Y5qLYXVuSUyTBjvP9UWLkIkAIW7jQRfTu4chjj8VJrA/edit?usp=sharing) with [code template](lectures/wls.R)|Special case of chapter 9||
  |2023-11-29|[Mixed models](https://docs.google.com/presentation/d/1O88kkbbnORjARW2ulNGEa9FjCV81IqmeKejbmdQzSek/edit?usp=sharing), [code template](lectures/mixed_models.Rmd)|Chapter 10||
  |2023-12-04|Paper discussion||Read [Why do people stay poor?](https://academic.oup.com/qje/article/137/2/785/6455333); [Homework 6](homeworks/applied/hw7_extended_topics.md)|
  |2023-12-06|Controlling for variables [code template](lectures/control_and_ivls.R)|||
  |2023-12-11|What we know and don't know||Homework 7 (due 12/13)|
  |2023-12-15|Final project or exam|||


### Logistics
Lectures:
  [MW 2:40pm - 3:55pm, Location: 517 Hamilton Hall](https://vergil.registrar.columbia.edu/#/courses/APPLIED%20LINEAR%20REG%20ANALYSIS)


### Grading
If your final grade is in \[93-100], you will earn at least an A, \[90-93) will earn at least an A-, \[87-90) will earn at least a B+, etc. A grading curves may occur depending on the class performance but will not curve downwards. I may not give out A+

#### - Homeworks (15%)
  - Late homeworks will receive 0 credit
  - Homework solutions will exist in R
  - Your lowest homework grade will be dropped
  - No make-up homeworks will be granted even if you registered late to the class
  - Please export all homeworks in PDF files following these [instructions](../../setup/math_and_code.md)
  - If you are not comfortable with LaTex, you can "write-in" the math afterwards.
#### - Exams (80%)
  - Midterms (15% for midterm 1 and 30% for Midterm 2)
  - Final Exam or Project (35%)
#### - Participation (5%)
  - This will be based on in-class online activities
  - You will receive the full 5% if you obtain 75% of this.

### Prerequisites
  - An introductory statistics class
    - Basic probability distributions (e.g. Gaussian, binomial distributions and their likelihoods)
    - Basic hypothesis testing (e.g. t-test)
    - Properties of summary statistics
  - Co-requisite: some familiarity with computing or UN2102 Applied Statistical Computing

### Textbooks / Supplies
- I'm hoping to write up some notes [here](lectures/README.md)
- Free text: [A modern approach to regression with R by Simon J. Sheather, available via CLIO](https://clio.columbia.edu/catalog/7900489)
- For mathematically curious students: [Statistical models: theory and practice](https://clio.columbia.edu/catalog/10285295)

### Acknowledgement
A lot of these materials are based off the materials from Prof Ronald Neath and Prof Gabriel Young.
