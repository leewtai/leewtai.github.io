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

par(mfrow=c(1, 2))
x <- rnorm(100)
y <- x + rnorm(100, sd=0.7)
plot(x, y, main="Regression line")
abline(lm(y~x), col="red")
plot(x, y, main="SD line")
abline(a=0, b=sd(y)/sd(x), col="blue")

par(mfrow=c(1, 2))
plot(x, y, main="Regression line")

abline(lm(y~x), col="red")

par(mfrow=c(1, 1))
plot(x, y)
mod <- lm(y~x)
abline(mod)
y_pred <- sum(mod$coefficients * c(1, x[1]))
segments(x[1], y[1], x[1], y_pred, col="red")


par(mfrow=c(1, 2))
x <- runif(100, max=2)
y <- (x)^2 + rnorm(100, sd=0.7)
plot(x, y)
mod <- lm(y~x)
#abline(mod)
#segments(x, y, x, mod$fitted.values, col="red")
plot(x, mod$residuals, col="red", pch=16,
     main="residual plot")
abline(h=0)


df <- read.csv("~/Downloads/titanic.csv")
hist(df$Fare, main="Distribution of Titanic Fare", xlab="Fare")


n <- 20
x <- 0:20
px <- dbinom(x, size = n, prob=0.5)
plot(x, px)



x <- 0:20
plot(x,
     dhyper(x, 45, 55, 20))


exps <- c(-5, 0, 5)
sds <- c(1, 3)
png("normal_tuning.png", 1200, 500)
par(mfcol=c(2, 3))
for(e in exps){
  for(s in sds){
    curve(dnorm(x, e, s), -20, 20,
          main=paste("Exp is:", e, "SE^2 is:", s^2),
          cex.main=2)
  }
}
dev.off()

n <- 25
png("3_distributions.png", 400, 1000)
par(mfrow=c(3, 1))
curve(dexp(x, 0.03), 0, 150, main="Population")
abline(v = 1/0.03, col="black", lwd=3)
legend("topright", fill="black", legend="Population Mean", cex=2)
y <- rexp(n, 0.03)
hist(y, main=paste(n, "Samples from Population"),
     xlab="", ylab="", breaks = 20, xlim=c(0, 150))
abline(v = 1/0.03, col="black", lwd=3)
abline(v = mean(y), col="red", lwd=3)
legend("topright", fill=c("black", "red"),
       legend=c("Population Mean", "Sample Mean"), cex=2)
curve(dnorm(x, 1/0.03, sqrt(1/0.03^2) / sqrt(n)), 0, 150)
abline(v = 1/0.03, col="black", lwd=3)
abline(v = mean(y), col="red", lwd=3)
legend("topright", fill=c("black", "red"),
       legend=c("Population Mean", "Sample Mean"),
       cex=2)
dev.off()


png("3_distributions_exp.png", 400, 1000)
par(mfrow=c(3, 1))
curve(dexp(x, 0.03), 0, 150, main="Population")
abline(v = 1/0.03, col="black", lwd=3)
legend("topright", fill="black", legend="Population Mean", cex=2)
y1 <- rexp(25, 0.03)
y2 <- rexp(25, 0.03)
h1 <- hist(y1, plot=FALSE, freq = FALSE)
h2 <- hist(y2, plot=FALSE, freq=FALSE)
plot(h1, col="#AA000066", main="Two Sets of Samples from the Same Box")
plot(h2, col="#0000AA66", add=TRUE)
abline(v=mean(y1), col="red")
abline(v=mean(y2), col="blue")
legend("topright", fill=c("red", "blue"),
       legend=c("Sample 1 Mean", "Sample 2 Mean"), cex=2)
curve(dnorm(x, 0, sqrt(1/0.03^2/ n + 1/0.03^2 / n)), -50, 50,
      main="Difference in Sample Avgs")
abline(v = 0, col="black", lwd=3)
abline(v = mean(y1) - mean(y2), col="red", lwd=3)
legend("topright", fill=c("black", "red"),
       legend=c("Expected Diff from Null", "Diff in Sample Means"),
       cex=1.5)
dev.off()

