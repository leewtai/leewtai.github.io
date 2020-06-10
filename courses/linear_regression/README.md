# Linear Regression

Linear regression is the first class where **data** meets **statistics** meets **programming**.

But more importantly, many confuse the concept of regression as a method of finding the best line
with regression as a way data is generated. Why this differentiation matters goes beyond regression
and highlights the care required when people are performing data analyses. The lessons here
will explain why statistics is so critical in all applied sciences that use data.

I will review some of these topics but I'm assuming:
- You have some basic exposure to programming
  - Plotted a scatter plot, ran a for-loop, create 
- You have exposure to an introductory statistics class before
  - Average, median, hypothesis testing, correlation, what is a random variables etc

At the end of this you should feel comfortable to
- Understand how regression is used in different problems, how to diagnose it,
  and its various challenges.
- Understand how estimation using observed data depends on assumptions from the data generation process
- Understand the need to formalize a problem via mathematics, simulating the mathematics via programming,
  and using the simulation to validate the mathematics.
- Understand multiple-comparison as a challenge


#### Computer setting up
I encourage you to set up [Jupyter Notebooks on your computer](../../../setup/conda_and_navigator_setup.md)
so you could learn R, Python, or Julia in the future.

#### Lessons
- Using math to formalize an abstract concept
  - regression as a candidate "best-fit" line
  - introducing the least squares objective function
  - re-learning the average as a special case of regression
- Solving for the best-fit line
  - numerical vs analytical solutions to regression
- Tying statistics to programming by simulating results from introductory statistics
  - review on confidence interval
  - validating mathematical derivations using programming
- Simulating data from a linear model
  - Graphical model of `X -> Y` and examples of non-linear models
  - Additive errors
- Why regression?
  - Estimation
  - Different best-fit lines on regression data
  - Similar results for the average extend to regression coefficients
- Vocabulary around the regression line
  - independent variable, X, covariates, features, predictors
  - dependent variable, Y, ...
- Tying artifacts from regression line to problems
  - Inference/prediction
- Interpretations of standard output from regression libraries
- Assumptions on regression data vs properties of the regression line
  - Trade-offs
  - bootstrap samples vs bootstrapping residuals
- Validating regression
  - Goodness of fit: r^2
  - Residual plots and assumption violations
- Binary outcome violates the regression data assumption
  - likelihood methods
  - logistic regression
  - connection between Gaussian likelihood and least squares
- Multivariate regression
  - matrix view of regression
  - candidate variables: interactions, polynomials
- Linear algebra view of regression
  - projection
  - additional variables
- Multiple-comparison
  - Bonferroni correction on t-tests
  - F-test
- Connection to ANOVA
- Gauss-Markov theorem vs James-Stein estimator
  - Would throwing out data help?
  - Which is better? truth vs the fitted values
- More features always better in regression?
  - mean squared error on new data points
  - Cross validation
  - bias variance trade-off
  - Collinearity
- Wrong models
  - omitted variables
  - confounders
- Different data generation
  - DAGs
- Instrumental variables
- Basic feature selection
- PCA regression
- Lasso/Ridge regression


## Past materials
I have some old materials online:
[syllabus for concentration](minor_syllabus.md)

[syllabus for major](major_syllabus.md)



