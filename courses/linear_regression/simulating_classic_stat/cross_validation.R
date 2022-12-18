n <- 100
p <- 5

x <- matrix(rnorm(n * (p - 1)), nrow=n, ncol=p-1)
X <- cbind(1, x)
betas <- rep(0, p)
betas[2] <- runif(1, -2, -1)
errors <- rnorm(n)
y <- X %*% betas + errors

true_error <- y - X %*% betas
sum(true_error^2)
mod <- lm(y ~ x)
sum(mod$residuals^2) # training error, i.e. error from the dataset used to train the parameters
# observation: latter is ALWAYS less than the former, even though betas are the TRUE values!!!
# This is unsatisfying, b.c. we want the true parameters to minimize the error.

# True fact of all models (beyond regression)
# discrepancy: true parameters should minimize generalizationi error, not training error, b/c
# regression is derived based on minimizing the training error.

k <- 10
folds <- sample(k, n, replace=TRUE)

i <- 1
metrics <- matrix(NA, ncol=2, nrow=k)
# try out multiple folds! this is called k-fold cross validation
for(i in seq_len(k)){
    is_train <- folds != i
    head(is_train)
    is_test <- !is_train
    
    df <- as.data.frame(cbind(x, y))
    names(df)[ncol(df)] <- 'y'
    train_df <- df[is_train, ]
    test_df <- df[is_test, ]
    
    mod <- lm(y ~ ., train_df) # gives me model trained on a subset
    mod2 <- lm(y ~ . - V3, train_df) # gives me model trained on a subset
    y_hat <- predict(mod, newdata = test_df)
    y_hat2 <- predict(mod2, newdata = test_df)
    new_error <- (test_df$y - y_hat)
    new_error2 <- (test_df$y - y_hat2)
    
    # how to identify a good model? what's a good metric?
    # - 
    metrics[i, 1] <- sqrt(mean(new_error ^2)) # rmse, almost std deviation (not taking away mean)
    metrics[i, 2] <- sqrt(mean(new_error2 ^2)) # rmse, almost std deviation (not taking away mean)
}
apply(metrics, 2, mean) # average across k folds
# do no harm situations! (medical cases)
# worst case scenario
max(abs(new_error))
max(abs(new_error2))
# cross validation enables us to try out all kinds of metrics!


# stability over error rates
apply(metrics, 2, sd)
# stability over coefficients
# pull the coefficient of interest over the k-folds, then check its SD
