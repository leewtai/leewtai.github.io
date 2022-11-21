# Homework 6: Progress with the final project

#### Q0 - Exploring the data

Your dataset is likely related to some population, please visualize some summary
statistics that can inform you of the potential biases in your data. For example,
if gender is a feature, we should visualize the distribution of gender given different
levels of the outcome variable or main feature. You should visualize two or more
variables for this question.
- If your data only consists time series of a single variable. You should be able
  to visualize the relationship between the series and different "lags" of the series.
  This will be considered a different variable.
- If your data does not have a population (e.g. case studies), you should be able
  to visualize the the distribution of data across different parameter settings.

In addition to your visualization, please also include:
- An articulation of your expectation and why you chose the particular visualization.
- Did the visualization make you have more or less faith in its ability to answer the research question at hand?

If you are still in the process of procuring the data (you should hurry),
you should focus on articulating your expectations according to your ideal dataset
(but notice that you're forced to talk about expectations between at least 2
variables now). In addition, you should try to find any data (regardless of quality)
online that contains one or two of your variables and plot the data there to prepare
yourself for possible data issues.


#### Q1 - Talking about the model

What model is your paper using? Specifically please answer:
- Is the main model a linear regression model (or logistic/probit regression)?
  - If no, please articulate what this model 'models' that regression does not? Including a wikipedia page or a reference that you're using to understand this model.
  - What is the objective function you believe is being used to fit the data to the model?
- What aspect of the model is being used to answer the research question? e.g. interpreting
  parameters, contrasting predicted values, generalizing on a new dataset, etc


#### Q2 - Model validation

How is the model validated in the paper? Note that even calculating a sample mean requires assumptions on proper random sampling. Validation strategies include comparisons to previous models, comments on the residuals, consistency with qualitative data points, plotting the model output against the data used to train the data, generalizing the data to new datasets, etc

This does not need to be exhaustive on the homework but you should be able to list at least 1 way the model is validated.


#### Q3 - Planning to perturb the model

If your paper already perturbs the model then please state the perturbations (sometimes called "robustness checks") done in the paper and the reasons the authors decided to show those in the paper.
If not, please state the perturbations you have in mind at the moment and why you decided to perform these perturbations given what you read in the paper and examining the data? See the final project description for possible reasons.
