n <- 100
p <- 5

x <- matrix(rnorm(n * (p - 1)), nrow=n, ncol=p-1)
X <- cbind(1, x)
betas <- rep(0, p)
betas[2] <- runif(1, -2, -1)
errors <- rnorm(n)
y <- X %*% betas + errors


k <- 10
folds <- sample(k, n, replace=TRUE)

i <- 1
is_train <- folds == i
is_test <- !is_train

df <- as.data.frame(cbind(x, y))
train_df <- df[is_train, ]
test_df <- df[is_test, ]

mod <- lm(y ~ ., train_df)
y_hat <- predict(mod, newdata = test_df)
new_error <- (test_df$y - y_hat)


