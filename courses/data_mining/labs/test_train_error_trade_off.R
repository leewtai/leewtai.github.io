n <- 100
degrees <- 1:50

X <- runif(n, max=2 * pi / 4 * 3)
Y <- 0.1 + -3 * sin(X) + rnorm(n, sd=0.5)
new_Y <- 0.1 + -3 * sin(X) + rnorm(n, sd=0.5)
X_mat <- sapply(degrees, function(i) X^i)


MSEs <- rep(NA, length(degrees))
test_MSEs <- MSEs
for(i in seq_along(degrees)){
  ols <- lm(Y ~ X_mat[, 1:i])
  MSEs[i] <- mean(ols$residuals^2)
  new_errors <- new_Y - ols$fitted.values
  test_MSEs[i] <- mean(new_errors^2)
}
plot(degrees, MSEs, type="b",
     ylim=c(0, max(test_MSEs)))
lines(degrees, test_MSEs, type="b", col="red")
legend("topright", legend=c("Test", "Train"),
       fill=c("red", "black"))

plot(X, new_Y)
points(X, ols$fitted.values, col="red")


ols <- lm(Y ~ X_mat)

df <- data.frame(Y, X_mat)
ols <- lm(Y ~ ., df)

ols <- lm(Y ~ X_mat[, 1]:X_mat[, 2])
ols <- lm(Y ~ X_mat[, 1]*X_mat[, 2])
summary(ols)
