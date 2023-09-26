# Homework 1: Prerequisite

#### Goals
Homework 1 is meant to tie together the statistics and programming concepts and start to read the outputs of the regression function in R.

#### Q0 - Different objective functions

The average is a good statistic because it "optimizes" a particular objective, the
total squared error:

$$\sum_{i=1}^n (X_i - \alpha)^2$$

Where $$X_i$$ is the i-th data point and $$\alpha$$ is a candidate statistic.

For this problem, please:
- Write a function called `total_squared_error()`, hint: look up the function `calc_se` in these [notes](https://leewtai.github.io/courses/stat_computing/lectures/learning_r_debug.html) if you have not defined a function before.
  - It should take in 2 inputs: `X` and `alpha`
  - It should execute the calculation above for the total squared error
  - It should output a single number. This number should be titled `total_sq_from_alpha` in your function.
- Please simulate 2000 random numbers from the exponential distribution (hint: `rexp()`) with the default parameter setting. Assign these values to a variable named `X`
- Please create a variable called `alpha_candidates` that is a vector that contains the values:
  - The mean of `X`
  - The median of `X`
  - ((max of `X`) + (min of `X`)) / 2
  - The mean of `X_trimmed`, where `X_trimmed` is `X` but removing the values that are larger than
    `5 * sd(X)` above the mean of `X` or smaller than `5 * sd(X)` below the mean of `X`.
- Please apply `total_squared_error()` to your `X` and each value in `alpha_candidates` and visualize this result and label your plot.
- Please write one sentence about which statistic has the smallest total squared error.


#### Q1 - Loading data and applying functions
Please calculate the following statistics for the police payroll dataset `processed_nyc_payroll_2022.csv` on Canvas. Please show your code and print out your final solutions (e.g. using `print()`).
If you have not worked with data frames, the [notes here](https://leewtai.github.io/courses/stat_computing/lectures/learning_r_data_viz.html) may be useful.

- Calculate a new variable called `total_pay`, where `total_pay` is the sum of the 3 columns that correspond to pay (recall that salary is not the same as pay).
- Are there any missing values or negative values in the data? One sentence answer please.
- Please calculate the minimum, maximum, 25th percentile, 50th percentile, and 75th percentile of `total_pay`. Treat missing values as 0 if there are any. You should make sure it's obvious to the grader which value corresponds to which statistic.
- Please repeat the above calculation for each gender category in the dataset.
- Please print out **one** name that has gender `'other'` or `'both'` that you would consider it obviously male or female. Please write out which gender you believe this name should be associated with. Your code does not need to show how you made this discovery.
- What is the 3 most popular job title in the dataset?
- Please filter the data to only those with the job title `'POLICE OFFICER'` then assign the data frame to a variable called `police`.
- Please plot the `total_pay` against the tenure in `police`. Hint: `sub(" days", "", "12 days")`


#### Q2 - Simulating the law of large numbers
- Does the law of large numbers apply to the standard deviation?
  - please simulate data from a Normal distribution (choose your own mean and sd).
  - please try out 100 different sample sizes, the smallest should be 5 and the largest should be 50000.
  - you create 3 different samples for each given sample size
  - show in a graph then answer in 3 sentences whether you observe the law of large numbers for the standard deviation?


#### Q3 - Logic review
Small reminder, 2 distributions can be the same **type** of distribution but may not be the same distribution if they do not share the same set of parameters. 
- True/False, if the means are the same between two distributions, they must be the same distribution. No proof necessary.
- True/False, if the means are different between two distributions, they must be different distributions. No proof necessary.
- True/False, if two distributions are the same, they have the same mean and variance. No proof necessary.


#### Q4 - Functions
We often deal with variables on different scales which can make interpreting results difficult. A useful trick is to standardize each variable such that its mean is 0 and standard deviation is 1. What transformation can do this?
- Please write down an R function called `standardize()` (without using the built-in function `scale()`) that transform data such that its mean is 0 and standard deviation is 1.
- Please simulate some data with $$E(X) \neq 0$$ and $$SD(X) > 1$$ then show that your function is working properly on this set of data.
  - You should demonstrate that the average and standard deviation of your simulated data satisfies the conditions above
  - You should show that after applying the function you defined, the average and standard deviation of the transformed data is now "standardized".


#### Q5 - Simulation and hypothesis testing review
- Please write the code that would simulate 100 data points from a random variable $$X\sim Normal(0, 1^2)$$ and another 50 data points from a random variable $$Y\sim Normal(0.1, 1.1^2)$$.
- Pretending we do not know the parameters used to generate the data, please construct the 90% confidence interval for the expectation of $$X$$ using the data you simulated. Please show your code (you can use built-in functions for this).
- Pretending that we do not know the parameters used to generate the data, we want to test the idea whether the expectation of X is the same as the expectation of Y.
  - Please write the code that would calculate the p-value from a 2 sample t-test that does not assume the variances are identical. Remember to report your p-value. (You can use built-in functions for this)
  - Is the null hypothesis true in this situation or not (given you know how the data is simulated)?
- If we fail to reject the null hypothesis, why can't we say the null or alternative hypothesis is true? Maximum 4 sentences.
- Repeat the p-value calculation with 1000 new set of simulations for $$X$$ (100 values) and $$Y$$ (50 values), what percentage of these 1000 p-values are below 5%? (This is "like" your statistical power except that we know the true difference)


{% include lib/mathjax.html %}
