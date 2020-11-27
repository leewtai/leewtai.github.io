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

#### Q1 - Do no harm?
Please generate data once again, using a similar model (notice `n` is increased):

```r
n <- 1000
beta0 <- -5
beta1 <- 1.2
max_x <- 10
x <- runif(n, 1, max_x)
y <- beta0 + beta1 * x + rnorm(n, sd=x)
x_new <- seq(1, max_x, length.out=20)
y_new <- beta0 + beta1 * x_new + rnorm(length(x_new), sd=x_new)
```

We would like to examine how we're being hurt when we add in random features (again, this means features that do not contribute to the variability in `y`). 
Let `m` indicate the number of random features we are adding to the problem (you can make up your own random features as long as none of them are identical to one another). For this problem, we will focus on the inference for $$\beta_1$$.
- How can we obtain a reliable estimate for the standard error of $$\hat{\beta}_1$$? Specifically, can we use `summary.lm()`, can we bootstrap the residuals, and/or can we do classic bootstrap? (A simple yes/no to each method is sufficient, in an exam I will ask for the reasons)
- Please numerically or graphically show that the estimated standard error of $$\hat{\beta}_1$$ (using one of the methods you recommend above) increases as you increase `m`.  Two different values of `m` is sufficient but please make the effect is very obvious while keeping $$(2 + m) < n$$ so you have enough data.
- With "random features", is our regression estimates $$\hat{\beta}_1$$ still unbiased? How would you verify this idea, i.e. come up with a numerical/graphical example to try to falsify this idea? Please remember that statistics in general can only "reject" or "fail to reject" with these types of questions but your example should show that you know what unbiased means. 
- Please show that your prediction accuracy for the new data points `x_new` decrease as `m` increases (again, 2 different `m` values is sufficient) as well using the following methods:
  - calculate the percent of new data points that fall within the point-wise `95%` prediction interval
  - calculate the average squared error between your prediction and the new data point
  - calculate the maximum absolute error between your prediction and the new data point
  hint: "your prediction" in a regression class means, given some independent feature, what's your best guess (a single value) for the dependent variable?

{% include lib/mathjax.html %}
