x <- rep(c(153, 161, 170, 197, 230, 255, 280), c(10, 5, 10, 25, 25, 10, 15))
hist(x, breaks = c(0, 154.4, 161.9, 170.7, 197.3, 230.1, 255.6, 300),
     xlab="Weight in lbs")
abline(v=180, col="red")

setwd("~/repos/leewtai.github.io/usecases_data/nyc_opendata/")
list.files()



par(mfrow=c(2, 2))
x <- rbinom(100, 1, 0.5)
y <- rnorm(100, mean=x)

boxplot(y ~ x)

x <- rbinom(100, 1, 0.5)
y <- rnorm(100, sd=x + 0.3)
boxplot(y ~ x)

x <- runif(100, min=-1)
y <- x ^2 + rnorm(100, sd=0.3)
plot(x, y)

x <- runif(100, min=-1)
y <- rnorm(100, sd=0.3)
plot(x, y)


par(mfrow=c(1, 2))
x <- runif(100, min=-1)
y <- x + rnorm(100, sd=0.3)
plot(x, y, main=paste("Corr is", round(cor(x, y), 2)))
x <- runif(100, min=-1)
y <- -x + rnorm(100, sd=0.9)
plot(x, y, main=paste("Corr is", round(cor(x, y), 2)))

x <- runif(100, min=-1)
y <- x^2 + rnorm(100, sd=0.1)
plot(x, y, main=paste("Corr is", round(cor(x, y), 2)))
x <- runif(100, min=-1)
y <- x + rnorm(100, sd=0.3)
x1 <- c(x, -1)
y1 <- c(y, 20)
plot(x1, y1, main=paste("Corr is", round(cor(x1, y1), 2)))


x <- rnorm(100)
y <- x + rnorm(100, sd=0.7)
plot(x, y, main=paste("Corr is", round(cor(x, y), 2)))
points(x, )