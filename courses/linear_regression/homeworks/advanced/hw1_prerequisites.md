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

#### Q4 - Calculus review in finding maximums
Continuing Q3, what value of `p` would maximize the probability above? Please express the answer in terms of `k` and `n`.

#### Q5 - Logic review
Small reminder, 2 distributions can be the same **type** of distribution but may not be the same distribution if they do not share the same set of parameters. 
- True/False, if the means are the same between two distributions, they must be the same distribution. No proof necessary.
- True/False, if the means are different between two distributions, they must be different distributions. No proof necessary.

#### Q6 - Algebra with random variables
Let $$Y = f(X)$$ where $$X$$ is a random variable with $$SD(X)>0$$, please mathematically write down a solution for $$f()$$ such that $$E(Y)=0$$ and $$SD(Y)=1$$.

#### Q7 - Simulation and hypothesis testing review
- Please write the code that would simulate 100 data points from a random variable $$X\sim Normal(0, 1^2)$$ and another 50 data points from a random variable $$Y\sum Normal(0.1, 1.1^2)$$.
- Pretending we do not know the parameters used to generate the data, please construct the 87% confidence interval for the expectation of X using the data you simulated. Please show your code.
- Use at most 2 sentences to explain why we should "pretend we do not know the parameters used to generate the data" when constructing the confidence interval?
- Pretending that we do not know the parameters used to generate the data, we want to test the idea whether the expectation of X is the same as the expectation of Y.
  - What is your null hypothesis?
  - Please write the code that would calculate the p-value from a 2 sample t-test that does not assume the variances are identical. Remember to report your p-value.

{% include lib/mathjax.html %}
