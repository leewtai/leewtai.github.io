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
- For the correlated errors. Let `n=500` and create 5 different sets of correlated errors using your function above. Please plot these errors in order on the same plot.
- For the independent errors. Again draw 5 sets of independent errors (500 samples each, all Normal(0, 1)) and plot them in order on the same plot.


#### Question 2, comment on the difference
According to the plots you've created, please answer the following:
- Do both type of errors overall have mean 0? One sentence explanation.
- Which set of errors have a larger variance or are they comparable?


#### Question 3, how correlated errors affect OLS


{% include lib/mathjax.html %}
