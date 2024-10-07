# Homework2 - Simulating time series-like data

### Goals
The purpose of this homework is to give you some experience in simulations
and the problems that surface when dealing with time series.

#### Question 0 creating correlated errors through time
Please write a function that takes in an integer, `n`, equal or larger than
1, then produces "errors" that are generated in the following way:
- The first error is always a Normal(0, 1), i.e. $$\epsilon_1 \sim N(0, 1)$$ random variable
- If `n>1`, then the subsequent errors should also follow a Normal distribution with standard deviation
  1 but with a mean starting from the previous error, i.e. $$\epsilon_i \sim N(\epsilon_{i-1}, 1)$$.
- Your output should be a numeric vector of length `n`


#### Question 1, visualizing correlated errors
To understand correlated errors, it's best to visualize and compare them to independent errors.
To do this, please create 2 plots: one with correlated errors and one with independent errors.
- For the correlated errors, let `n=500` and create 5 different sets of correlated errors using your function in Question 0. Please plot these errors in the natural order on the same plot.
- For the independent errors. Draw 5 sets of independent errors, 500 samples per set and all following a Normal(0, 1). Please plot them in on the same plot.

#### Question 2, comment on the difference
According to the plots you've created, please answer the following:
- Do both type of errors overall have mean 0 (1 sentence)? What could you do to be more certain (1 sentence)?
- Which type of errors have a larger variance or are they comparable?


#### Question 3, how correlated errors affect OLS
Please simulate data from the usual linear model $$Y_i = X_i\beta + \epsilon_i$$,
except that $$\epsilon$$ are now generated from your correlated function.
Let the non-constant column in $$X$$ be evenly spaced values between
0 and 10 in increments of 0.02 (inclusive of bounds, this implies the `n`).
Set $$\beta = \binom{1}{2}$$.
You should assume that at each value of $$X_i$$, we only observe one $$Y_i$$

For each dataset generated, please fit the ordinary linear regression (OLS i.e. `lm()`) and store:
- the fitted parameters
- the associated SE for the parameters in the output of `summary.lm()`

Please create 1000 simulated datasets and estimate real the
mean and SE of the regression coefficients.

Do the mean and SE based on the simulated values "overall agree" with the values from `summary.lm()`?
Please explain your answer with a graph.

#### Question 4
Repeat the steps above but replace the OLS with different versions of ARIMA:
- `arima(y, order=c(1, 1, 1), xreg=X)`
- `arima(y, order=c(1, 1, 0), xreg=X)`
- `arima(y, order=c(0, 1, 1), xreg=X)`
- `arima(y, order=c(0, 1, 0), xreg=X)`
You only need to store the result related to the parameter for `X`.

- Which model fits our random walk the best?

#### Question 5
Which of our usual regression conditions are satisfied in our simulation above?
- linearity $$Y = X\beta + \epsilon$$
- errors have 0 conditional expectation $$E(\epsilon\vert X) = 0$$
- errors are independent
- errors have a constant conditional variance $$Var(\epsilon\vert X) = \sigma^2$$
- errors follow a normal distribution


{% include lib/mathjax.html %}
