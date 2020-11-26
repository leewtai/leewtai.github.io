Homework 6: More challenges with Multivariate Regression

#### Q0 - Collinearity and Cross validation
On Canvas, there's a file named `processed_payroll_2019_first_5000.csv` that was originally from 
https://data.cityofnewyork.us/City-Government/Citywide-Payroll-Data-Fiscal-Year-/k397-673e

We will explore the behavior of regression with collinearity through this example.
Our main variable of interest is the total pay for each individual and we will learn its relationship with
all the other features.

### Q1 - explore the data
- Please keep only the records that correspond to people who are "ACTIVE" on July 31, 2019.
- Calculate the total pay as the sum of the gross pay, overtime (ot) pay, and other pay.
- Between the total pay, the $$\log(total\ pay + 1)$$, and $$\sqrt(total\ pay)$$, which one follows the Normal distribution the most? Please show the evidence that supports your claim.
- How many agencies are in our data? (We only grabbed the first 50000 records from NYC OpenData)
- How many boroughs of NYC are in the dataset?
- How many genders (derived from the first name) are in the dataset?
- How many values are there for rare titles? (This is defined as "within our dataset, that title has appeared less than 50 times")
- Please calculate the tenure for each person by calculating the days between their start date in that agency relative to 2020 Jan 1st then plot the distribution of the tenure. If your time zones are off, ignore that. Hint: 
  ```r
  strptime("2018-08-13T00:00:00.000", "%Y-%m-%dT%H:%M:%S.000")
  ```

#### Q2 - fitting an OLS with collinear features
- Please regress the $$\sqrt{total\ pay}$$ against tenure, gender, rarity of title, regular hours, overtime hours, and borough. Please make sure you fit the intercept! Please show the `summary.lm()` output. (side comment: you should know why we did not add "agency" as a feature)
- What is the $$r^2$$ of the fitted OLS model here?
- Please plot the residual plot of the OLS (do not bother making it pretty)
- Are any assumptions from our usual linear regression model violated? Please justify your answer according to what you perceive from the residual plot? (this will be generously graded!)
- According to what features were dropped by R, which set of features were "collinear" with one another?
- The "baseline group" is the group identified when all of the "membership" features used in the regression are set to 0. For example, if I regress income on urban/rural/suburban as a feature along with an intercept, and my OLS coefficients are for rural and suburban, then my baseline group would be urban. Please describe the "baseline group" according to the values that were dropped from the collinear features in our model.
- What is your prediction for someone's total pay (not square rooted) if they are in the baseline group and their other features are at the average level of the entire dataset (e.g. their regular hours are the same as the average regular hours of the entire dataset)?


#### Q3 - Cross validation
Hopefully you're questioning why we bothered with square rooting the total pay? We will use cross validation to make this argument.

We have 2 competing models:
- Model1: Fit an OLS using $$\sqrt{total\ pay}$$ as the dependent variable, then predict new data points using $$\hat{Y}^2_{ols1}$$
- Model2: Fit an OLS using $$total\ pay$$ as the dependent variable, then predict new data points using $$\hat{Y}_{ols2}$$ directly

Side comment: I highly encourage you to try to make an intuitive argument for BOTH models before doing the analysis.

Main question: please do a 10 fold cross validation (notice doing Jackknife should feel a bit intimidating for most laptops) to see which method of prediction has a lower mean absolute prediction error.

Some specifications:
- Please use the same features as we did from above
- Do not worry about making the size of the different cross validation groups the same (random sample is sufficient)
- From your 10 different folds, you should have 10 different errors from each model, please VISUALIZE the performance using these 20 values (there are many answers here) that clearly show the difference or non-difference between the 2 models.
- Please articulate, based on the visualization above, which model is better.
- Does the answer change if we switch the definition to the mean squared prediction error?

Side comment: Why do you think this is?

\end{document}
