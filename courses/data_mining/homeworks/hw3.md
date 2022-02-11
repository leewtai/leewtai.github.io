# HW3 - Comparing different models

This homework is to meant for you practice with different regression models on the same dataset.

Context: Finding jobs is difficult. Job descriptions tell us what companies are looking for
so we should be able to detect some signal from job descriptions whether we're prepared enough
for industry. However, there are too many job descriptions to look through.

Please download the dataset, `job_descrip.csv`, from CourseWorks.
- This dataset has the "word counts" from a non-random sample of job descriptions from indeed (2021 and before).
  - The column names are the "words" from the job description and the elements are the absolute count of those
    words in the job description.
  - Some words have been filtered out if it is either too frequent (not discriminative enough for different titles)
    or too rare (indiffertiable from noise).
  - Each row corresponds to a different job description
- There's a column called `job_title` that has the job title used to search for these job descriptions.
- There are "ads" on indeed's website so some job descriptions are not real.

## Q1. Exploratory Data Analysis (EDA)

Please answer the following:
- How many job titles are there?
- What is the least popular and most popular job title?
- How many columns do we have?
- What is the percentage of 0's in our word counts, across all of the words and jobs in our data?
- For each word, compute the number of 0's. Now plot this histogram.
- What is the longest and shortest word in our job descriptions? If there are ties, just pick 5 random ones (in each category) to show.
  This is to gain an understanding of the data quality.
- For the most popular word, i.e. word appeared in most job descriptions, plot the histogram of its word counts across the different job descriptions. If there is a tie, just pick one of them randomly.
- Please describe on the distribution that you see (this should be one sentence only).

## Q2. Basic model setup

For the rest of the homework, we will set our response variable as any job title that has the word 'analyst' in it.

- What percentage of job titles have the word "analyst" in it?
- Please report all words that begins with "analy" in our word frequency matrix, then remove them from our word frequency matrix. This will be our feature matrix `X`.
- Please create another feature matrix called `X2 = log(X + 1)`
  - Why would the `log()` make sense and why do we add 1? (one sentence each or combine both answers into one sentence)
- Why can't we fit OLS to this current setup?
- Please isolate 100 records from the data to serve as a test set.
  - Please make sure your code will have the expected amount of "analyst" positions in this test set (hint: stratified sampling).
- Please calculate the classification error, precision, and recall if we predicted randomly (but proportional to the frequency of "analyst" positions in our dataset).

## Q3. Fitting PCA + OLS

- Please apply PCA to `X2` and plot the ratio of cumulative `sdev^2` over the total `sdev^2`. Please make a decision how to set `center` and `scale` for our call to `prcomp()`.
  - FYI, `sdev` is the singular value and `sdev^2` is called the eigen value.
- Between eyeballing for a `k` value as we did in class vs choosing the smallest `k` such that our ratio above is greater than 0.9, which approach do you recomend choosing given the plot above?
- Please fit OLS using your PCA output and your recommended `k` value.
- Please sort the features according to the p-values you observe. Hint: `lm_summary <- summary(my_ols)$coefficients` 
  - Please report the top words associated with the top 3 features using the "rotation" matrix from your PCA. Please explain whether these features make sense or not given our problem.
- Please round your predictions to make a prediction on the test set. Please calculate your classification error, precision, and recall.
- Please comment on whether you believe the OLS is similar to fitting to random noise or it seems to detect a signal between our "W" and Y.

## Q4. Fitting LASSO

- Please fit the LASSO to our `Y` and `X2` (using the `glmnet` package) and show the change in cross validation error given different regularization parameters (i.e. `lambda`). Make sure you test a wide enough range of `lambda` values that a "dip" appears.
  - Should we normalize our data first?
- What percentage of coefficients were set to 0 in the model corresponding to the `lambda.1se`?
- What are the 50 most influencial words (if there are 50 or more non-0 coefficients) in this case?
- Please round your predictions to make a prediction on the test set. Please calculate your classification error, precision, and recall.

## Q5. Fitting Naive Bayes
- Please fit the Naive Bayes model using both X and X2. For both cases, please use cross validation (with at least 10 folds) to determine
  an optimal cutoff for prediction rather than using "rounding" as we had from before. You will need to choose one metric when doing this cross validation.
- Please calculate your 2 sets of classification errors, precisions, and recalls on the test set using the respective optimal cutoffs.

## Q6. Back to OLS

- Use all top words we've discovered in LASSO and filter a new `X3` matrix. Use this matrix to run OLS and make predictions as we did for LASSO on the test set. Reporting the same set of metrics on the test set.
- Use `X3` to run Logistic Regression as well. Report the same set of metrics on the test set.

## Q7. Some questions

- Across all models, are the top words what you expected? Elaborate with a couple sentences.
- Visualize the evaluation metrics we have for all models and label the graph.
- Based on the graph(s), do you think there's an optimal model or are they all comparable?
- If we can get top words from the model, why do we care about the evaluation metrics.


## Q8. Thinking about Final Project

Please write a paragraph abou what you will do for your final project and where you "might" find data for this. You may need to start collecting data early if you need to scrape data on a routine.

