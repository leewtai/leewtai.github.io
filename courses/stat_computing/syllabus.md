# Applied Statistical Computing
UN2102 - Spring 2021

### Learning outcomes
- Manipulate data with different structures
- Explore data via visualization
- Tackle familiar statistical concepts using simulations
- Solving problems by working backwards and decomposing complex tasks
- Write reproducible code
- Debug code


### Expectations
- Come to class, bring your laptop, take chances!
  - Run through the code in lecture
  - Take notes that augment the lectures
- Give feedback, don't waste your time if you think a topic is not helpful
- Participate and ask questions, this is not easy!
  - In class: forecast what should be done, compare with what is happening, then summarize the difference.
  - Online: describe what you observe, describe what you expect, communicate clearly.
  - To each other: summarize the conversation to ensure you're listening and think constructively before criticizing.
- Academic honesty: https://www.cs.columbia.edu/education/honesty/

### People
Instructor:
Wayne Tai Lee: wtl2109

Teaching Assistant(s):
- Andrew Davison: ad3395
- Navid Ardeshir: na2844

### Timeline
I reserve the right to change the ordering and the content for the course throughout the semester.

|Date|Topic|Reference|Due|
|---|---|---|---|
|2021-01-12|- [Why statistical computing](https://docs.google.com/presentation/d/1RH8OgxPhIbMTQdqKTUUbjtg65LER0OM8PM6M6g1jYWg/edit?usp=sharing)|||
|2021-01-14|- [Variables, vectors, and functions on vectors](https://docs.google.com/presentation/d/1dOFhuoEEIcQXauf6qd5FKMzbcJaiVUNROptup1Ooktw/edit?usp=sharing)|[Simulating LLN](https://leewtai.github.io/courses/stat_computing/lectures/learning_r_lln.html)|Get [R](https://cran.rstudio.com/) installed, then [R studio](https://rstudio.com/products/rstudio/download/) installed|
|2021-01-19|- [For-loops](https://docs.google.com/presentation/d/1yiEH4INA9TFzXFLvl1HgFziXbKspdrogSlSyYpTJmK8/edit?usp=sharing)|[Simulating LLN](https://leewtai.github.io/courses/stat_computing/lectures/learning_r_lln.html)||
|2021-01-21|- [Recreating Fisher's results](https://leewtai.github.io/courses/stat_computing/lectures/lec1/fisher_in_R.html)|[Past course notes on subsetting](https://leewtai.github.io/courses/stat_computing/lectures/learning_r_data_viz.html)||
|2021-01-26|- [Data frames and booleans](https://leewtai.github.io/courses/stat_computing/lectures/learning_r_data_viz.html)|||
|2021-01-28|- [Writing functions in R](lectures/lec2/writing_functions_in_R.md)|[Scope](https://leewtai.github.io/courses/stat_computing/lectures/learning_r_debug.html)|[Homework 1](homeworks/hw0.md) Due|
|2021-02-02|- [Data visualization - baseR](https://leewtai.github.io/courses/stat_computing/lectures/learning_r_data_viz.html)|Text 7.1.1 + 7.1*||
|2021-02-04|- [if/else](lectures/learning_r_data_wrangle.md)|||
|2021-02-09|Review session||[Homework 2](homeworks/hw1.md) Due|
|2021-02-11|Take-Home Midterm 1|||
|2021-02-16|[Joins](https://leewtai.github.io/courses/stat_computing/lectures/learning_r_data_wrangle.html)|||
|2021-02-18|[Lists](https://leewtai.github.io/courses/stat_computing/lectures/learning_r_data_wrangle.html)|Text 5||
|2021-02-23|[*apply functions and vectorized calculations](https://leewtai.github.io/courses/stat_computing/lectures/learning_r_summarize.html)||[Homework 3](homeworks/hw3.md)|
|2021-02-25|More practice on data wrangling|||
|2021-03-02|Spring Recess No Class|||
|2021-03-04|Spring Recess No Class|||
|2021-03-09|[Entering tidyverse with Data Visualization ggplot() and `%>%`](https://us.edstem.org/courses/181/lessons/882/slides/4088)<br> ggplot video on [Vimeo](https://vimeo.com/409003549) and [優酷](https://v.youku.com/v_show/id_XNDYzNjk0MDAzNg==.html) <br> `%>%` operator video on [Vimeo](https://vimeo.com/409003734) and [優酷](https://v.youku.com/v_show/id_XNDYzNjkzOTY5Mg==.html)|[Online Tutorials](http://r-statistics.co/Complete-Ggplot2-Tutorial-Part1-With-R-Code.html)|[Homework 4](homeworks/hw4.md)|
|2021-03-11|[Working with text](https://leewtai.github.io/courses/stat_computing/lectures/learning_r_text_manipulation.html)|||
|2021-03-16|[Working with text continued](https://leewtai.github.io/courses/stat_computing/lectures/learning_r_text_manipulation.html)|||
|2021-03-18|[Reading in different types of data](https://us.edstem.org/courses/181/lessons/870/slides/3962) and [lec-vimeo](https://vimeo.com/399962856) or [lec-優酷](https://v.youku.com/v_show/id_XNDYwMTQ5ODUyOA==.html)|||
|2021-03-23|Review session||[Homework 5](homeworks/hw5.md)|
|2021-03-25|Take-Home Midterm 2|||
|2021-03-30|[Scraping](https://leewtai.github.io/courses/stat_computing/lectures/learning_r_scraping_and_api.html) with [vimeo lectures](https://vimeo.com/404714829) and [優酷 lecture](https://v.youku.com/v_show/id_XNDYyMTU3MDg0MA==.html)|||
|2021-04-01|[API Calls](https://leewtai.github.io/courses/stat_computing/lectures/learning_r_scraping_and_api.html) with [vimeo lecture](https://vimeo.com/404715597) and [優酷 lecture](https://v.youku.com/v_show/id_XNDYyMTU3MDQ1Ng==.html)|||
|2021-04-06|Simulations<br> Simulation video on [vimeo](https://vimeo.com/408097921) and [優酷](https://v.youku.com/v_show/id_XNDYzMzk3MzEyNA==.html)|||
|2021-04-08|Permutations<br> Permutation video on [vimeo](https://vimeo.com/408097666) and [優酷](https://v.youku.com/v_show/id_XNDYzMzk3MzM2NA==.html)|||
|2021-04-13|[Debugging in R](https://us.edstem.org/courses/181/lessons/873/slides/4012) with [Vimeo lectures](https://vimeo.com/407632826) and [優酷 lectures](https://v.youku.com/v_show/id_XNDYyMTU3MTE2OA==.html)|||
|2021-04-15|What we don't know||[Homework 6](homeworks/hw6_v2.md)|
|2021-04-20|Take-Home Final Exam|||


### Logistics
Lectures:
  [TuTh 4:10pm - 5:25pm, Zoom Link on Canvas](https://vergil.registrar.columbia.edu/#/courses/APPLIED%20STATISTICAL%20COMPUTING)

Office Hours:
  - Wayne: by appointment via Google Invites
  - Andrew: Tu/Th 1-2pm on [Zoom](https://columbiauniversity.zoom.us/j/98205016672?pwd=NjJ1Y2JaRHRNK2syczg1YjNrNVhnUT09)
  - Navid: W 1:30-3:30pm on [Zoom](https://columbiauniversity.zoom.us/j/4838701880)
      - Navid also has a [sign-up sheet](https://docs.google.com/spreadsheets/d/13a2S-viVBKrtIqSNZAbQRkpc5jxHJUO1SoKPlhHuMHg/edit#gid=0) to avoid overflow.

### Grading
If your final grade is in [93-100], you will earn at least an A, [90-93) will earn at least an A-, [87-90) will earn at least a B+, etc. A grading curves may occur depending on the class performance but I will not curve downwards. I may not give out A+ in this class.

#### - Homeworks (15%)
- Late homeworks will receive 0 credit
- Homework solutions will exist in R
- Your lowest homework grade will be dropped (this is for students who add this course late)
  - No make-up homeworks will be granted even if you registered late to the class
- Please export all homeworks in PDF files following these [instructions](../../setup/math_and_code.md)
  - You should try using Rmarkdown to create your solutions

#### - Exams (80%)
- Midterms (25% each)
- Final (30%)

#### - Participation (5%)
- This will be based on in-class online activities
- You'll need at least 50% here to pass the class
- If you achieve 50% participation, you will receive the full 5% credit

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
