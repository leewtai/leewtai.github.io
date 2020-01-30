# Random Functions in R

#### Statistical Computing
The foundations to statistical computing are
- Aggregate data
- Simulate randomness

```r
coin_tosses <- sample(c("HEAD", "TAIL"), 10, replace=TRUE)`
```

#### Example: the Law of Large Numbers
Theorem:

As the sample size increases, the sample average converges to the population
average.

How would we simulate this phenomenon?

#### Reintroducing the Normal Distribution
![normal density](normal_density.png)
- `rnorm()` returns a sample from the distribution
- `dnorm()` returns the density
- `pnorm()` returns the probability less than or equal to point x
- `qnorm()` returns the quantile given a probability

#### How would you stress test the Normal functions?
If you didn't believe in the function, how would you test it?

Start with what you know then work backwards, what do you know mathematically about a standard normal?
  - Center
  - Spread
  - Specific percentiles?

#### Making non-deterministic functions deterministic
```r
set.seed(444)
rnorm(1)
rnorm(1)
rnorm(1)
set.seed(444)
rnorm(1)
rnorm(1)
set.seed(444)
# guess the output of
# rnorm(2)
```

#### Order matters when setting the seed
```r
set.seed(444)
sample(c(1, 2, 3, 4, 5))
rnorm(2)
```

#### Other functions that create random data
- `sample()`
  To draw with or without replacement from a given vector
  - `sample(c('HEAD', 'TAIL'), 10, replace=TRUE)`
  - `sample(1:52, 5)`
- `runif()`
  To draw data from a uniform distribution
  - `runif(10)`
  - `runif(10, min=0, max=100)`
- `rnorm()`
  - `rnorm(10)`
  - `rnorm(10, mean=100, sd=13)`
- `rexp()`
  - `rexp(10)`
  - `rexp(10, rate=0.01)`

#### Back to demonstrating the Law of Large Numbers

Create a large vs small dataset:
```r
n <- 10
small_data <- rnorm(n)
large_data <- rnorm(n * 100)

small_avg <- mean(small_data)
large_avg <- mean(large_data)
```

Now what?

#### Common mistake with random variables
A **single realization** does not demonstrate tendencies for random variables!
By chance, we can always observe the opposite from what we expected.

For demonstration, recall that the average of normals is still a normal!
```r
a_narrow_norm_sample <- rnorm(1, sd=0.5)
wider_norm_samples <- rnorm(120, sd=1)

wider_dist <- abs(wider_norm_samples - 0)
narrow_dist <- abs(a_narrow_norm_sample - 0)
accidents <- wider_dist <= narrow_dist
mean(accidents)
```

A random variable is characterized by its behavior over **multiple realizations**

#### Simulating multiple realizations

Each realization is essentially identical to the other, something for-loops
are very good at.

Let's wrap the previous code in a for-loop!
```r
num_sim <- 1000
large_avgs <- c()
small_avgs <- c()

for(i in 1:num_sim){
    n <- 10
    small_data <- rnorm(n)
    large_data <- rnorm(n * 100)

    small_avgs[i] <- mean(small_data)
    large_avgs[i] <- mean(large_data)
}
```

Now what?

Code comment:
- `n` doesn't change over the iterations, we should take it out of the loop

#### There are many ways to analyze the "spread" of a distribution
```r
sd(small_avgs)
sd(large_avgs)

IQR(small_avgs)
IQR(large_avgs)

mean(abs(small_avgs) >= 0.1)
mean(abs(large_avgs) >= 0.1)
```
