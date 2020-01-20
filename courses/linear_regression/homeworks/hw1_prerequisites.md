# Homework 1: Prerequisite

### Purpose
Homework 1 is meant to give you some practice to refresh your basics for the course.

### Expectations
- These are all pre-requisites for the class so if you find some of these challenging, you should reach out to the TA to brush up on these topics.
- Please upload a scanned image of your solution to CourseWorks.

### Assignment:
**Q1** Please calculate the following statistics for the noise complaints from the dataset `graffiti_vs_noise_by_zip_2018`. No code necessary but please round the answer to the 5th decimal.
- The mean
- The sample standard deviation (with the n-1 factor)
- The mean for zip codes between 11000 and 11500 (inclusive, i.e. including 11000)
- The sample standard deviation for zip codes between 11000 and 11500

**Q2** 
Please express $$Var(X + Y)$$ using $Var(X)$, $Var(Y)$, and $Cov(X, Y)$.

**Q3** 
Imagine I have a coin with $P(coin toss = Heads) = p$, write down the probability that I have `k` heads after tossing the coin `n` times?

**Q4** 
Continuing Q3, what value of `p` would maximize the probability above? Please express the answer in terms of `k` and `n`.

For Q5 and Q6, note that 2 distributions can be the same **type** of distribution but may not be the same distribution if they do not share the same set of parameters. 

**Q5** 
True/False, if the means are the same between two distributions, they must be the same distribution. No proof necessary.

**Q6** 
True/False, if the means are different between two distributions, they must be different distributions. No proof necessary.

**Q7** 
Let $Y = f(X)$ where $X$ is a random variable with $SD(X)>0$, please mathematically write down a solution for $f()$ such that $E(Y)=0$ and $SD(Y)=1$.

For Q8 and Q9, pretend that we simulated 100 data points from a random variable, $X\sim Normal(0, 1^2)$ and another 50 data points from a random variable, $Y\sum Normal(0.1, 1.1^2)$. However, you are not told the true distributions of $X$ and $Y$ but only given the data.

**Q8** 
Please write the R code that would compute the 95% confidence interval for the expectation of X.

**Q9**
We want to test the idea whether the expectation of X is the same as the expectation of Y.
- What is your null hypothesis?
- Please write the code that would calculate the p-value from a 2 sample t-test that does not assume the variances are identical.
