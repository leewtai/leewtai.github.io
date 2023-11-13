# Here are the example DAGs

## Ideal regression case
n <- 100
X <- rnorm(n, sd=0.4)
Z <- rnorm(n)
Y <- X + Z + rnorm(n)
summary(lm(Y~X))
summary(lm(Y~ X + Z))

## Colliders
n <- 100
X <- rnorm(n)
Y <- rnorm(n)
Z <- X + Y + rnorm(n)

summary(lm(Y ~ X))
summary(lm(Y ~ X + Z))


## Mediators
n <- 100
X <- rnorm(n)
Z <- 2 * X + rexp(n, rate=0.2)
Y <- 1 - 4 * Z + rnorm(n, sd=2)

summary(lm(Y ~ X))
summary(lm(Y ~ X + Z))

## Confounders
n <- 100
Z <- rexp(n, rate=0.2)
X <- Z + rnorm(n)
Y <- 1 - 4 * Z + rnorm(n, sd=2)
