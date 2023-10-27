# Homework 5: More challenges with Multivariate Regression

#### Q0 - Collinearity and Cross validation
On Ed Resources, there's a file named `processed_nyc_payroll_2022.csv` that was originally from 
[NYCOpen Data](https://data.cityofnewyork.us/City-Government/Citywide-Payroll-Data-Fiscal-Year-/k397-673e)

We will explore the behavior of regression with collinearity through this example.
Our main variable of interest is the total pay for each individual and we will learn its relationship with
all the other features.

### Q1 - explore the data
- Please keep only the records that correspond to people who are "ACTIVE" on July 31, 2022 (read the column names!).
- Calculate the total pay as the sum of the gross pay, overtime (ot) pay, and other pay.
- Between the total pay, the $$\log(total\ pay + 1)$$, and $$\sqrt{total\ pay}$$, which one follows the Normal distribution the most? Please show the evidence that supports your claim.
- How many different job titles are in our data (do not bother standardizing them)?
- How many boroughs of NYC are in the dataset?
- How many genders (derived from the first name) are in the dataset?
- How many values are there for rare titles? (This is defined as "within our dataset, that title has appeared less than 50 times")

#### Q2 - fitting an OLS with collinear features

Continuing from Q1

- Please regress the $$\sqrt{total\ pay}$$ against tenure, gender, whether the title was rare, regular hours, overtime hours, and borough. Please make sure you fit the intercept! Please show the `summary.lm()` output. (side comment: you should know why we did not add work title as a feature)
- What is the $$r^2$$ of the fitted OLS model here?
- Please plot the residual plot of the OLS (do not bother making it pretty)
- Are any assumptions from our usual linear regression model violated? Please justify your answer according to what you perceive from the residual plot? (this will be generously graded!)
- According to what features were dropped by R, which set of features were "perfectly collinear" with one another?
- The "baseline group" is the group identified when all of the "membership" features used in the regression are set to 0. For example, if I regress income on urban/rural/suburban as a feature along with an intercept, and my OLS coefficients are for rural and suburban, then my baseline group would be urban. Please describe the "baseline group" according to the values that were dropped from the collinear features in our model.
- What is your prediction for someone's total pay (not square rooted) if they are in the baseline group and their other features are at the average level of the entire dataset (e.g. their regular hours are the same as the average regular hours of the entire dataset)?
- What is the expected change in total pay if a police officer moved their work location from Manhattan to Bronx if the model is correct.
- What is the expected change in total cost for NYC, assuming we believe the model, if we did not allow people to do overtime.

Side comment: the model is bad, don't trust the results. A lot would need to go into understanding these posted payroll values.


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


#### Q4 - Global preferences

On Ed Resources, you'll find a file called `global_pref_survey_individual.csv`.
This is the individual survey data referenced in our reading [Global Evidence on Economic Preferences](https://academic.oup.com/qje/article/133/4/1645/5025666).
Before you start, make sure your R's major version is at least 4.0 (you can check via `R.version`). If not, it's recommended that you update R. The biggest difference is whether character columns are read in as factors or characters.

Please answer the following using this dataset:

- How many records are in the dataset?
- What is the highest percentage of missing value across all columns in the dataset? Which column is this?
- What percent of data is `NA` after reading in the data for the column `date`?
  What time range does the dataset cover? (side note: the important message is that `is.na()`
  doesn't always catch everything)
- Please answer and show your code that verifies whether `country` and `isocode` and `ison` are redundant.
- Why do we avoid having redundant features in modeling? (4 sentences max)
- What is the mean and sd of all the possible response variables?
- To "attempt" to reproduce the OLS coefficients on Table V for patience without region FE (FE = Fixed Effects),
  please run the regression of patience against the listed variables after doing the following manipulations (we will call this regression model `mod`):
  - Change age values that are 99 and above to something reasonable
  - Make sure the country variable is a factor, not a character (make sure this is the last variable you add when calling `lm()`)
  - Create a new column called `age2` from squaring the `age` column
  - You will need to multiply the age column by a constant, figure this out after you examine the first run of regression coefficients (this is mentioned somewhere in the paper as well)
- How did the table end up with 78501 records for this regression? Please write the code that counts the number of records that do not have `NA` in the variables used in the regression above (rather than letting `lm()` handle this for you) and see how many samples you end up with.
- Continuing with the same regression, the wording below Table V claims the values in the parentases are standard errors. Compare these to the standard errors from your run. Do you believe the values are SE for the coefficients? (You'll likely have one number off)
- What changes to the OLS estimates and $$R^2$$ values if we remove the `age2` variable? Let's call this model `mod_sans_age2`. 
- Plot `patience` against `age2` and compare this to the scatter plot of residuals from `mod_sans_age2` against `age2`. HINT: check the length of the residuals before you plot. Make sure your graph handles the issue with too many overlapping points masking the relationship.
  NOTE: the key from this and the above question is that it's not obvious why `age2` was added except its impact on interpreting `age`
- Does removing the signal modeled from the independent variables always reduce the variability in our dependent variable? Please answer this after completing the following:
  - What is the range of the residuals from `mod_sans_age2` and the range of `patience` in our data
  - What is the standard deviation of these values?
- Back to using `mod`, plot the residuals vs the fitted values, i.e. $$\hat{Y}$$, and calculate the correlation between the two.
  - Which assumptions of our regression do you believe is violated vs not? (graded on consistent message)
- Please randomly choose 10% of the data for testing and 90% for training, i.e. train `mod` using only 90% of the records then see its prediction error on the records in the 10% test set. Please choose and calculate a sensible measure to summarize "prediction error" that behaves acts like an objective function for choosing good models. Prediction error is defined as $$Y - \hat{Y}$$.
- Using the same test/train split and prediction error metric above. Articulate the impact of adding a feature called `subj_math_skills2` on `mod` where `subj_math_skills2` is simply squaring the `subj_math_skills` column.
- Contrast this impact to adding a feature called `rand_math` to `mod` where `rand_math` is a shuffled/permuted version of `subj_math_skills`. Please repeat the generation of `rand_math` 100 times and summarize the impact.
  NOTE: please notice that your $$R^2$$ should have only gone up from adding `rand_math`


{% include lib/mathjax.html %}
