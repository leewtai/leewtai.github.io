setwd("~/repos/leewtai.github.io/courses/intro-stat/")

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
plot(x, y, main=paste("Corr is", round(cor(x, y), 2)))
points(x, )



#### Demonstrating different sampling methods!
k <- 10
N <- k^2
x <- 0:9
y <- 0:9
xy <- expand.grid(x, y)
set.seed(18)
cols <- sample(rep(c("white", "black"), times=c(N * 0.9, N * 0.1)))
png("srs.png", 300, 350)
plot(1, 1, type="n", xlim=c(0, 10), ylim=c(0, 10), xaxt="n", yaxt="n", xlab="", ylab="")
rect(xy[, 1], xy[, 2], xy[, 1]+1, xy[, 2] + 1, col=cols)
dev.off()

png("srs_challenge.png", 300, 350)
plot(1, 1, type="n", xlim=c(0, 10), ylim=c(0, 10), xaxt="n", yaxt="n", xlab="", ylab="")
rect(xy[, 1], xy[, 2], xy[, 1]+1, xy[, 2] + 1, col=cols)
subxy <- cbind(c(0, 0, 5, 5, 0), c(4, 10, 10, 4, 4))
for(i in 1:4){
    segments(subxy[i, 1], subxy[i, 2], subxy[i + 1, 1], subxy[i + 1, 2], col="red",
             lwd=3)
}
dev.off()

png("strat_prep.png", 300, 350)
plot(1, 1, type="n", xlim=c(0, 10), ylim=c(0, 10), xaxt="n", yaxt="n", xlab="", ylab="")
rect(xy[, 1], xy[, 2], xy[, 1]+1, xy[, 2] + 1)
subxy <- cbind(c(0, 0, 5, 5, 0), c(4, 10, 10, 4, 4))
for(i in 1:4){
  segments(subxy[i, 1], subxy[i, 2], subxy[i + 1, 1], subxy[i + 1, 2], col="red",
           lwd=3)
}
dev.off()

set.seed(10)
png("strat_prep1.png", 300, 350)
sub1 <- xy[, 1] <= 4 & xy[, 2] >= 4
cols <- rep("white", 100)
cols[sample(which(sub1), 3)] <- "black"
plot(1, 1, type="n", xlim=c(0, 10), ylim=c(0, 10), xaxt="n", yaxt="n", xlab="", ylab="")
rect(xy[, 1], xy[, 2], xy[, 1]+1, xy[, 2] + 1, col=cols)
subxy <- cbind(c(0, 0, 5, 5, 0), c(4, 10, 10, 4, 4))
for(i in 1:4){
  segments(subxy[i, 1], subxy[i, 2], subxy[i + 1, 1], subxy[i + 1, 2], col="red",
           lwd=3)
}
dev.off()

png("strat_prep2.png", 300, 350)
sub1 <- xy[, 1] <= 4 & xy[, 2] >= 4
cols[sample(which(!sub1), 7)] <- "black"
plot(1, 1, type="n", xlim=c(0, 10), ylim=c(0, 10), xaxt="n", yaxt="n", xlab="", ylab="")
rect(xy[, 1], xy[, 2], xy[, 1]+1, xy[, 2] + 1, col=cols)
subxy <- cbind(c(0, 0, 5, 5, 0), c(4, 10, 10, 4, 4))
for(i in 1:4){
  segments(subxy[i, 1], subxy[i, 2], subxy[i + 1, 1], subxy[i + 1, 2], col="red",
  lwd=3)
}
dev.off()


png("clust_prep.png", 300, 350)
plot(1, 1, type="n", xlim=c(0, 10), ylim=c(0, 10), xaxt="n", yaxt="n", xlab="", ylab="")
rect(xy[, 1], xy[, 2], xy[, 1]+1, xy[, 2] + 1)
for(j in 0:9){
    subxy <- cbind(j + c(0, 0, 1, 1, 0), c(0, 10, 10, 0, 0))
    for(i in 1:4){
      segments(subxy[i, 1], subxy[i, 2], subxy[i + 1, 1], subxy[i + 1, 2], col="red",
               lwd=3)
    }
}
dev.off()

