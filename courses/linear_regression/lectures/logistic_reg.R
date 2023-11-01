# Challenger dataset

df <- read.csv("~/Downloads/challenger.csv")
names(df)
df$is_stressed <- df$number_stressed > 0
mod <- lm(is_stressed ~ launch_temp_F, df)



# Maximum likelihood code
## Generate random mean (m) and sd (s) so we don't know the truth!
m <- rexp(1, 0.04)
s <- rexp(1, 0.04)
x <- rnorm(50, m, s)

# reasonable guesses
est_avg <- 1 / 0.04
est_sd <- 1 / 0.04

hist(x, freq=FALSE)
curve(dnorm(x, est_avg, est_sd),
            from=min(x),
            to=max(x),
            add=TRUE, col="blue")


# Logistic regression and link functions
df <- read.csv("challenger.csv")
x <- df$launch_temp_F
y <- df$is_stressed

logistic_reg <- glm(y ~ x, family = binomial(link="logit"))

logit = function(x, coefs=logistic_reg$coefficients) {
                 z <- cbind(1, x) %*% coefs
                 return(exp(z) / (1 + exp(z)))}

# Visualize the link function effect
plot(x, y, col="#00000033", pch=16)
curve(logit, from=min(x), to=max(x),
            add=TRUE, col="blue")


predict(logistic_reg)
