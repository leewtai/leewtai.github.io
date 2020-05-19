# Exercise 1, check if 
n <- 100
num_sim <- 1000
outcome <- rep(NA, num_sim)

for(i in 1:num_sim){
    new_data <- rnorm(n, 0, 5)
    y_avg <- mean(new_data)
    # In class I forgot the sqrt(n-1) factor!
    y_se <- sd(new_data) / sqrt(n)
    stat <- abs(y_avg / y_se)
    outcome[i] <- stat >= 1.96
}

mean(outcome)
# We should expect this to surround 
2 * pt(-1.96, n-1)
# If we did not estimate y_se, i.e. y_se = 5 / sqrt(n) then we would expect
2 * pnorm(-1.96)



# Exercise 2, is the median a better estimate than the avg for E(Y)
# When Y~Normal(0, 5^2)
bad_est <- function(x){
    if(sample(c(TRUE, FALSE), 1)){
        out <- quantile(x, 0.75)
    }else{
        out <- quantile(x, 0.25)
    }
    return(out)
}
n <- 100
num_sim <- 1000
outcome <- matrix(NA, nrow=num_sim, ncol=3)
true_mean = 0
for(i in 1:num_sim){
    new_data <- rnorm(n, true_mean, 5)
    outcome[i, 1] <- mean(new_data)
    outcome[i, 2] <- median(new_data)
    outcome[i, 3] <- bad_est(new_data)
}

x_range <- range(outcome)
par(mfrow=c(1, 3))
hist(outcome[, 1], xlim=x_range, main="avg")
hist(outcome[, 2], xlim=x_range, main="med")
hist(outcome[, 3], xlim=x_range, main="bad")

# Not recommended
abs(apply(outcome, 2, mean) - true_mean)
# Better
apply(outcome, 2, function(x) mean(abs(x - true_mean)))
apply(outcome, 2, function(x) mean((x - true_mean)^2))

