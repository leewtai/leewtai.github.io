# Statistical Computing and Introduction to Data Science
GR5206 - Fall 2022

## Learning outcomes
- Understand basic programming
  - Manipulate data with different structures
  - Control flow
  - Functions
- Explore data via visualization
- Study statistical concepts via simulations
- Automate tasks with programming
- Understand basic optimization

### Prerequisites
- An introductory statistics class
  - Basic probability distributions (e.g. Gaussian, binomial distributions and their likelihoods)
  - Basic hypothesis testing (e.g. t-test)
  - Summary statistics
  - Histograms, boxplots, etc
- Multivariate calculus
  - Derivatives and functions
- Matrix operations and inverses of matrices
- You should be at least co-enrolled in a modeling class like regression

### Textbooks and references
- Google!
- [Python concept notes](lectures/learning_python_intro.md)
- [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)
- Basics only - [Programming with Python by Software Carpentry](https://swcarpentry.github.io/python-novice-inflammation/)
- [LearningPython.org](https://www.learnpython.org/)
- Data engineering references (not covered in this class):
  - Designing Data-Intensive Applications by Martin Kleppmann (available in NYPL)
  - System Design Interview - An Insider's Guide by Alex Xu


## Timeline
I reserve the right to change the ordering and the content for the course throughout the semester.

|Date|Topic|Reference|Due|
|---|---|---|---|
|2022-09-08|[Introduction + python as a calculator](https://docs.google.com/presentation/d/1hbdEFneIriuFSxtwfH29LvJp1AX_gZ961FtG4msPL7o/edit?usp=sharing)|- [Python concepts 1, 2, 3, 4](lectures/learning_python_intro.md)<br>- [Software Carpentry - Python Fundamentals + Analyzing Patient Data](https://swcarpentry.github.io/python-novice-inflammation/)<br>- [Python Data Science Handbook Chapter 2: Understanding Data Types in Python to The Basics of Numpy Arrays](https://jakevdp.github.io/PythonDataScienceHandbook/)||
|2022-09-15|Numpy, objects, and subsetting<br>[AB Testing](https://docs.google.com/presentation/d/1lRzWdkLiwV0_3zBNKcDF6VqOu6JGpXSCy4WZNXH69NM/edit#slide=id.p)|[Python concepts 5, 6, 8, 10, 11](https://leewtai.github.io/courses/stat_computing/lectures/learning_python_intro.html)|[Set up your jupyter notebook environment with the command line](https://leewtai.github.io/setup/conda_and_navigator_setup.html)|
|2022-09-22|[For-loop, if/else, working with files,<br>AB testing assignment](https://docs.google.com/presentation/d/115mFspST_Id7c0qk1H4R2UAmUOQAp_nZO96KPQbcRyc/edit?usp=sharing)|[Python concepts 7, 9, 21, 23](https://leewtai.github.io/courses/stat_computing/lectures/learning_python_intro.html)|HW1 Due|
|2022-09-29|[Pandas, summaries, and visualization<br>Exploratory data analysis](https://docs.google.com/presentation/d/1qpWNoeyzZnxuKsi4O1v4FJDc6m_V177fIRht_kAhySg/edit?usp=sharing)|[Python concepts 12, 14, 15, 16](https://leewtai.github.io/courses/stat_computing/lectures/learning_python_intro.html)||
|2022-10-06|[Nested data and data wrangling<br>Basic data engineering](https://docs.google.com/presentation/d/1c_hbkqKo-_kqrwFSeuebhyAjaNsKvaCAZCmI3pkI2xc/edit?usp=sharing)|[Python concept 24 and all previous chapters](https://leewtai.github.io/courses/stat_computing/lectures/learning_python_intro.html)|HW2 Due|
|2022-10-13|Regular expression and interacting with APIs|[Python concepts 13, 17](https://leewtai.github.io/courses/stat_computing/lectures/learning_python_intro.html)||
|2022-10-20|Designing data pipelines|All previous Python concepts|HW3 Due|
|2022-10-27|Midterm|||
|2022-11-03|[Data use cases, relational data, and SQL](https://docs.google.com/presentation/d/18RuceAE4_9vM4k7ILTNcpoA2UCarpObwNjdonlgEpjQ/edit?usp=sharing)<br>Data quality concepts and data engineering|[Python concepts 20](https://leewtai.github.io/courses/stat_computing/lectures/learning_python_intro.html)||
|2022-11-10|[Modeling data](https://docs.google.com/presentation/d/1StjjdlxBuHEJidpC3D_NczrsBitZaXmuvIven_xs5c4/edit?usp=sharing)<br>"Data science methods"|[Python concepts 18](https://leewtai.github.io/courses/stat_computing/lectures/learning_python_intro.html)||
|2022-11-17|[Optimization](https://docs.google.com/presentation/d/1zcG_RxtVZMPP-ZjkovMpZwXvI-GKbifcGzuU8vMjU-E/edit?usp=sharing)<br>Objective functions|[Python concepts 19](https://leewtai.github.io/courses/stat_computing/lectures/learning_python_intro.html)|HW4 Due|
|2022-11-24|Thanksgiving NO CLASS|||
|2022-12-01|[Bootstrap, permutation, and other simulations](https://docs.google.com/presentation/d/1NiOdRHs7eeB94F-eS3lxJvqZGsKUll2LWwjw7bf5mqk/edit?usp=sharing)<br>Model evaluation|||
|2022-12-08|[Validation](https://docs.google.com/presentation/d/1OO7WHa8oKpOS0HeTQqeKeWK0MqFlg70d9ytTdTZMm0s/edit?usp=sharing) and [what we don't know](https://docs.google.com/presentation/d/1x_RDVUNHKRA_OH53BqoBpp8QLwQ62WZrk7jnzdBsegE/edit?usp=sharing)||HW5 Due on 5/2|
|TBD|Final|||


## Logistics
Class time: [F 10:10am - 12:40pm, Location: 301 Uris](https://vergil.registrar.columbia.edu/#/courses/STAT%20COMP%20&%20INTRO%20TO%20DATA%20SCI)

### Teaching Team
See Ed for offiec hours

### Grading
If your final grade is in [93-97), you will earn at least an A, [90-93) will earn at least an A-, [87-90) will earn at least a B+, etc. A grading curves may occur depending on the class performance but I will not curve downwards. I will not give out A+ for this class.

#### - Homeworks (25%)
- Late homeworks will receive 0 credit
- No make-up homeworks will be granted even if you registered late to the class
- If you want to learn how to set up Jupyter Notebooks with Python, follow these [instructions](../../setup/conda_and_navigator_setup.md)
- Please read these important things related to [submitting homeworks on Ed](ed_hw_faq.md)

#### - Exams (70%)
- Midterms
- Final

#### - Participation (5%)
- In class participation
- Online question posting (non-private) and answers are all ways to achieve this
- I will reach out after the midterm if you are at risk of missing some points here.

##### Exam accomodations
In order to receive disability-related academic accommodations for this course, students must first be registered with their school Disability Services (DS) office. Detailed information is available online for both the [Columbia](https://health.columbia.edu/content/disability-services) and Barnard registration processes.

Refer to the appropriate website for information regarding deadlines, disability documentation requirements, and [drop-in hours](https://health.columbia.edu/getting-care/drop-offices/disability-services-drop-hours)(Columbia)/[intake session]() (Barnard).

 

For this course, students are not required to have testing forms or accommodation letters signed by faculty. However, students must do the following:

·         The Instructor section of the form has already been completed and does not need to be signed by the professor.

·         The student must complete the Student section of the form and submit the form to Disability Services.

·         Master forms are available in the Disability Services office or online: https://health.columbia.edu/services/testing-accommodations


## Expectations
- Take chances!
  - Break the code in lecture
- Give feedback in office hours or e-mail, don't waste your time if you think a topic is not helpful
- Participate and ask questions, this is not easy!
  - In class: forecast what should be done, compare with what is happening, then summarize the difference.
  - Online: describe what you observe, describe what you expect, communicate clearly.
  - To each other: summarize the conversation to ensure you're listening and think constructively before criticizing.
- Academic honesty: https://www.cs.columbia.edu/education/honesty/

### Acknowledgement
A lot of these materials are based off the materials from Prof Thibault Vatter and Prof Gabriel Young.