cols <- rep("white", 100)
png("clust_prep1.png", 300, 350)
plot(1, 1, type="n", xlim=c(0, 10), ylim=c(0, 10), xaxt="n", yaxt="n", xlab="", ylab="")
cols[seq(7, 100, by =10)] <- "black"
rect(xy[, 1], xy[, 2], xy[, 1]+1, xy[, 2] + 1, col=cols)
for(j in 0:9){
  subxy <- cbind(j + c(0, 0, 1, 1, 0), c(0, 10, 10, 0, 0))
  for(i in 1:4){
    segments(subxy[i, 1], subxy[i, 2], subxy[i + 1, 1], subxy[i + 1, 2], col="red",
             lwd=3)
  }
}
dev.off()


xx <- rnorm(10000, 50, 10) + rexp(10000, 1/50)
png("inference-basic.png", 500, 300)
par(mfrow=c(1, 1))
plot(density(xx), xlab="", ylab="",yaxt="n", xlim=c(0, 500), main="Population")
abline(v=mean(xx), col="red")
dev.off()

png("inference-basic1.png", 1000, 600)
par(mfrow=c(2, 3))
for(i in 1:6){
  xxx <- sample(xx, 100)
  hist(xxx, xlab="X", ylab="", yaxt="n", main="100 Samples from the Population", xlim=c(0, 500))
  abline(v=mean(xxx), col="red")
  if(i == 6){
      legend("topright", legend="mean", fill="red")
  }
}
dev.off()

n <- 20
x <- 0:n
px <- dbinom(x, n, 0.5)
png("binomial.png")
plot(x, px, xlab="Possible Total", ylab="Probability", main="Binomial Distribution",
     pch=16, col="red")
dev.off()


