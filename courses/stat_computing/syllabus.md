# Applied Statistical Computing
UN2102 - Spring 2021

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
- TBD

### Timeline
I reserve the right to change the ordering and the content for the course throughout the semester.

|Date|Topic|Reference|Due|
|---|---|---|---|
|2021-01-12|- [Statistical computing](lectures/lec1/lec1.md) and Intro Stat Review|||
|2021-01-14|- Motivating example: [recreating Fisher's results](lectures/lec1/fisher_in_R.md)|- read.csv() Text 10.2.1<br>- filtering Text 3.2.4<br>- For-loops Text 7.1.1<br>- vectors Text 2.1.1, 2.4.2<br>- boolean operations Text 7.2<br>- writing functions 1.3|Get [R](https://cran.rstudio.com/) installed, then [R studio](https://rstudio.com/products/rstudio/download/) installed|
|2021-01-19|- [Fisher's continued](lectures/lec1/fisher_in_R.md)<br>- [Data types](lectures/lec1/functions_and_data.md)|Same as previous class + Text 1.4.1,1.4.2||
|2021-01-21|- [vectors in R](lectures/lec1/vectors_in_R.md)<br>- [Random functions](lectures/lec2/builtin_functions_in_R.md)<br>|Text 2.* + Text 5.* |[Homework 1](homeworks/hw1.md)|
|2021-01-26|- [Random functions](lecture/lec2/builtin_functions_in_R.md)|7.3, 7.4, 7.5, 7.6||
|2021-01-28|- [Writing functions in R](lectures/lec2/writing_functions_in_R.md)|Text 1.3||
|2021-02-02|- [For loops](lectures/lec3/loops_in_R.md) <br>- [if/else](lectures/lec3/ifelse_in_R.md)|Text 7.1.1 + 7.1*|[Homework 2](homeworks/hw2.md)|
|2021-02-04|Review session|||
|2021-02-09|Take-Home Midterm 1|||
|2021-02-11|[Data visualization - baseR](https://us.edstem.org/courses/181/lessons/744/slides/3422)|Text 12||
|2021-02-16|[lists](https://us.edstem.org/courses/181/lessons/771/slides/3536)|Text 4||
|2021-02-18|[Data frames](https://us.edstem.org/courses/181/lessons/773/slides/3551) and [JOINS](https://us.edstem.org/courses/181/lessons/778/slides/3567)|Text 5||
|2021-02-23|[*apply functions and vectorized calculations](https://us.edstem.org/courses/181/lessons/783/slides/3601)||[Homework 3](homeworks/hw3.md)|
|2021-02-25|[tapply, aggregate, and data wrangling](https://us.edstem.org/courses/181/lessons/802/slides/3701)|||
|2021-03-02|Spring Recess No Class|||
|2021-03-04|Spring Recess No Class|||
|2021-03-09|Data wrangling continued||[Homework 4](homeworks/hw4.md)|
|2021-03-11|TBD|||
|2021-03-16|TBD|||
|2021-03-18|[Reading in different types of data](https://us.edstem.org/courses/181/lessons/870/slides/3962) and [lec-vimeo](https://vimeo.com/399962856) or [lec-優酷](https://v.youku.com/v_show/id_XNDYwMTQ5ODUyOA==.html)|||
|2021-03-23|Review session||[Homework 5](homeworks/hw5.md)|
|2021-03-25|Take-Home Midterm 2|||
|2021-03-30|[Basic text manipulation - dates](https://us.edstem.org/courses/181/lessons/872/slides/3972) and [lec-vimeo](https://vimeo.com/400405775) or [lec-優酷](https://v.youku.com/v_show/id_XNDYwMzM2ODkwMA==.html)|Text 11||
|2021-04-01|[Regular expression](https://us.edstem.org/courses/181/lessons/872/slides/3977) and [lec-vimeo](https://vimeo.com/400420922) or [lec-優酷](https://v.youku.com/v_show/id_XNDYwMzM4MjA0MA==.html)|Text 11||
|2021-04-06|[Debugging](https://us.edstem.org/courses/181/lessons/873/slides/4012) with [Vimeo lectures](https://vimeo.com/407632826) and [優酷 lectures](https://v.youku.com/v_show/id_XNDYyMTU3MTE2OA==.html)|Text 13||
|2021-04-08|[Scraping](https://us.edstem.org/courses/181/lessons/871/edit/slides/3970) with [vimeo lectures](https://vimeo.com/404714829) and [優酷 lecture](https://v.youku.com/v_show/id_XNDYyMTU3MDg0MA==.html) vs calling [APIs](https://us.edstem.org/courses/181/lessons/871/edit/slides/4013) with [vimeo lecture](https://vimeo.com/404715597) and [優酷 lecture](https://v.youku.com/v_show/id_XNDYyMTU3MDQ1Ng==.html)|Many online blogs teach this, I would read them after listening to these lectures|[Homework 6](homeworks/hw6.md)|
|2021-04-13|[Simulations and permutations](https://us.edstem.org/courses/181/lessons/746/edit/slides/4083)<br> Simulation video on [vimeo](https://vimeo.com/408097921) and [優酷](https://v.youku.com/v_show/id_XNDYzMzk3MzEyNA==.html) <br> Permutation video on [vimeo](https://vimeo.com/408097666) and [優酷](https://v.youku.com/v_show/id_XNDYzMzk3MzM2NA==.html)|||
|2021-04-15|[Introduction to Version Control and Git](https://us.edstem.org/courses/181/lessons/881/slides/4073) no pre-lecture videos for this|[Change code on GitHub directly](https://guides.github.com/activities/hello-world/)||
|2021-04-20|[Entering tidyverse with Data Visualization ggplot() and `%>%`](https://us.edstem.org/courses/181/lessons/882/slides/4088)<br> ggplot video on [Vimeo](https://vimeo.com/409003549) and [優酷](https://v.youku.com/v_show/id_XNDYzNjk0MDAzNg==.html) <br> `%>%` operator video on [Vimeo](https://vimeo.com/409003734) and [優酷](https://v.youku.com/v_show/id_XNDYzNjkzOTY5Mg==.html)|[Online Tutorials](http://r-statistics.co/Complete-Ggplot2-Tutorial-Part1-With-R-Code.html)||
|2021-04-22|What we don't know||[Homework 7](homeworks/hw7.md)|
|2021-04-??|||Take-Home Final Exam|


### Logistics
Lectures:
  [TuTh 4:10pm - 5:25pm, Zoom Link on Canvas](https://vergil.registrar.columbia.edu/#/courses/APPLIED%20STATISTICAL%20COMPUTING)

Office Hours:
  - Wayne: by appointment via Google Invites
  - TBD

### Grading
If your final grade is in [93-100], you will earn at least an A, [90-93) will earn at least an A-, [87-90) will earn at least a B+, etc. A grading curves may occur depending on the class performance but I will not curve downwards. I may not give out A+ in this class.

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
- You'll need at least 50% here to pass the class

##### Exam accomodations
In order to receive disability-related academic accommodations for this course, students must first be registered with their school Disability Services (DS) office. Detailed information is available online for both the [Columbia](https://health.columbia.edu/content/disability-services) and Barnard registration processes.

Refer to the appropriate website for information regarding deadlines, disability documentation requirements, and [drop-in hours](https://health.columbia.edu/getting-care/drop-offices/disability-services-drop-hours)(Columbia)/[intake session]() (Barnard).

For this course, students are not required to have testing forms or accommodation letters signed by faculty. However, students must do the following:
  - The Instructor section of the form has already been completed and does not need to be signed by the professor.
  - The student must complete the Student section of the form and submit the form to Disability Services.
  - Master forms are available in the Disability Services office or online: https://health.columbia.edu/services/testing-accommodations

### Prerequisites
- An introductory statistics class
  - Basic probability distributions (e.g. Gaussian, binomial distributions and their likelihoods)
  - Basic hypothesis testing (e.g. t-test)
  - Summary statistics
  - Histograms, boxplots, etc
- Some understanding of Microsoft Excel or Google Spreadsheets

### Textbooks / References
- [The Art of R Programming: Tour of Statistical Software Design](https://clio.columbia.edu/catalog/13882895) is available through CLIO
- [Advanced R](https://adv-r.hadley.nz/) is available online
- [Past course notes](lectures/learning_r_intro.md) is available online

### Acknowledgement
A lot of these materials are based off the materials from Prof Thibault Vatter and Prof Gabriel Young.
