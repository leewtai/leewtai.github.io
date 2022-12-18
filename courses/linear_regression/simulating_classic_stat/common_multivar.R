# Simulate the simultaneous inference problem (issues with multi-variate regression)

n <- 1000
p <- 10
x <- matrix(rnorm(n * (p - 1)), nrow=n, ncol = p-1)
X <- cbind(1, x)
# all features SHOULD fail to reject
betas <- rep(0, p)
errors <- rnorm(n)

made_a_mistake <- c()
sim_num <- 1000
for(i   in   seq_len(sim_num)){
    errors <- rnorm(n)
    y <- X %*% betas + errors
    
    mod <- lm(y ~ x)

    summ_tab <- summary(mod)$coefficients

    # fraction of features we rejected beta is 0
    made_a_mistake[i] <- any(summ_tab[, 4] < (0.05 / p))
}
mean(made_a_mistake)

# Bonferroni is correct and requires no assumptions
# but very impractical in real life (There's an alternative)
# 
# Trick: change the question!
# False discovery rate (i.e. we tolerate a minium number of mistakes)

# p by default is the number of coefficients.
# in reality, this should be the number of hypothesis tests you're running
# in social science, you often only care about a small subset of feature
# most other faetures are "controls"

# "control" means adding a variable into the regression, where the variable
# can explain the variability in y, but is not of interest to the research
# e.g. gender's effect on salary is the research interest, but we need
# to control for tenure + job title at the job


# each hypothesis test, given all features are indep
# the fraction (excluding intercept) should approach 5% false positive
# consistent with past learnings


# data source - Kaggle
# https://www.kaggle.com/datasets/hellbuoy/car-price-prediction

df <- read.csv("~/Downloads/CarPrice_Assignment.csv")
# For the sake of saving time in class, let's focus on a few variables
sdf <- df[, c('price', 'citympg', 'horsepower', 'fueltype', 'carbody', 'CarName')]

# Levels are set arbitrarily
sdf[['fueltype']] <- factor(sdf$fueltype, levels=c('gas', 'diesel'))
# sdf[['fueltype']] <- as.factor(sdf$fueltype)
sdf[['carbody']] <- as.factor(sdf$carbody)
sdf[['brand']] <- as.factor(sub('([^ ]+) .*', '\\1', sdf$CarName))

# Indicators / membership variables
mod <- lm(price ~ fueltype + carbody, sdf)
summary(mod)

# good default for newdata
newdata <- sdf
# To detect the effect of fueltype = gas!
newdata[['fueltype']][newdata$fueltype != 'gas'] <- 'gas'
yhat_gas <- predict(mod, newdata = newdata)
newdata[['fueltype']][newdata$fueltype != 'diesel'] <- 'diesel'
yhat_diesel <- predict(mod, newdata = newdata)
mean(yhat_diesel - yhat_gas) # average "treatment" effect!
# by average the difference, i'm aggregating over all possible factors not manipulated
sd(yhat_diesel - yhat_gas)




# the interpretation of the intercept, is the predicted value
# for the "default" class, i.e. the class that is left out
# by all other membership variables.
# I recommend, to always compute y_hat
newdata <- sdf[1, ]

y_hat <- predict(mod, newdata=newdata)
# always calculate y_hat using predict() to get the effect of overall
# impact from different coefficients

# polynomials
sdf['citympg2'] <- sdf$citympg^2
mod <- lm(price ~ citympg, sdf)
summary(mod)
mod2 <- lm(price ~ citympg + citympg2, sdf)
summary(mod2)


# Interactions

## Adding all possible interactions and "main effects"
mod <- lm(price ~ citympg * carbody, sdf)
summary(mod)
head(model.matrix(~ citympg * carbody, sdf))
newdata <- sdf
newdata[['carbody']][newdata$carbody != 'convertible'] <- 'convertible'
yhat_convt <- predict(mod, newdata)
newdata[['carbody']][newdata$carbody != 'sedan'] <- 'sedan'
yhat_sedan <- predict(mod, newdata)
head(yhat_sedan - yhat_convt)
mean(yhat_sedan - yhat_convt)

# "counterfactual"
original_yhat <- predict(mod, sdf)

## Adding only interactions
mod <- lm(price ~ citympg : carbody, sdf)
summary(mod)

