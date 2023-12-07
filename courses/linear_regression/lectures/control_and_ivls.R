# What does controlling for a variable mean?

n <- 500

k <- 2
groups <- sample(1:k, n, replace=TRUE)
x <- runif(n, max=5)

y <- -3 * groups + x * 2 * groups + rnorm(n)

groups_cat <- as.factor(groups)
plot(x, y)

# How would i visualize what this model does?
# will it model the two curves?
mod <- summary(lm(y ~ x + groups_cat))

# let's start simple
naive_mod <- lm(y ~ x)
poss_x_vals <- seq(0, 5, length.out=100)
ndf <- data.frame(x=poss_x_vals)
preds <- predict(naive_mod,
                 newdata=ndf)
plot(x, y)
points(poss_x_vals, preds, col="red")

mod <- lm(y ~ x + groups_cat )