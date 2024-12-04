# Homework4 - Preparing for your final project

### Goals
The purpose of this homework is to give you some time to work on your final project


#### Question 0: Final project check in
Please create one graph that visualizes the data for your final project. If you're still collecting
data, please grab external sources of data that would give you a sense of what the data may look like.
For example, if I'm waiting for the sleeping data of my baby (who is not born yet), I might get data (or a plot)
from medical journals on what is the expected sleeping duration for a new born child.
- Please make sure your graph is labeled (with units, labels, and titles)
- Please make write one paragraph to describe what a viewer should notice? Things to notice could 
  includeSurprises can lead to insights for generating hypotheses and non-surprises can serve as data validation.
  In the event of an external plot/data, you might want to summarize the motivation of the paper/journal for creating
  the plot.


#### Question 1: Comparing kriging to weighted averages
Let's try to simulate data that has a spatial dependence.
Our goal is to create data $$\epsilon = \begin{bmatrix}\epsilon(s_1) \\ \vdots \\ \epsilon(s_n) \end{bmatrix}$$
where $$Cov(\epsilon(s_i), \epsilon(s_j)) = \sigma^2 \exp(-\frac{d(s_i, s_j)}{\rho}) > 0$$. $$s$$ indicate the
different locations, $$d(s_i, s_j)$$ is the distance between $$s_i$$ and $$s_j$$.
So the covariance decreases as distance increases between 2 locations (e.g. NYC's weather vs Hoboken weather relative
to NYC vs SF weather).

- Using the code below, please visualize `y` over space that will highlight its spatial correlation.
- For 100 different random locations, please visualize the residuals from the weighted average using data that is biasedly collected, see `train` below.
  $$\bar{y}(s) = \frac{1}{\sum_i w(s, s_i)}\sum_{i\in neighbors(s)} w(s, s_i) y(s_i)$$ where $$w(s, s_i) = exp(-distance(s, s_i) / \rho)$$
- Please repeat the visualization above but use the kriging estimate instead of the weighted average. Be sure you're using the same training data as above so results
  are comparable. In other words, since we calculated 100 different averages, we should also train 100 different kriging models as well.
  For this class, please ignore any error messages related to the grid searches for lambda has hit the endpoints.
- Please comment on the difference you observe between the weighted average and the kriging methods.

```r
# Part 1
set.seed(100)
library(RColorBrewer)
sigma2 <- pi
rho = 10

n_samps <- 100
even_pts <- seq(0, 1, length.out=n_samps)
neighbor_dist <- 1 / n_samps
locations <- expand.grid(even_pts, even_pts)
dist_mat <- as.matrix(dist(locations, diag=TRUE, upper=TRUE))
cov_mat <- sigma2 * exp(-dist_mat/rho)
noise <- rnorm(nrow(locations))
L <- chol(cov_mat)
# L should be lower triangular, if not, use L = t(L)
corr_noise <- L %*% noise
mean_fun <- function(locs){locs[, 1] + locs[, 2] * 3}
y <- mean_fun(locations) + corr_noise 

# VISUALIZATION CODE GOES HERE

# Part 2-4
inner_square <- (locations[, 1] > 0.1
                 & locations[, 2] > 0.1
                 & locations[, 1] < 0.9
                 & locations[, 2] < 0.9)
test_locs <- sample(which(inner_square), 100)
get_biased_neighbors <- function(loc, locs, n=10){
    x <- loc[[1]]
    y <- loc[[2]]
    neighbors <- abs(locs[, 1] - x) < 0.1 & abs(locs[, 2] - y) < 0.1
    south_west_neighbors <- (locs[, 1] < x
                             & locs[, 2] < y
                             & neighbors)
    north_east_neighbors <- (locs[, 1] > x
                             & locs[, 2] > y
                             & neighbors)
    train <- sample(which(south_west_neighbors), n - 1)
    train <- c(train, sample(which(north_east_neighbors), 1))
    return(train)
    }
train_locs <- lapply(test_locs, function(ind) get_biased_neighbors(locations[ind, ], locations))
```

#### Question 2: Comparing sampling methods

Please generate data using the following code:
```{r}
set.seed(5833)
n <- 2^20
# create 5 states with one clear minority
states <- rep(c('A', 'B', 'C', 'D'), c(n/2, n/2^2, n/2^8, n/2^8))
states <- c(states, rep('E', n - length(states)))
# table(states) / n
streets <- vector('integer', n)
start <- 1
end <- 0
for(state in unique(states)){
    state_total <- sum(states == state)
    end <- end + state_total
    # let there be around 500 people on every street within a state
    streets[start:end] <- sample(seq_len(round(state_total / 500)), state_total, replace=TRUE)
    start <- end + 1
}
response <- rnorm(n, ifelse(streets < 5, -20, 0), ifelse(states %in% c('B', 'C'), 20, 5))
special <- 'D'
response[states == special] <- response[states == special] + rnorm(sum(states == special), 100, sd=50)
```

This is simulating a scenario where we could leverage people's state and their street to survey them for a variable, called `response`. It's important to know that "streets" are nested within the state, i.e. street 1 in State A is not the same as Street 1 in State B.

For the following sampling methods:
- An SRS of 2500 people from the population
- Within each state, an SRS 500 of the people
- Within each state, cluster sample 1 street out of all streets.
- Within each state, pick an SRS of 5 streets, then pick an SRS of 100 people from each of those sampled streets.

Please calculate or simulate the following for each of the sampling methods above:
- The expected number of people within the sample
- The expected value of the simple sample average of `response`, and is this unbiased for the population average of `response`?
- The expected value of the weighted sample average of `response`, where the weights for samples from different states are proportional to the states' population relative to the overall population, and is this unbiased for the population average of `response`?
- The probability of someone in State A street 2 to be sampled?
- The probability of someone in State D street 2 to be sampled?
- The expected value of the simple sample average of `response` based on only samples from State D, and is this unbiased for the true average of `response` in State D?
- The SE of the simple sample average based on only samples from the State 'D'?
- The Mean Squared Error of the simple sample average based on only samples from the State `D` for estimating the true average of `response` in State D?


#### Question 3: Simulation

Imagine a variable, Y, where $Y_{men}\sim N(0, Variance=1)$ and $Y_{women} \sim N(1, Variance=4)$. If we can collect 100 samples from a population of 1000000 people (you should assume exactly 50/50 split between the sex). Which of the following is the most accurate on average for estimating the population average or are they comparable? Please justify your answer with a proof or a simulation.
- An SRS of 100 from the population using the simple sample average
- 50 samples from each sex using the simple sample average
- 20 samples of men and 80 samples of women, using the weighted average where each unit `i` is weighted by `1/P(i being sampled)`


{% include lib/mathjax.html %}
