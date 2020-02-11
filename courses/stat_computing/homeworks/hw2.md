# HW2 - Programming with statistics

#### Q1
Imagine a random variable with variance 0.25 and assume you have `n=100` independent realizations
from this random variable. What is **the variance** of
the sample average using these 100 realizations? (No code here!)

(We do not need to know whether this variable is Normal or not.)

#### Q2
Please **write the code** that simulates 100 data points from a Bernoulli random variable with p=0.5 (i.e. the fair coin except heads=1 and tails=0),
and assign these values to a variable called `coin_tosses`. Then **write the code** that computes the sample average of these data points and call that value `p`.

#### Q3
To simulate the behavior of the sample average, i.e. `p`, we need to repeat the calculation over
different datasets. Please **write the code** that simulates `B=100` separate sample averages similar to the specifications
in Q2 and calculate the sample variance on these sample averages (hint: `var()`).

#### Q4
Which statement is true about relationship between the answers from Q1 and Q3. No explanation needed. Hint, you can simulate each of these.

1. TRUE/FALSE, if we increased `B`, then the uncertainty in the sample average, as
   an estimate for the population average, will decrease.
2. TRUE/FALSE, if we increase `n`, then the uncertainty of the sample average, as
   a random variable, will decreases.
3. TRUE/FALSE, if we increase `B`, the proportion of sample averages in Q3 that deviate from
   0.5 by a magnitude of 0.05 will decrease.
4. TRUE/FALSE, if we increase `B` the variance from Q3 will get closer to the answer in Q1.

Hint: there are two sample sizes here: one for the average and one for the simulation, you need to keep these two concepts clearly separated.

#### Q5
Please note that the fair coin has the highest variance compared to all other coins with different probabilities of showing heads. 
Therefore, the fair coin is also a convenient upper bound for calculating sample sizes necessary when we are estimating
the probability of certain events.

If we want to estimate the probability of an event (an unknown probability) happening with a standard error smaller than 1%, how many samples do we at least need?
Please **show the code** that does this calculation for you and report the number.

#### Q6
In social sciences, the correlation between 2 variables can be very low but it is very
unlikely to have exactly 0 correlation. We will use simulation to estimate random variables that should have 0 correlation.

Please simulate 2 sets of data points with `n=195` each (roughly the number of countries), one from a standard normal distribution,
and another one drawn uniformly over the integers from 1 through 20 (inclusive of the bounds and with replacement).
All samples are independent of each another.

Please **show the code** that simulates the data and calculate the correlation between your 2 sets of random variables.

#### Q7
Using a for-loop, please estimate the probability of seeing a correlation value above 0.1 or below -0.1 between these 2 sets of independent random variables in the setting of Q6. 
Please choose a sensible number of simulations such that the standard error for this probability is at most 1%.
Please show all code and report your estimate.

Hint: to estimate the probability of a standard normal random variable falling outside of -1.5 and 1.5, we would do:
```r
sim_data <- rnorm(1000)
out_of_range <- (sim_data > 1.5) | (sim_data < -1.5)
mean(out_of_range)

# Should approach the following with larger sample sizes
pnorm(-1.5) * 2
```
