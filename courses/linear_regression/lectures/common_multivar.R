# data source - Kaggle
# https://www.kaggle.com/datasets/hellbuoy/car-price-prediction

df <- read.csv("~/Downloads/CarPrice_Assignment.csv")
# For the sake of saving time in class, let's focus on a few variables
sdf <- df[, c('price', 'citympg', 'horsepower', 'fueltype', 'carbody', 'CarName')]

# Levels are set arbitrarily
# sdf[['fueltype']] <- factor(sdf$fueltype, levels=c('gas', 'diesel'))
sdf[['fueltype']] <- as.factor(sdf$fueltype)
sdf[['carbody']] <- as.factor(sdf$carbody)
sdf[['brand']] <- as.factor(sub('([^ ]+) .*', '\\1', sdf$CarName))

# Indicators / membership variables
mod <- lm(price ~ fueltype + carbody, sdf)
summary(mod)


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

## Adding only interactions
mod <- lm(price ~ citympg : carbody, sdf)
summary(mod)

