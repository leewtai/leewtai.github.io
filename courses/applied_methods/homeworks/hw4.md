# Homework3 - Preparing for your final project

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
corr_noise <- L %*% noise
mean_fun <- function(locs){locs[, 1] + locs[, 2] * 3}
y <- mean_fun(locations) + corr_noise 

# VISUALIZATION CODE GOES HERE

# Part 2
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


{% include lib/mathjax.html %}
