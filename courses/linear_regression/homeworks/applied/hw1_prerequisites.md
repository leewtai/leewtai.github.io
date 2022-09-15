# Homework 1: Prerequisite

#### Goals
Homework 1 is meant to give you a concrete understanding of the prerequisites for this class. If you find these challenging, you should reach out to the TA to brush up on these topics.

#### Q1 - Loading data and applying functions
Please calculate the following statistics for the noise complaints from the dataset `processed_nyc_payroll_201901.csv` on Canvas. Please show your code and print out your final solutions (e.g. using `print()`).
- Please calculate the minimum, maximum, 25th percentile, 50th percentile, and 75th percentile of `total_pay`, where `total_pay` is the sum of the 3 columns that correspond to pay. Treat missing values as 0 if there are any. You should make sure it's obvious to the grader which value corresponds to which statistic.
- Please repeat the above calculation for each gender category in the dataset.
- Please print out one name that has gender `'other'` but you would consider it obviously male or female. Please write out which gender you believe this name should be associated with. Your code does not need to show how you made this discovery.
- Please filter the data to only those from the `'FIRE DEPARTMENT'` and a job title `'FIREFIGHTER'` then re-calculate the pay statistics for each gender category.
- Please plot the `total_pay` against tenure for the firefighter subset created above. Let tenure be the number of years between the `2019-07-31` to their start date in the agency.

#### Q2 - Reviewing definitions
Please express $$Var(X + Y)$$ using $$Var(X)$$, $$Var(Y)$$, and $$Cov(X, Y)$$.

#### Q3 - Probability review
Imagine I have a coin with $$P(coin toss = Heads) = p$$, write down the probability that I have `k` heads after tossing the coin `n` times.

#### Q4 - For-loop review in finding maximums
Continuing Q3, let's fix `n=100`, then search for which values of `p` would maximize the likelihood, i.e. the answer from Q3, for different values of `k`.
- Please vary `k` from `0, 1, 2, ..., 100`
- Please vary `p` from `0, 1e-3, 2e-3, ..., 0.999, 1`

Please visualize your answer on a 2D grid where different values of `p` are on your x-axis, different values of `k` are your y-axis, and the color intensity correspond to the likelihood values (i.e. more saturated = higher likelihood). Please show your code.


#### Q5 - Logic review
Small reminder, 2 distributions can be the same **type** of distribution but may not be the same distribution if they do not share the same set of parameters. 
- True/False, if the means are the same between two distributions, they must be the same distribution. No proof necessary.
- True/False, if the means are different between two distributions, they must be different distributions. No proof necessary.
- True/False, if two distributions are the same, they have the same mean and variance. No proof necessary.

#### Q6 - Functions
We often deal with variables on different scales which can make interpreting results difficult. A useful trick is to standardize each variable such that its mean is 0 and standard deviation is 1. What transformation can do this?
- Please write down an R function called `standardize()` (without using the built-in function `scale()`) that does this.
- Please simulate some data with $$E(X) \neq 0$$ and $$SD(X) > 1$$ then show that your function is working properly on this set of data.
  - You should demonstrate that the average and standard deviation of your simulated data satisfies the conditions above
  - You should show that after applying the function you defined, the average and standard deviation is now "standardized".


#### Q7 - Simulation and hypothesis testing review
- Please write the code that would simulate 100 data points from a random variable $$X\sim Normal(0, 1^2)$$ and another 50 data points from a random variable $$Y\sim Normal(0.1, 1.1^2)$$.
- Pretending we do not know the parameters used to generate the data, please construct the 87% confidence interval for the expectation of X using the data you simulated. Please show your code.
- Pretending that we do not know the parameters used to generate the data, we want to test the idea whether the expectation of X is the same as the expectation of Y.
  - What is your null hypothesis?
  - Please write the code that would calculate the p-value from a 2 sample t-test that does not assume the variances are identical. Remember to report your p-value. (You can use built-in functions for this if you wish)
- If we fail to reject the null hypothesis, why can't we say the null or alternative hypothesis is true? Maximum 4 sentences. (EDITED, if you answered the previous version that's fine too)


{% include lib/mathjax.html %}
