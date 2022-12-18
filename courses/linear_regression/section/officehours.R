n <- 50
cat_variable <- c('A', 'B', 'C')
group <- factor(sample(cat_variable, n, replace=TRUE), levels=cat_variable)
y <- rnorm(n)

X_sans_int <- model.matrix(~group - 1)
X <- cbind(1, X_sans_int)
mod <- lm(y ~ group - 1)
mod2 <- lm(y ~ X - 1)

# Why can't the different categories, have average 0?
# BA MA and PHD, these must center 0

# Example:
# Case 1: (center is not 0 across the coefficients for the categories)
# Base: 80K, BA + 0, MA + 10k, PhD + 20K
# Case 2 (forcing the center to be 0, i.e. beta1 + beta2 + beta3 = 0, this is an extra constraint!)
# Base: 90K (beta0), BA -10k (beta1), MA + 0k (beta2), PhD + 10K (beta3)
### This is done in a model called random effects model!
### This is an extra constraint on a collection of betas!

