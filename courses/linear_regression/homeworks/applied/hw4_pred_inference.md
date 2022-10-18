# Homework 4: Prediction vs Inference

Here are the formulas in textbooks and from our slides when all 5 assumptions are satisfied under simple linear regression:

- $$\hat{\beta}_0 = \bar{y} - \hat{\beta}_1 \bar{x}$$
- $$\hat{\beta}_1 = Corr_{x, y}\frac{SD_y}{SD_x}$$
- $$Var(\hat{\beta}_1|X) = \frac{\sigma^2}{\sum (x_i - \bar{x})^2}$$
- $$Var(\hat{\beta}_0|X) = \sigma^2\left[\frac{1}{n} + \frac{\bar{x}^2}{\sum (x_i - \bar{x})^2}\right]$$
- $$\hat{\sigma}^2 = \frac{1}{n-2}\sum (y_i - \hat{y}_i)^2$$
- $$\frac{\hat{\beta}_1}{\hat{SE}(\hat{\beta}_1|X)} \sim t_{df=n-2}$$
- $$\frac{\hat{\beta}_0}{\hat{SE}(\hat{\beta}_0|X)} \sim t_{df=n-2}$$

Recall that: $$\hat{SE}(\hat{\beta}_1|X)$$ differs from $$SE(\hat{\beta}_1|X)$$ becase it estimates $$\sigma^2$$ with $$\hat{\sigma}^2$$


#### Q1 - Verifying calculations from summary.lm()
Please create a matrix or data frame called `summ_tab` using the formulas above that matches the output from the `coefficients` attribute under `summary.lm()`
You may use basic functions like `pt()`, `mean()`, `sd()`, `corr()`, `sum()`, `/`, etc

#### Q2 - different ways to generate data

Please first generate data using the following code:
```
n <- 50
x <- rnorm(n)
z <- runif(n)
w <- rexp(n)
indep_vars <- cbind(x, z, w)

errors <- rnorm(n, sd=10)
betas <- c(1, 2, 3, 4)
y <- betas[1] + betas[2] * x + betas[3] * z + betas[4] * w + errors
# The following will produce an error
should_be_y <- indep_vars %*% betas + errors
```

The `%*%` symbol is how we tell R to perform [matrix multiplication](https://en.wikipedia.org/wiki/Matrix_multiplication).
The last line above should produce an error. Please modify `indep_vars` such that `y` and `should_be_y` are almost identical (within machine precision). Be sure to demonstrate
that the two variables, after your fix, are almost identical.

FYI, R implicitly treats vectors as matrices as `n` by `1` matrices when doing matrix operations.

#### Q3 - Cross checking formulas

Continue from Q2, to run the regression of `y` on `x`, `z`, and `w`, we can run `mod <- lm(y~x + z + w)`
For each of the following matrix expression, write out the corresponding R code to perform the matrix operation, THEN write at most 2 sentences that describe its relationship to values within `summary(mod)$coefficients`.
- $$\hat{\beta} = (X^TX)^{-1}X^TY$$
- $$Cov(\hat{\beta}|X) = \sigma^2 (X^TX)^{-1}$$

Hint:
- $$X^T$$ indicates the transpose of the matrix X.
- $$Z^{-1}$$ indicates the inverse of matrix `Z`, see `solve`
- $$X^TX$$ performs matrix multiplication between the matrix `X^T` and `X` itself.
- $$Cov(\epsilon)$$ denotes the covariance matrix of $$\epsilon$$, this has the definition of $$E([\epsilon - E(\epsilon)]^T[\epsilon - E(\epsilon)])$$
Please numerically verify the formulas based on matrices match our previous formulas for SLR (e.g. those given on the midterm) for the following quantities (hint: we've shown that `summary.lm()` agrees with our formulas before). You are expected to generate your own $$n$$, $$\beta$$, $$\epsilon$$ etc.

- $$\hat{SE}(\hat{\beta}_i\mid X)$$
- $$\hat{SE}(\hat{Y}\mid X)$$

#### Q4 - confidence intervals from different bootstraps
Use the file `hw4_scatter.csv` on Canvas, please reproduce the following plot:
<img src="../images/hw4_conf_inter_boot.png" alt="conf_inter_boot" width='600'>

#### Q5 - intuition practice
- Continuing from Q4, If we used `predict.lm(..., interval="confidence")`, would its results align better with the classic bootstrap or bootstrapping the residuals?
- Which method is more "correct", the classic bootstrap or bootstrapping the residuals?

#### Q6 - Prediction Intervals
First generate your data following the process below:

```r
set.seed(100)
n <- 50
x_range <- 1:20
beta0 <- -5
beta1 <- 1.2
x <- sample(x_range, n, replace=TRUE)
y <- beta0 + beta1 * x + rnorm(n)
```
For the first 3 problems, do not overwrite your original `x`, `y` data pairs.
- Plot the `80%` confidence interval and prediction interval on the scatter plot of x and y (hint: `predict.lm()`). The range of x values should be all the integers from 1 through 20.
- Generate `1000` new data pairs, what percentage of them are within your prediction interval?


#### Q7 - Prediction or inference
For each of the following, please state whether we should care about the prediction interval or the confidence interval for the regression line, no need for explanation.
- You have data between engagement with similar startups (e.g. page views) and marketing spend from multiple companies, you're curious about how much engagement your startup will get if you spend X dollars. Should you use a prediction interval or confidence interval?
- You have data on a specific spring between the weight placed on it vs the length it stretched (the length is measured by eye-balling, i.e. noisy). You want to guess the length of this particular spring if you give it weights you have not measured before, should you compute the confidence interval or the prediction interval for this problem?
- The government wants to learn about the relationship between investment in education vs poverty levels to make policies that would affect many households, should they compute the confidence interval or the prediction interval?


#### Q8 - How categorical values are turned into numbers and handled in regression

Run the following code
```
n <- 50
cat_variable <- c('A', 'B', 'C')
group <- factor(sample(cat_variable, n, replace=TRUE), levels=cat_variable)
y <- rnorm(n)

X <- model.matrix(~group)
mod <- lm(y ~ group)
mod2 <- lm(y ~ X)
```

- Examine at the first few rows of `X` and explain the relationship between `X` and `group` using no more than 4 sentences.
- `mod2` has a coefficient listed as `NA`, how can we change the code above such that this doesn't happen? Please explain why this happens using at most 2 sentences (we're looking for one keyword).
- Please verify or disprove that `mod` and `mod2` are "the same" from a statistical perspective? Statistical here means attributes, artifacts, or behavior from the model.

{% include lib/mathjax.html %}
