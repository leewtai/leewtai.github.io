# Homework 5: issues with more features in regression

#### Q0 - Multiple Hypothesis Testing
We've shown that multiple hypothesis testing is an issue when we are testing multiple features (i.e. multiple $$\hat{\beta}_i$$.
Turns out it appears when we're inferring for the true line at multiple points as well. Please generate the following data

```r
n <- 50
beta0 <- -5
beta1 <- 1.2
max_x <- 10
x <- runif(n, 1, max_x)
y <- beta0 + beta1 * x + rnorm(n)
x_new <- seq(1, max_x, length.out=20)
```

- If we use the `90%` confidence intervals from `predict.lm()` to infer the true line at each of the values in `x_new`, what percentage of the confidence intervals contain the true line? Please write the code that will compute this percentage. (side comment: each of these confidence intervals are also called "point-wise confidence intervals" instead of a "joint confidence interval")
- Keep your `x_new` and `x` values fixed, please perform `B=1000` simulations that generate new realizations of `y` under the true model.  Please calculate the fraction of simulations where the `90%` confidence intervals contains the true line across all values of `x_new`.  (Side comment: the collective interval can be considered an "confidence envelope" that tries to contain the true line at all points. I recommend plotting the true line vs the interval for a case that has less than `100%` coverage if you're having a hard time visualizing this). 
- Please use Bonferroni's correction (as we did for the coefficients) to make the answer from above be `90%` across the 20 different `x_new` values, how would you change the code above in `predict.lm()` to achieve this?
- TRUE/FALSE, is it possible for the confidence intervals at `c(1, max_x)` (i.e. the 2 most extreme `x_new` values) to contain the true values, yet the confidence intervals in between to not contain the true line? No need for explanation (Hint: I do recommend you to leverage your simulation).

#### Q1 - practice with real data

In CourseWorks you'll find a file called `global_pref_survey_individual.csv`.
This is the individual survey data referenced in our reading [Global Evidence on Economic Preferences](https://academic.oup.com/qje/article/133/4/1645/5025666).
Before you start, make sure your R's major version is at least 4.0 (you can check via `R.version`).

Please answer the following using this dataset:

- How many records are in the dataset?
- What is the highest percentage of missing value across all columns in the dataset? Which column is this?
- What percent of data is `NA` after reading in the data for the column `date`?
  What time range does the dataset cover? (side note: the important message is that `is.na()`
  doesn't always catch everything)
- Please answer and show your code that verifies whether `country` and `isocode` and `iso` are redundant.
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


#### Q2 - Final project question

- Please link to a paper that you may be exploring for your final project and answer the following questions
  - What is the research question of the paper (2 sentences at most)
  - What would an ideal dataset be in your opinion?
  - Contrast your ideal dataset with the dataset used in the paper and compare these two.

{% include lib/mathjax.html %}
