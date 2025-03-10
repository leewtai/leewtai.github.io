# Statistical Computing and Introduction to Data Science
GR5206 / 4206 - Fall 2024

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
- AI tools like ChatGPT are generally **NOT allowed** unless explicitly allowed for the assignment. You are strongly discouraged from using them for intro courses which this course is. If you cannot resist the temptation though, it is best that you prompt ChatGPT to ask you questions rather than having it provide you with solutions. You are still responsible for the correctness of your work. Here’s an example prompt you could try:
  ```
  You are a college instructor helping students to learn Python fundamentals. You should not give the solution to students but help clarify and guide their thinking by asking questions back or providing counter examples. 

  Here are 2 examples: 
  Question: 
  """
  create a simulation that demonstrates the sample average is unbiased for estimating the population mean. 
  """
  Your answer: 
  """
  What does unbiased mean? Let's write the code that will draw a sample first. 
  """
  
  Question: 
  """
  Where is my bug?
  y = x.shuffle()
  sum(y)
  TypeError: 'NoneType' object is not iterable
  """
  Your answer:
  """
  What do you think the type of `y` is?
  """
  ```




## Timeline
I reserve the right to change the ordering and the content for the course throughout the semester.

|Date|Topic|Reference|Due|
|---|---|---|---|
|2024-09-06|[Introduction + python as a calculator](https://docs.google.com/presentation/d/1hbdEFneIriuFSxtwfH29LvJp1AX_gZ961FtG4msPL7o/edit?usp=sharing)|- [Python concepts 1, 2, 3, 4](lectures/learning_python_intro.md)<br>- [Software Carpentry - Python Fundamentals + Analyzing Patient Data](https://swcarpentry.github.io/python-novice-inflammation/)<br>- [Python Data Science Handbook Chapter 2: Understanding Data Types in Python to The Basics of Numpy Arrays](https://jakevdp.github.io/PythonDataScienceHandbook/)||
|2024-09-13|Numpy, objects, and subsetting<br>[AB Testing](https://docs.google.com/presentation/d/1lRzWdkLiwV0_3zBNKcDF6VqOu6JGpXSCy4WZNXH69NM/edit#slide=id.p)|[Python concepts 5, 6, 8, 10, 11](https://leewtai.github.io/courses/stat_computing/lectures/learning_python_intro.html)|[Set up your jupyter notebook environment with the command line](https://leewtai.github.io/setup/conda_and_navigator_setup.html)|
|2024-09-20|[For-loop, if/else, working with files,<br>AB testing assignment](https://docs.google.com/presentation/d/115mFspST_Id7c0qk1H4R2UAmUOQAp_nZO96KPQbcRyc/edit?usp=sharing)|[Python concepts 7, 9, 21, 23](https://leewtai.github.io/courses/stat_computing/lectures/learning_python_intro.html)|HW1 Due|
|2024-09-27|[Pandas, summaries, and visualization<br>Exploratory data analysis](https://docs.google.com/presentation/d/1qpWNoeyzZnxuKsi4O1v4FJDc6m_V177fIRht_kAhySg/edit?usp=sharing)|[Python concepts 12, 14, 15, 16](https://leewtai.github.io/courses/stat_computing/lectures/learning_python_intro.html)||
|2024-10-04|[Nested data and data wrangling<br>Basic data engineering](https://docs.google.com/presentation/d/1c_hbkqKo-_kqrwFSeuebhyAjaNsKvaCAZCmI3pkI2xc/edit?usp=sharing)|[Python concept 24 and all previous chapters](https://leewtai.github.io/courses/stat_computing/lectures/learning_python_intro.html)|HW2 Due|
|2024-10-11|Regular expression and interacting with APIs|[Python concepts 13, 17](https://leewtai.github.io/courses/stat_computing/lectures/learning_python_intro.html)||
|2024-10-18|Designing data pipelines|All previous Python concepts|HW3 Due|
|2024-10-25|Midterm in the evening!|||
|2024-11-01|[Data use cases, relational data, and SQL](https://docs.google.com/presentation/d/18RuceAE4_9vM4k7ILTNcpoA2UCarpObwNjdonlgEpjQ/edit?usp=sharing)<br>Data quality concepts and data engineering|[Python concepts 20](https://leewtai.github.io/courses/stat_computing/lectures/learning_python_intro.html)||
|2024-11-08|[Modeling data](https://docs.google.com/presentation/d/1StjjdlxBuHEJidpC3D_NczrsBitZaXmuvIven_xs5c4/edit?usp=sharing)<br>"Data science methods"|[Python concepts 18](https://leewtai.github.io/courses/stat_computing/lectures/learning_python_intro.html)||
|2024-11-15|[Optimization](https://docs.google.com/presentation/d/1zcG_RxtVZMPP-ZjkovMpZwXvI-GKbifcGzuU8vMjU-E/edit?usp=sharing)<br>Objective functions|[Python concepts 19](https://leewtai.github.io/courses/stat_computing/lectures/learning_python_intro.html)|HW4 Due|
|2024-11-22|[Bootstrap, permutation, and other simulations](https://docs.google.com/presentation/d/1NiOdRHs7eeB94F-eS3lxJvqZGsKUll2LWwjw7bf5mqk/edit?usp=sharing)<br>Model evaluation<br>[Validation](https://docs.google.com/presentation/d/1OO7WHa8oKpOS0HeTQqeKeWK0MqFlg70d9ytTdTZMm0s/edit?usp=sharing) and [what we don't know](https://docs.google.com/presentation/d/1x_RDVUNHKRA_OH53BqoBpp8QLwQ62WZrk7jnzdBsegE/edit?usp=sharing)|||
|2024-11-29|Thanksgiving NO CLASS|||
|2024-12-06|Big exam||HW5 Due on 12/1|
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
- If you want to learn how to use Google Colab, follow these [instructions](../../setup/colab.md)
- Please read these important things related to [submitting homeworks on Ed](ed_hw_faq.md)

#### - Exams (70%)
- 2 weighing schemes
  - Midterm (30%) Final (40%)
  - Midterm (15%) Final (55%)
You will receive a letter grade from curving each approach and receive the higher letter grade between the 2 approaches.

#### - Participation (5%)
- In class participation
- Online question posting (non-private) and answers are all ways to achieve this
- I will reach out after the midterm if you are at risk of missing some points here.
- You can miss one of these for free.

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
