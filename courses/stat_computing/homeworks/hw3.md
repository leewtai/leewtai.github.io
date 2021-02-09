# Homework 3 - random variables ARE functions

#### Context: modeling data with random variables
In your introductory statistics course, you likely came across probability distributions.
These are useful mathematical tools that summarize complicated datasets efficiently using
parameters. For example, if you claim some data is Normally distributed, then by simply
providing the mean and variance of the data (i.e. the parameters for the Normal distribution
but also common summary statistics for most distributions) could give people a strong sense of how the
data is distributed. For example, IQ scores are Normal and are designed so the mean is 100
with a standard deviation (SD) around 15 (i.e. variance is 15^2). These parameters along with the
Normal distribution allow us to know various facts like that half of the people have IQ above 100,
68% of the population should have IQ between 85 and 115, and less than 2.5% of the people have IQs above 130.

R has several built-in functions that draw random samples from well-known distributions given
parameters:
- `rnorm(10, mean=2, sd=3)` would return 10 samples from the Normal distribution with mean 2 and SD 3.
- `rexp(3, 0.02)` would return 3 samples from the exponential distribution with rate as 0.02.
- `runif(50, -2, max=1)` would return 50 samples from a uniform distribution ranging from -2 to 1.

#### Q0 Knowing R's built-in random functions
With the help of Wikipedia, you should be able to find how the parameters of the various distributions
relate to summary statistics like the mean and variance of those distributions.

- Please write a function `new_runif()` that takes in 3 parameters, `n`, `mean`, and `sd` then produces
  `n` random samples with the specified mean and SD.
  - The default mean should be 0 and default SD should be 1
  - You should write this functin leveraging `runif()`
  - The SD is simply square-root of the variance.
- Please draw 1000 samples from `new_runif()` and `rnorm()` with the same mean and SD then plot their histograms.
  - The histograms can be 2 different plots. If you know what a density is, you could also try to overlay the
    density plots, try `plot(density(SOME_DATA))`
  - It should be clear which plot or curve represents which distribution.

Side Note:
- it's important to know that different distributions, with the same mean and SD can look very different.

#### Q1 Creating a multi-modal random variable
A difficult type of data to describe are datasets with multiple modes or peaks in their distribution.
Height across men and women is one such example. One popular probability distribution to describe
such data is the mixture gaussian distribution. 

Please write a function `rgaussmix()` that can generate samples from a mixture gaussian distribution.
The inputs (in order) should be:
- `n`, an integer that represents the number of indepdendent samples you want from this random variable
- `mus`, a numeric vector with length `k`, mathematically we would denote this as $$\mu_1, \dots, \mu_k$$
- `sds`, a numeric vector with length `k`, mathematically we would denote this as $$\sigma_1, \dots, \sigma_k$$
- `prob`, a numeric vector with length `k` that indicates the probability of choosing the different Gaussians. This should have a default to `NULL`.
Please note that `k` is provided by the user who is calling `rgaussmix()` and should be derived from the
parameters, this should not be an input to your function.

To draw a single sample from the Mixture Gaussian Distribution with `k` modes.
- Sample from `1` through `k` according to the probabilities of `prob`, let's assign this sample to a variable named `j`
  - if `prob` is `NULL`, then you should sample uniformly.
- Use the `j`-th element from `mus` and `sds` to get a sample from a Normal distribution with mean$$=\mu_j$$ and SD$$=\sigma_j$$
- The resulting sample from this Normal is then from a Gaussian Mixture.
- Repeat the above steps to get another sample

The function should return a numeric vector of length `n` where each element is a realization from the Gaussian mixture specified.

Requirements for the function:
- Please check that the length of `mus` matches the length of `sds`. If not, please use `stop()`
    to return an Error message saying "mus and sds have different lengths".
- If given `n=0`, the function should return an empty vector, please AVOID using `if()` to address this issue. Hint: `seq_len()`
- Pleaes leverage `rnorm()` and `sample()` in your code.

Please submit the code for this quesiton.

#### Q2 Testing out the function
Please apply your function above with the following inputs and show the desired output:
- `rgaussmix(mus=1:3, sds=rep(0.1, 3), n=300)`
  - Please show the histogram for this.
- `rgaussmix(300, mus=1:3, sds=rep(0.1, 3), prob=c(0.5, 0.4, 0.1))`
  - Please show the histogram for this.
- `rgaussmix(0, mus=1:3, sds=rep(0.1, 3), prob=c(0.5, 0.4, 0.1))`
  - This should return an empty vector
- `rgaussmix(10, 1:3, 1:4)`
  - Please show that this should return an error
- `rgaussmix(300, mus=1:3, sds=c(0.2, -1, 0.5))`
  - If you leveraged `rnorm()`, you should have `NA` values for some with a warning message, please show these messages.
  - Please plot the histogram from this command.
- Please comment how `hist()` addresses NA values in your data:
  - Does it warn you that NA values were detected?
  - Does the histogram function throw an error or warning?


#### Q3 Central Limit Theorem
Here we are going to simulate the central limit theorem, something even more miraculous than the Law of Large Numbers!

We want to demonstrate that the CLT works on complicated distributions, like a Gaussian mixture. Imagine we had a Gaussian mixture where the first and second components are Normal(10, sd=2) and Normal(18, sd=2) respectively, and the first component is 4 times more likely to appear than the second component.
By demonstrate, we mean that the sample averages will follow a bell curve and the width of the bell curve will decrease with larger sample sizes.

You are expected to leverage your function from Q1.

Please demonstrate the CLT works by showing the following:
- Choose an appropriate sample size, `n`, where samples from the Gaussian mixture can produce histograms that clearly show the bimodal pattern (e.g. n >> 10). Please plot the histogram with your sample size in the title of the graph.
- (this is worded intentionally more statistically) Please simulate 2500 different **sample averages** for the sample size you chose above and plot the distribution of the **sample averages**.
- Now please repeat the step above but draw `10*n` data points. Please make sure the new plot is comparable to the previous one, e.g. if I hid the tick marks, the distribution with the larger sample size should have a visibly tighter distribution.
  - You should not hide the tick marks!

Please show all code and all graphs.

Side note: notice how the distribution of the sample average should be "bell-shaped" but no longer bimodal!!!


{% include lib/mathjax.html %}
