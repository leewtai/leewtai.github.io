# Project 2: Human-in-the-Loop

One type of data mining is to assist people to process through lots of data.
The so called human-in-the-loop process often works by leveraging machine
learning models that help prioritize relevant information and remove unlikely
options. For example, a logistic regression that identifies candidate clothing customers may
like given their age, gender, location, and past selections where a stylist makes
the final choices (e.g. Stitchfix does something like this internally).

The goal of this project is for you to perform data mining on text data through
a human-in-the-loop model.
In particular, you are asked to mine through job descriptions to identify the
top 3 job descriptions with respect to a given resume. The motivating example is to
assist a student through thousands of job descriptions without asking them to read every
single one.

Your goal should be to optimize both alignment with the resume **and** having a good range
of options. For example, if your top 3 recommendations are data analyst from 3 different tech companies,
you may have achieved alignment but missed the objective of diversity.

The data can be found on CourseWorks. This is scraped from [Indeed.com](https://www.indeed.com)
using different job titles but focused in New York and full-time positions.

Your report should include:
- An introduction and conclusion
- Please summarize the data and any data processing you have done before executing your approach.
  - You should comment on the distribution of job descriptions and whether a good fit is even possible.
  - You should call out data quality issues if some may impact your recommendations.
- How you decided to tackle the problem
  - This process should have tested if Term Frequency Inverse Document Frequency (tf-idf) provides
    useful information.
  - Your process is likely a multi-stage process instead of a single model but this can be subjective
  - A peer outside of the class should be able to follow your steps according to these instructions and find recommendations for their resume.
- How you validated the method is providing both **good** and **diverse** recommendations:
  - This should include a formal metric for both "good" and "diverse"
  - You must validate the recommendations given your resume(s) so your report necessarily includes your resume
    - You should include a few intentionally bad and/or good job descriptions and show how your approach
      prioritized or deprioritized these jobs for your resume.
  - You cannot manually go through all descriptions as a validation.
