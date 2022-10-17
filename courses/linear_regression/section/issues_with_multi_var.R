set.seed(28)
n <- 100
p <- 5
X <- cbind(rep(1, n),
           matrix(runif(n * (p - 1), 0, 5), nrow=n))
beta <- runif(p, -10, 10)
eps <- rnorm(n, sd=2)
Y <- X %*% beta + eps

# Visualize the marginal relationship
par(mfrow=c(1, 2))
for(i in seq_len(p-1)){
    plot(X[, i + 1], Y,
         main=paste("Corr ", round(cor(X[, i + 1], Y), 2)))
}

# How to visualize the conditional relationship, look at residuals after regressing on other X




# Do no harm?

n <- 100
p <- 2
x <- runif(n, 0, 4)
beta <- c(2, 2)
eps <- rnorm(n)
Y <- beta[1] + x * beta[2] + eps


# Add "m" bad features, once with m=5, then m=50





