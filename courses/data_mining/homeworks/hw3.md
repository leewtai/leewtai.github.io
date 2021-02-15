# HW3 - Comparing different models

This homework is to meant for you practice some feature engineering with the
different regression models.

Context: the US is increasingly polarized and [Twitter](https://twitter.com/home), a social
media platform, is providing the space for people to voice their opinions or find like-minded
individuals. In this assignment, we will use Twitter data `non_retweets_dc_inaug_steal.csv` on CourseWorks
that has contains the token frequencies. This has been processed somewhat to minimize the data size. 
The non-token variables are `created_at`, `like_count`, `reply_count`, `retweet_count`, `tweet_body`.

Please **re-download** this dataset given there were issues with the version given in class.

The tweets are collected overtime with the query words "steal", "inaguration", and "washington dc" using
Twitter's [Recent Search API](https://developer.twitter.com/en/docs/twitter-api/tweets/search/api-reference/get-tweets-search-recent).
Calls were made once a day around midnight and there is a limit on the number of queries that
can be made freely.

## Question 0
What dates do the tweets cover? Please visualize the temporal distribution of the tweets
with the intent to understand where most Tweets in the dataset came from in time.

## Question 1
Please combine all the token frequencies that contain the string `inaug` into a single column.
You should remove the redundant tokens after this summarization. Please select the method
of "combining" that is consistent with the "token frequency" concept.

Please report the fraction of records that have non-zero frequencies for this new column.

## Question 2
We want to discover the topics correlated with the inauguration over time. To achieve this,
please model your new column from Question 1 against all other tokens (i.e. exclude the non-token variables)
using the following models. This is **time-consuming**! You should use `Sys.time()` to have a realistic expectation of how long each model will take.

Please plot the MSE from a 5-fold cross validation to compare the prediction accuracy between
- OLS
  - Please ignore the rank deficient warning, this is a warning of high-collinearity
    that is common with high dimensional data and why OLS shouldn't do well.
- stepwise regression using AIC as the objective
  ```r
  ols = lm(y ~ ., df)
  ols_summ = summary(ols)$coefficients
  okay_features = rownames(ols_summ)[ols_summ[, 4] < 0.05]
  init_formula = paste('y ~', paste(okay_features, collapse='+'))
  init_mod = lm(init_fomrula, df)
  # "~." sets the upper model for the `scope` as using all of the features
  step_mod <- step(init_mod, "~.")
  ```
- Lasso corresponding to $$\lambda$$=`lambda.min` from cv.glmnet
  - hint: [predict.cv.glmnet](https://www.rdocumentation.org/packages/glmnet/versions/4.1/topics/predict.cv.glmnet)
  - hint: you may want to convert the training X matrix into sparse matrices, i.e. `Matrix(as.matrix(df_sans_y), sparse=TRUE)`
    to speed things up. This essentially avoids many multiplications when a 0 is involved.
- Ridge regression corresponding to $$\lambda$$=`lambda.min` from cv.glmnet

Please **do not** normalize your features for this problem but use the raw frequencies.

hint, adding some print statements can help with unnecessary panics:
```{r}
library(caret)
test_folds <- createFolds(DEP_VARIABLE, k=5)
for(i in seq_along(test_folds)){

    # Some code that isolates the test/train data!
    
    print(paste("cross validation fold", i))
    t0 <- Sys.time()
    ols <- lm(TRAIN_DEP_VARIABLE ~ TRAIN_INDEP_VARIABLE)
    print(paste('running OLS took', Sys.time() - t0))
    }
```

Side comment:
- You may want to see how the `lambda.1se` compares.
- (personal observation) Normalizing the features does help with the optimization but our features are
  all token frequencies so it's not as big of a concern.

## Question 3
For the algorithm that performed the best, please retrain the model with the following requirements:
- Use all of the data, i.e. do not reserve data for test/train.
- You may need to normalize the features. If Lasso/Ridge was best, note that sparsity will not hold after
  you normalize.

Please plot the distribution of the coefficients.

## Question 4
Please list out the top tokens corresponding to the strongest non-zero coefficients.

Side comment: If you are not or were not an American, what do these tokens and their coefficients
suggest about inauguration?
