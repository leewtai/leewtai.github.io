# Final Project - Applied Linear Regression 2022 Fall

Due 12/16/2022.

The goal of the final project is to demonstrate your learnings from Applied Linear Regression and
connect those learnings to potential future projects that benefit your career. You may request to
substitute your final project with your own proposal as long as it achieves similar objectives.

Final deliverable:

- A written report (pdf on CourseWorks) and code (in R or Python on [GitHub](https://github.com) in a public repository)
- The report should **attempt** to reproduce and evaluate an academic article that is
  - Published in a reviewed journal no earlier than 2016
  - May be published and is under the supervision of a faculty member at Columbia Univ (this includes honor theses)
- The article must have real data that is not based on a simulation
  - Exceptions can be made for emulators in a scientific discipline.
- You are encouraged to overlap this final project with your efforts outside of this course (e.g. other courses,
  work, hobby) with the exception of an interview.
- You must complete your own project.
- You are discouraged from starting a new project from scratch.


## Required sections for the project

The sections below can be rearranged or merged, the key is that the relevant ideas are
covered.

- A paper summary that discusses
  - the research goal of the paper
  - introduce the data used
  - the model used and how it relates to the question
  - the conclusions from the paper and the key results that motivate the conclusion
- An introducion for your report that covers
  - what result your paper will focus on and **attempt** to reproduce.   
  - the type of evaluations you tried, the summary of the results, and its implication on
    the paper (see details below)
- A description about the data that is used
  - Your should include at least one visual that introduces the key variables to a novice
  - What you believe the ideal dataset would be
  - Contrasting your ideal with the dataset and its implication on the research question
- Reproducing the results
  - You may focus on reproducing a single key result from the paper
  - You should justify why you chose the particular result
  - This result should relate to a model. A model is likely field specific, and you should articulate this
    for a novice to your field and in a quantitative format (enough details to simulate this).
  - If you are reproducing a non-numeric result, you must have a quantitative assessment for whether you reproduced the result.
  - If you cannot reproduce the result, you should discuss why the difference may exist
    (parameter fitting, data quality, package version for the model, lack of access to data processing, etc)
    - If the paper is too advanced given the limits of regression but is a topic you plan on learning next semester, you may
      state so then use regression as a "closest approximation" to the model used in the paper. If you do this, come to office hours
      to get pre-approved for your problem.
- Evaluating the result by doing two or more major categories from below
  - Testing the result's sensitivity to data, e.g.
    - Removing a small fraction of points (ideally not in a random fashion)
    - Adding or removing features
    - Sensible transformations to the data
  - Testing the sensitivity to model choice, e.g.
    - Replacing the proposed model with a different model (e.g. time series with just regression)
    - Changing hyper-parameters
    - Adding or removing features. This should not be the same as the data features above but features
      that change the model.
  - Creating a simulation to verify that the approach/model has desirable properties in the context of the problem, e.g.
    - reasonable statistical power with the given sample size, feature size, and minimum detectable effect
    - unbiasedness in the parameter of interest
    - is more robust to outliers than past models
    - etc ...
  - Testing a particular assumption mentioned in the paper or required by the model that isn't explicitly verified in the paper.
  - Changing the evaluation criteria for the result
  - Improving the model based on any of the tests above
- Your evaluation above should have at least one visual
- Your evaluation needs to be summarized and its implication on the model/problem need to be articulated
- Some conclusion
