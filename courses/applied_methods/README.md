# Applied Statistical Methods

This is a placeholder page for a survey course on different applied statistical
topics. A survey course is not meant to give you a deep understanding into any
of the topics but to present the challenges that gave rise to the method and

### Course material

Syllabi:
- [3105 Applied Statistical Methods](syllabus.md)

### Pre-requisites
- linear regression
  - the assumptions behind using linear regression for inferring the "true" model (if this
    sentence doesn't make sense, that means you don't have it).
    - how to validate these assumptions
  - interpreting the linear regression coefficients
  - uncertainty of the linear model and the issue of multiple hypothesis testing
  - how to simulate the regression model for data generation
  - How to improve regression
    - creating features (polynomials, interactions, etc)
    - feature selection

### Computer setting up
I encourage you to set up [Jupyter Notebooks on your computer](../../setup/conda_and_navigator_setup.md)
so you could repeat these in R or Python in the future. For Python users, you'll need `numpy` and `statsmodel`.


### Possible topics
- Population and sample collection
  - goals in collecting data
    - measure what you want
    - minimize the uncertainty
  - stratified sampling vs cluster sampling
- Refresher on linear regression
  - Diagnosing regression with real data and improvements
- Bayesian view on linear regression
  - graphical models
- Time series data
  - Kalman filters
  - Contrast with linear regression
- Kriging
  - Estimating unknown surfaces
  - Mining data?
- Causal inference
  - Counter factual and potential outcomes
  - Randomized experiments
  - Propensity scores
  - Synthetic controls
- Survival analysis
  - censor issues
- Causal inference using observational studies
- False Discovery rate
  - Procedure and different question
- Sequential hypothesis testing
