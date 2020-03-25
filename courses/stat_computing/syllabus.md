# Applied Statistical Computing
UN2102 - Spring 2020

### Learning outcomes
- Manipulate data with different structures
- Explore data via visualization
- Tackle familiar statistical concepts using simulations
- Work backwards vs learning via imitation
- Write reproducible code
- Debug code


### Expectations
- Come to class, bring your laptop, take chances!
  - Run through the code in lecture
  - Take notes that augment the lectures
- Give feedback in office hours or e-mail, don't waste your time if you think a topic is not helpful
- Participate and ask questions, this is not easy!
  - In class: forecast what should be done, compare with what is happening, then summarize the difference.
  - Online: describe what you observe, describe what you expect, communicate clearly.
  - To each other: summarize the conversation to ensure you're listening and think constructively before criticizing.
- Academic honesty: https://www.cs.columbia.edu/education/honesty/

### People
Instructor:
Wayne Tai Lee: wtl2109

Teaching Assistant(s):
[Jialin Ouyang](http://stat.columbia.edu/department-directory/ph-d-students/): jo2559
[Ding Zhou](http://stat.columbia.edu/department-directory/ph-d-students/): dz2336

### Timeline
I reserve the right to change the ordering and the content for the course throughout the semester.

|Date|Topic|Reference|Due|
|---|---|---|---|
|2020-01-21|- [Statistical computing](lectures/lec1/lec1.md) <br> - [Recreating Fisher's results](lectures/lec1/fisher_in_R.md)|||
|2020-01-23|- [Fisher's continued](lectures/lec1/fisher_in_R.md)|- read.csv() Text 10.2.1<br>- filtering Text 3.2.4<br>- For-loops Text 7.1.1<br>- vectors Text 2.1.1, 2.4.2<br>- boolean operations Text 7.2<br>- writing functions 1.3|Get [R](https://cran.rstudio.com/) installed, then [R studio](https://rstudio.com/products/rstudio/download/) installed|
|2020-01-28|- [Fisher's continued](lectures/lec1/fisher_in_R.md)<br>- [Data types](lectures/lec1/functions_and_data.md)|Same as previous class + Text 1.4.1,1.4.2||
|2020-01-30|- [vectors in R](lectures/lec1/vectors_in_R.md)<br>- [Random functions](lectures/lec2/builtin_functions_in_R.md)<br>|Text 2.* + Text 5.* |[Homework 1](homeworks/hw1.md)|
|2020-02-04|- [Random functions](lecture/lec2/builtin_functions_in_R.md)|7.3, 7.4, 7.5, 7.6||
|2020-02-06|- [Writing functions in R](lectures/lec2/writing_functions_in_R.md)|Text 1.3||
|2020-02-11|- [For loops](lectures/lec3/loops_in_R.md) <br>- [if/else](lectures/lec3/ifelse_in_R.md)|Text 7.1.1 + 7.1*|[Homework 2](homeworks/hw2.md)|
|2020-02-13|Review session|||
|2020-02-18|Midterm 1|||
|2020-02-20|[Data visualization - baseR](https://us.edstem.org/courses/181/lessons/744/slides/3422)|Text 12||
|2020-02-25|[lists](https://us.edstem.org/courses/181/lessons/771/slides/3536)|Text 4||
|2020-02-27|[Data frames](https://us.edstem.org/courses/181/lessons/773/slides/3551) and [JOINS](https://us.edstem.org/courses/181/lessons/778/slides/3567)|Text 5||
|2020-03-03|[*apply functions and vectorized calculations](https://us.edstem.org/courses/181/lessons/783/slides/3601)||[Homework 3](homeworks/hw3.md)|
|2020-03-05|[tapply, aggregate, and data wrangling](https://us.edstem.org/courses/181/lessons/802/slides/3701)|||
|2020-03-10|Class cancelled for social distancing|||
|2020-03-12|Data wrangling continued||[Homework 4](homeworks/hw4.md) due 3/13|
|2020-03-17|Spring Recess No Class|||
|2020-03-19|Spring Recess No Class|||
|2020-03-24|Class cancelled given nation lockdown and moving situations|||
|2020-03-26|[Reading in different types of data](https://us.edstem.org/courses/181/lessons/870/slides/3962) and [lec-vimeo](https://vimeo.com/399962856) or [lec-優酷](https://v.youku.com/v_show/id_XNDYwMTQ5ODUyOA==.html)|||
|2020-03-31|Review session||[Homework 5](homeworks/hw5.md)|
|2020-04-02|Midterm 2|||
|2020-04-07|[Basic text manipulation - dates](https://us.edstem.org/courses/181/lessons/872/slides/3972) and [lec-vimeo](https://vimeo.com/400405775) or [lec-優酷](https://v.youku.com/v_show/id_XNDYwMzM2ODkwMA==.html)|Text 11||
|2020-04-09|[Regular expression](https://us.edstem.org/courses/181/lessons/872/slides/3977) and [lec-vimeo](https://vimeo.com/400420922) or lec-優酷|Text 11||
|2020-04-14|[Debugging](https://us.edstem.org/courses/181/lessons/873/slides/4012)|Text 13||
|2020-04-16|[Scraping](https://us.edstem.org/courses/181/lessons/871/edit/slides/3970) vs calling [APIs](https://us.edstem.org/courses/181/lessons/871/edit/slides/4013)|Many online blogs teach this, I would read them after listening to these lectures|Homework 6|
|2020-04-21|[Introduction to Version Control and Git](https://us.edstem.org/courses/181/lessons/881/slides/4073)|[Change code on GitHub directly](https://guides.github.com/activities/hello-world/)||
|2020-04-23|[Simulations and permutations](https://us.edstem.org/courses/181/lessons/746/edit/slides/4083)|||
|2020-04-28|[Entering tidyverse with Data Visualization ggplot() and `%>%`](https://us.edstem.org/courses/181/lessons/882/slides/4088)|[Online Tutorials](http://r-statistics.co/Complete-Ggplot2-Tutorial-Part1-With-R-Code.html)|Homework 7|
|2020-04-30|Putting things together and review|||
|[TBD](https://ssol.columbia.edu/cgi-bin/ssol/8qDDYeMUzcpWYvwaP3d6Sh/?p_r_id=8qDDYeMUzcpWYvwaP3d6Sh&p_t_id=1&tran%5B1%5D_tran_name=scel&tran%5B1%5D_term_id=20201&tran%5B1%5D_act=Update+View)||Final Exam|You!|


### Logistics
Lectures:
  [TuTh 4:10pm - 5:25pm, Location: TBD](https://vergil.registrar.columbia.edu/#/courses/APPLIED%20STATISTICAL%20COMPUTING)

Office Hours:
  - [Ding](http://stat.columbia.edu/department-directory/ph-d-students/): M 5-6pm and W 1-2pm at the School of Social Works 10th Floor Lounge (1255 Amsterdam Ave)
  - [Jialin](http://stat.columbia.edu/department-directory/ph-d-students/): M 3-4pm and W 4-5pm at the School of Social Works 10th Floor Lounge (1255 Amsterdam Ave)
  - Wayne: Th 1-3pm 715 Watson Hall + Wed 9-11am 601 Watson Hall

### Grading
If your final grade is in [93-97), you will earn at least an A, [90-93) will earn at least an A-, [87-90) will earn at least a B+, etc. A grading curves may occur depending on the class performance but I will not curve downwards. I may not give out A+ in this class.

#### - Homeworks (15%)
- Late homeworks will receive 0 credit
- Homework solutions will exist in R
- Your lowest homework grade will be dropped (this is for students who add this course late)
  - No make-up homeworks will be granted even if you registered late to the class
- Please export all homeworks in PDF files following these [instructions](../../setup/math_and_code.md)
  - If you want to learn how to set up Jupyter Notebooks with R, follow these [instructions](../../setup/conda_and_navigator_setup.md)

#### - Exams (80%)
- Midterms (25% each)
- Final (30%)

#### - Participation (5%)
- This will be based on in-class online activities

##### Exam accomodations
In order to receive disability-related academic accommodations for this course, students must first be registered with their school Disability Services (DS) office. Detailed information is available online for both the [Columbia](https://health.columbia.edu/content/disability-services) and Barnard registration processes.

Refer to the appropriate website for information regarding deadlines, disability documentation requirements, and [drop-in hours](https://health.columbia.edu/getting-care/drop-offices/disability-services-drop-hours)(Columbia)/[intake session]() (Barnard).

 

For this course, students are not required to have testing forms or accommodation letters signed by faculty. However, students must do the following:

·         The Instructor section of the form has already been completed and does not need to be signed by the professor.

·         The student must complete the Student section of the form and submit the form to Disability Services.

·         Master forms are available in the Disability Services office or online: https://health.columbia.edu/services/testing-accommodations


### Prerequisites
- An introductory statistics class
  - Basic probability distributions (e.g. Gaussian, binomial distributions and their likelihoods)
  - Basic hypothesis testing (e.g. t-test)
  - Summary statistics
  - Histograms, boxplots, etc
- Some understanding of Microsoft Excel or Google Spreadsheets

### Textbooks / Supplies
[The Art of R Programming: Tour of Statistical Software Design](https://clio.columbia.edu/catalog/13882895) is available through CLIO

### Acknowledgement
A lot of these materials are based off the materials from Prof Thibault Vatter and Prof Gabriel Young.
