# Homework 1: Prerequisite

#### Goals
Homework 1 is meant to give you a concrete understanding of the prerequisites for this class. If you find these challenging, you should reach out to the TA to brush up on these topics.

#### Q1 - Loading data and applying functions
Please calculate the following statistics for the noise complaints from the dataset `graffiti_vs_noise_by_zip_2018.csv` on Canvas. You do not need to submit your code but please round the answer to the 5th decimal.
- The mean
- The sample standard deviation (with the n-1 adjustment)
- The mean for zip codes between 11000 and 11500 (inclusive, i.e. including 11000)
- The sample standard deviation for zip codes between 11000 and 11500

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

#### Q6 - Algebra with random variables
We often deal with variables on different scales which can make interpreting results difficult. A useful trick is to standardize each variable such that its mean is 0 and standard deviation is 1. What transformation can do this?
- Please write down an R function called `standardize()` (without using the built-in function `scale()`) that does this.
- Please simulate some data with $$E(X) \not\eq 0$$

Let $$Y = f(X)$$ where $$X$$ is a random variable with $$SD(X)>0$$, please mathematically write down a solution for $$f()$$ such that $$E(Y)=0$$ and $$SD(Y)=1$$.

#### Q7 - Simulation and hypothesis testing review
- Please write the code that would simulate 100 data points from a random variable $$X\sim Normal(0, 1^2)$$ and another 50 data points from a random variable $$Y\sim Normal(0.1, 1.1^2)$$.
- Pretending we do not know the parameters used to generate the data, please construct the 87% confidence interval for the expectation of X using the data you simulated. Please show your code.
- Pretending that we do not know the parameters used to generate the data, we want to test the idea whether the expectation of X is the same as the expectation of Y.
  - What is your null hypothesis?
  - Please write the code that would calculate the p-value from a 2 sample t-test that does not assume the variances are identical. Remember to report your p-value. (You can use built-in functions for this if you wish)
- If we fail to reject the null hypothesis, why can't we say the alternative hypothesis is true?

{% include lib/mathjax.html %}
