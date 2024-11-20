# Homework5 - Visualizing for Validation

### Goals
The purpose of this homework is to give you a sense of "validating" models.

#### Question 1: Final project validation.
Please visualize the data **with** your model. The previous homework was only related to visualizing the data itself.
If you visualized your model with your data already, you should avoid to use the same graphic.
The motivating example here is that "a peer unfamiliar with your project" will rarely believe your
model/analysis is "reasonable" unless you can visually show how your model and data relate to one another.
Please make sure your model and data are clearly labeled and that you include a caption for the graph.

You do not need to explain your model for this assignment.

For example:
- if you have a regression, you could plot the fitted values against the data points.
- if you have a logistic regression, you could plot boxplots for the fitted probabilities for the positive vs negative cases.
- if you have a cluster, you could show the data by coloring the different groups differently.
- if you ran a simulation, what is the true underlying process vs the simulated realizations.
- if you are testing a hypothesis, you could plot the test statistic vs the test statistic under the null distribution.

Thought for curious students: how would your model behave if your data was perturbed, contaminated, or stripped of a feature?


#### Question 2: Talk to a peer about your final project

There's no deliverable here but these are questions I encourage you to talk to a peer about (because I would likely ask these):
- Why would someone be interested in this topic?
- What is the ideal approach you would have taken to tackle this approach if you were not limited by time?
- What model are you using?
- Is your model wrong, why do you think it's still okay?

#### Question 3: 

In class we showed how "right censoring" affects us.
Please create a simulation that shows how left censoring, e.g. we know when people die from cancer but don't know when their cancer started, impact the following:
- The estimation of the survival curve, i.e. P(T > t)
- Our ability to detect the effect of a new drug (e.g. that prolong survival)
- The ability to estimate the parameter in the Cox Proportional Hazard model (coxph() in R) 

You should choose how the censoring happens (this impacts your answer above).