png("binomial_param.png", 1200, 600)
par(mfrow=c(2, 4))
for(ni in c(10, 100)){
  for(pi in c(0.1, 0.4, 0.6, 0.9)){
    x <- 0:ni
    px <- dbinom(x, ni, pi)
    plot(x, px, xlab="Possible Total", ylab="Probability",
         main=paste0("Draws = ", ni, "; Prob(H) = ", pi),
         pch=16, col="red",
         cex.main=2, cex=2)
=======
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

png("expectations.png", 1000, 300)
par(mfrow=c(1, 3))
curve(dnorm(x), -4, 4, main="Normal(0, 1)", cex.main=2)
abline(v=0, col="red")
curve(dexp(x), 0, 5, main="Exponential(1)", cex.main=2)
abline(v=1, col="red")
curve(dbeta(x, 0.5, 0.4), 0, 1, main="Beta(0.5, 0.4)", cex.main=2)
abline(v=0.5 / 0.9, col="red")
dev.off()

png("lln_text.png")
par(mar=c(5, 6, 6, 1))
plot(1, 1, type="n", xlab="Number of Trials", ylab="Sample Mean",
     xlim=c(0, max(ns)), ylim=c(0, 1), cex.lab=2, main="LLN Demo",
     cex.main=2)
p <- 0.3
for(col in c("red", "blue", "purple", "green", "grey")){
  
  ns <- c(1, 2, 3, 10, 50, 100, 250, 500, 1000)
  sample_data <- rbinom(max(ns), 1, p)
  sample_means <- sapply(ns, function(n) mean(sample_data[1:n]))
  points(ns, sample_means, type="b", col=col, pch=16)

}
abline(h = p, col="black", lwd=2)
dev.off()


png("finite_bernoulli.png")
ni <- 250
x <- sapply(1:9000, function(x) mean(rbinom(ni, size=1, p=0.3)))
hist(x, xlab="Possible Value")
dev.off()


png("lln_text_exp.png")
par(mar=c(5, 6, 6, 1))
plot(1, 1, type="n", xlab="Number of Trials", ylab="Sample Mean",
     xlim=c(0, max(ns)), ylim=c(0, 0.5), cex.lab=2, main="LLN Demo",
     cex.main=2)
p <- 0.3
for(col in c("red", "blue", "purple", "green", "grey")){
  
  ns <- c(1, 2, 3, 10, 50, 100, 250, 500, 1000)
  sample_data <- rexp(max(ns), 1/p)
  sample_means <- sapply(ns, function(n) mean(sample_data[1:n]))
  points(ns, sample_means, type="b", col=col, pch=16)
  
}
abline(h = p, col="black", lwd=2)
dev.off()


png("finite_exponential.png")
ni <- 250
x <- sapply(1:9000, function(x) mean(rexp(ni, 0.3)))
hist(x, xlab="Possible Value")
dev.off()


ns <- c(3, 25, 100)
png("clt.png", 1500, 800)
par(mfrow=c(2, 4))
curve(dexp(x, 1/20), 0, 20, main="Distr of Exponential R.V.", cex.main=2)
for(ni in ns){
  means <- sapply(1:1000, function(x) mean(rexp(ni, 1/20)))
  hist(means, xlab="", ylab="", main=paste("Sample Mean of", ni, "Exp R.V."), cex.main=2)
}
curve(dbinom(x, 1, 0.3), 0, 1, main="Distr of Bernoulli R.V.", lwd=3, cex.main=2)
for(ni in ns){
  means <- sapply(1:1000, function(x) mean(rbinom(ni, 1, 0.3)))
  hist(means, xlab="", ylab="", main=paste("Sample Mean of", ni, "Bernoulli R.V."), cex.main=2)
}
dev.off()

png("clt2.png", 1500, 800)
par(mfrow=c(2, 4))
curve(dunif(x, -5, 5), -5.2, 5.2, main="Distr of Uniform R.V.", cex.main=2)
for(ni in ns){
  means <- sapply(1:1000, function(x) mean(runif(ni, -5, 5)))
  hist(means, xlab="", ylab="", main=paste("Sample Mean of", ni, "Uniform R.V."), cex.main=2)
}
curve(dbinom(x, 50, 0.3), 0, 50, main="Distr of Binomial R.V.", lwd=3, cex.main=2)
for(ni in ns){
  means <- sapply(1:1000, function(x) mean(rbinom(ni, 50, 0.3)))
  hist(means, xlab="", ylab="", main=paste("Sample Mean of", ni, "Binomial R.V."), cex.main=2)
}
dev.off()

png("normal_density.png")
curve(dnorm(x), -4, 4, xlab="", ylab="", xaxt="n",
      main="Normal(E(Y), SE(Y)^2 / n)")
dev.off()

png("normal_density.png")
plot(1, 1, type="n", xlim=c(-4, 4), ylim=c(0, 0.5))
x <- seq(-4, -3, by=0.02)
y <- rep(0, length(x))
y <- c(y, dnorm(rev(x)))
x <- c(x, rev(x))
polygon(x, y, col="red")
x <- seq(3, 4, by=0.02)
y <- rep(0, length(x))
y <- c(y, dnorm(rev(x)))
x <- c(x, rev(x))
polygon(x, y, col="red")
x <- seq(2, 3, by=0.02)
y <- rep(0, length(x))
y <- c(y, dnorm(rev(x)))
x <- c(x, rev(x))
polygon(x, y, col="blue")
x <- seq(-3, -2, by=0.02)
y <- rep(0, length(x))
y <- c(y, dnorm(rev(x)))
x <- c(x, rev(x))
polygon(x, y, col="blue")
x <- seq(-2, -1, by=0.02)
y <- rep(0, length(x))
y <- c(y, dnorm(rev(x)))
x <- c(x, rev(x))
polygon(x, y, col="green")
x <- seq(1, 2, by=0.02)
y <- rep(0, length(x))
y <- c(y, dnorm(rev(x)))
x <- c(x, rev(x))
polygon(x, y, col="green")
x <- seq(-1, 1, by=0.01)
y <- rep(0, length(x))
y <- c(y, dnorm(rev(x)))
x <- c(x, rev(x))
polygon(x, y, col="grey")
dev.off()

png("sampling_dist_under_null.png", 800, 500)
curve(dnorm(x, 0, 1.94), -6, 6,
      ylab="", xlab="Possible Test Stat",
      main="Null Distribution",
      cex.main=2, cex.lab=2)
abline(v=0, col="black", lwd=3)
abline(v=-1.94, col="grey", lwd=3)
abline(v=1.94, col="grey", lwd=3)
abline(v=-1.94*2, col="green", lwd=3)
abline(v=1.94*2, col="green", lwd=3)
abline(v=-1.94*3, col="blue", lwd=3)
abline(v=1.94*3, col="blue", lwd=3)
dev.off()

png("sampling_dist_under_null2.png", 800, 500)
curve(dnorm(x, 0, 1.94), -6, 6,
      ylab="", xlab="Possible Test Stat",
      main="Null Distribution",
      cex.main=2, cex.lab=2)
abline(v=0, col="black", lwd=3)
abline(v=-1.94, col="grey", lwd=3)
abline(v=1.94, col="grey", lwd=3)
abline(v=-1.94*2, col="green", lwd=3)
abline(v=1.94*2, col="green", lwd=3)
abline(v=-1.94*3, col="blue", lwd=3)
abline(v=1.94*3, col="blue", lwd=3)
abline(v=-3, col="red", lwd=3)
legend("topleft", fill="red", legend="Observed Test Stat = -3", cex=2)
dev.off()


png("sampling_dist_under_null_std.png", 800, 500)
curve(dnorm(x, 0, 1), -3, 3,
      ylab="", xlab="Possible Std Test Stat",
      main="Std Null Distribution",
      cex.main=2, cex.lab=2)
abline(v=0, col="black", lwd=3)
abline(v=-1, col="grey", lwd=3)
abline(v=1, col="grey", lwd=3)
abline(v=-2, col="green", lwd=3)
abline(v=2, col="green", lwd=3)
abline(v=-3, col="blue", lwd=3)
abline(v=3, col="blue", lwd=3)
abline(v=-3 / 1.94, col="red", lwd=3)
legend("topleft", fill="red", legend="Std Observ Test Stat = (-3 - 0) / 1.94",
       cex=2)
dev.off()

png("sampling_dist_under_null_std_p_val.png", 800, 500)
curve(dnorm(x, 0, 1), -3, 3,
      ylab="", xlab="Possible Std Test Stat",
      main="Std Null Distribution",
      cex.main=2, cex.lab=2)
curve(dnorm(x, 0, 1), -3, -3 / 1.94, fill="red")
abline(v=0, col="black", lwd=3)
abline(v=-1, col="grey", lwd=3)
abline(v=1, col="grey", lwd=3)
abline(v=-2, col="green", lwd=3)
abline(v=2, col="green", lwd=3)
abline(v=-3, col="blue", lwd=3)
abline(v=3, col="blue", lwd=3)
abline(v=-3 / 1.94, col="red", lwd=3)
legend("topleft", fill="red", legend="Std Observ Test Stat = (-3 - 0) / 1.94",
       cex=2)
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




curve(dexp(x, .3), 0, 10, ylab="", main="Exponential(0.3)",
      xlab="Possible Values")
ev <- 1/.3
abline(v=ev)
png("confidence_interval.png", 1200, 600)
par(mfcol=c(2, 3))
for(n in c(5, 20, 100)){
  for(sig_lvl in c(0.95, 0.8)){
  sim_num <- 100
  plot(0, 0, type="n", xlim=c(0, 10),
       ylim=c(0, sim_num+1), ylab="", yaxt="n",
       xlab="",
       main=paste("n =", n, "Sig Lvl=", sig_lvl * 100, "%"),
       cex.main=2)
  abline(v=ev)
  for(i in 1:sim_num){
    #interval <- confint(lm(runif(n, -5, 5)~1))
    interval <- confint(lm(rexp(n, .3)~1))
    if(interval[1] > ev | interval[2] < ev){
      col <- "red"
    } else {
      col <- "black"
    }
    segments(interval[1], i, x1=interval[2], i,
             col=col)
  }
  }  
}
dev.off()


dfs <- c(1, 3)
sig_lvls <- c(0.1, 0.05, 0.01)
i <- 1
j <- 1
png("chi-sq-p-vals.png", 1800, 1000)
par(mfrow=c(2, 3))
for(i in seq_along(dfs)){
  for(j in seq_along(sig_lvls)){
    curve(dchisq(x,dfs[i]), xlim=c(0, 30),
          xlab="Chi-Square Stat", ylab="",
          main=paste("Deg Freedom:", dfs[i], "Sig Lvl:", sig_lvls[j]),
          cex.main=3.5, cex.lab=2)
    x <- seq(qchisq(1 - sig_lvls[j], dfs[i]), 30, length.out=100)
    y <- dchisq(x, dfs[i])
    x <- c(x, rev(x))
    y <- c(y, rep(0, length(y)))
    polygon(x, y, col="red")
    legend("topright", legend=paste("Cutoff:", round(qchisq(1 - sig_lvls[j], dfs[i]), 2)), fill="red",
           cex=3)
  }
}
dev.off()

png("alt_is_true.png", 800, 500)
par(mfrow=c(1, 2))
curve(dnorm(x), -5, 5, col="red", ylab="",
      main="Sample Avg Distr", xlab="Possible Sample Avg")
curve(dnorm(x, mean=0.1), -5, 5, col="blue", add=TRUE)
legend("topleft", legend=c("Treatment", "Control"),
       fill=c("red", "blue"),
       cex=1)
curve(dnorm(x), -5, 5, col="red", ylab="",
      main="Sample Avg Distr", xlab="Possible Sample Avg")
curve(dnorm(x, mean=3), -5, 5, col="blue", add=TRUE)
legend("topleft", legend=c("Treatment", "Control"),
       fill=c("red", "blue"),
       cex=1)
dev.off()


theta1 <- 0
theta2 <- 0.1
x_max <- 5
y1 <- rexp(100, rate = theta1)
y2 <- rexp(100, rate = theta2)
par(mfrow=c(1, 2))
curve(dexp(x, rate=1/theta1), xlim=c(0, x_max))
curve(dexp(x, rate=1/theta2), xlim=c(0, x_max))


x_max <- 5
png("power1.png", 800, 600)
curve(dnorm(x, 0), xlim=c(-x_max, x_max), col="purple",
      xlab="Possible Std Diff in Avg", ylab="",
      main="Null Distr",
      cex.main=2, cex.lab=2)
x <- seq(-5, -2.5, length.out = 100)
y <- dnorm(x)
y <- c(y, rep(0, length(x)))
x <- c(x, rev(x))
polygon(x, y, col="red")
x <- seq(2.5, 5, length.out = 100)
y <- dnorm(x)
y <- c(y, rep(0, length(x)))
x <- c(x, rev(x))
polygon(x, y, col="red")
legend("topright", legend="< 0.05 ?", fill="red", cex=2)
dev.off()

x_max <- 5
png("power2.png", 800, 600)
curve(dnorm(x, 0), xlim=c(-x_max, x_max), col="purple",
      xlab="Possible Std Diff in Avg", ylab="",
      main="Null Distr",
      cex.main=2, cex.lab=2)
abline(v=2.5, col="red", lwd=3)
abline(v=-2, col="black", lwd=3)
abline(v=2, col="black", lwd=3)
legend("topleft", legend=c("Obs Std Test Stat", "k cutoff"),
       fill=c("red", "black"))
dev.off()


x_max <- 5
png("mde_demo.png", 1300, 400)
par(mfrow=c(1, 3))
curve(dnorm(x, 0), xlim=c(-x_max, x_max), col="purple",
      xlab="Possible Samp Avg", ylab="",
      main="Null Distr",
      cex.main=2)
curve(dnorm(x, 0), xlim=c(-x_max, x_max), col="blue",
      xlab="Possible Samp Avg", ylab="",
      main="Difference in Mean = MDE",
      cex.main=2)
curve(dnorm(x, 1), add=TRUE, col="red")
curve(dnorm(x, 0), xlim=c(-x_max, x_max), col="blue",
      xlab="Possible Samp Avg", ylab="",
      main="Difference in Mean > MDE",
      cex.main=2)
curve(dnorm(x, 2), add=TRUE, col="red")
dev.off()

d <- 3
png("p-val-vs-power.png", 1200, 500)
par(mfrow=c(1, 2))
curve(dnorm(x, 0), xlim=c(-x_max, x_max), col="purple",
      xlab="Std Diff in Samp Avg", ylab="",
      main="Getting p-values",
      cex.main=2, lwd=3)
curve(dnorm(x, d), col="orange", add=TRUE)
x <- seq(-5, -2, length.out = 100)
y <- dnorm(x)
y <- c(y, rep(0, length(x)))
x <- c(x, rev(x))
polygon(x, y, col="red")
x <- seq(2, 5, length.out = 100)
y <- dnorm(x)
y <- c(y, rep(0, length(x)))
x <- c(x, rev(x))
polygon(x, y, col="red")
legend("topleft", legend=c("Null", "MDE"),
       fill=c("purple", "orange"), cex=2)

curve(dnorm(x, 0), xlim=c(-x_max, x_max), col="purple",
      xlab="Std Diff in Samp Avg", ylab="",
      main="Getting Stat Power",
      cex.main=2)
curve(dnorm(x, d), col="orange", add=TRUE, lwd=3)
x <- seq(-5, -2, length.out = 100)
y <- dnorm(x, d)
y <- c(y, rep(0, length(x)))
x <- c(x, rev(x))
polygon(x, y, col="blue")
x <- seq(2, 5, length.out = 100)
y <- dnorm(x, d)
y <- c(y, rep(0, length(x)))
x <- c(x, rev(x))
polygon(x, y, col="blue")
legend("topleft", legend=c("Null", "MDE"),
       fill=c("purple", "orange"), cex=2)
dev.off()

png("power2.png", 800, 600)
curve(dnorm(x, 0), xlim=c(-x_max, x_max), col="purple",
      xlab="Std Diff in Samp Avg", ylab="",
      main="Determine Cutoff Using the Null",
      cex.main=2, lwd=3)
abline(v=2, lwd=3)
abline(v=-2, lwd=3)
legend("topleft", legend=c("Cutoff k"),
       fill="black")
dev.off()

png("power3.png", 800, 600)
curve(dnorm(x, 0), xlim=c(-x_max, x_max), col="purple",
      xlab="Std Diff in Samp Avg", ylab="",
      main="Get Stat Power by Area Under Altern Distr",
      cex.main=2, lwd=3)
abline(v=2, lwd=3)
abline(v=-2, lwd=3)
legend("topleft", legend=c("Cutoff k"),
       fill="black")
curve(dnorm(x, d), col="orange", add=TRUE, lwd=3)
x <- seq(-5, -2, length.out = 100)
y <- dnorm(x, d)
y <- c(y, rep(0, length(x)))
x <- c(x, rev(x))
polygon(x, y, col="blue")
x <- seq(2, 5, length.out = 100)
y <- dnorm(x, d)
y <- c(y, rep(0, length(x)))
x <- c(x, rev(x))
polygon(x, y, col="blue")
legend("topleft", legend=c("Cutoff k", "Stat Power"),
       fill=c("black", "blue"),
       cex=2)
dev.off()

x_min = -5
x_max = 8
d = 5
png("power-example3.png", 800, 600)
curve(dnorm(x, 0), xlim=c(x_min, x_max), col="purple",
      xlab="Std Diff in Samp Avg", ylab="",
      main="Fix Cutoff, Identify Altern Distr",
      cex.main=2, lwd=3)
abline(v=2, lwd=3)
abline(v=-2, lwd=3)
legend("topleft", legend=c("Cutoff k"),
       fill="black")
curve(dnorm(x, d / 0.95), col="orange", add=TRUE, lwd=3)

x <- seq(x_min, -2, length.out = 100)
y <- dnorm(x, d / 0.95)
y <- c(y, rep(0, length(x)))
x <- c(x, rev(x))
polygon(x, y, col="blue")
x <- seq(2, x_max, length.out = 100)
y <- dnorm(x, d/0.95)
y <- c(y, rep(0, length(x)))
x <- c(x, rev(x))
polygon(x, y, col="blue")
legend("topleft", legend=c("Cutoff k", "Stat Power"),
       fill=c("black", "blue"),
       cex=2)
abline(v=d/0.95, lwd=3, col="orange")

dev.off()

setwd("repos/leewtai.github.io/usecases_data/social_vulnerability/")
df <- read.csv("svi_census.csv")
df <- df[!is.na(df$pop_2014_20_24), ]
names(df)[1:5] <- c("geo_id", "pop_2014_20_24",
                    "pop_2018_20_24", "pop_2014_20_24_moe",
                    "pop_2018_20_24_moe")
df["pop_diff"] <- (df$pop_2018_20_24 - df$pop_2014_20_24) / df$pop_2014_20_24

setwd("~/repos/leewtai.github.io/courses/intro-stat/")
df <- read.csv("attempts_vs_midterm1.csv")
df <- df[df$pet != "Neither", ]
boxplot(df$Total ~ df$fame)
head(df)
df["diff"] <- df$count_post - df$count_pre
cond <- df$Total > 50
plot(df$Total[cond], df$diff[cond],
     pch=16, col="#00000055")
x2 <- df$Total^2

boxplot(df$Total ~ df$pet)
summary(lm(df$diff ~ df$Total + x2, subset=cond))

plot(df$count_pre, df$count_post,
     xlab=expression("Y_b"), ylab=expression("Y_a"),
     xlim=c(0, 10), ylim=c(0, 10),
     pch=16, col="#00000055",
     main="Attempts Before and After Midterm")
png("midterm.png")
hist(df$Total, xlab="Midterm Score %",
     main="Midterm Distribution")
dev.off()

png("midterm_by_fame.png")
boxplot(df$Total ~ df$fame,
        main="Midterm by Fame Preference", xlab="Preference for Fame",
        ylab="Midterm Score",
        cex=1.5)
dev.off()

png("fame_pet.png")
mosaicplot(table(df$fame, df$pet),
           main="Pet vs Fame Preference",
           cex=1.5)
dev.off()

png("hist3.png", 1200, 400)
par(mfrow=c(1, 3))
hist(df$count_post, xlab="Y_a", main="Distri of Y_a",
     cex.main=2)
hist(df$diff, xlab="Y_a - Y_b", main="Distri of Y_a - Y_b",
     cex.main=2)
hist(df$diff2, xlab="(Y_a - Y_b) / Y_b", main="Distri of (Y_a - Y_b) / Y_b",
     cex.main=2)
dev.off()