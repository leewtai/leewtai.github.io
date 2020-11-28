# Homework 7: Aggregated data and High Dimension Anomalies

## Weighted Least Squares
Let's create data at the individual level according to the linear regression model $$$$Y=X\beta + \epsilon$$$$ with the following specifications

- Let $$\epsilon_i\stackrel{ind}{\sim} Normal(0, 20)$$.
- Let the sample size, $$n$$, be 1000.
- Let $$\beta = \binom{0}{1.2}$$ (the first parameter is for the constant feature).
- let's assign each sample to 20 exclusive groups according to the following multinomial distribution: $$P(i\in$$ Group $$k) \propto \frac{1}{\sqrt{k}}$$ where $$k\in\{1, \dots, 20\}$$
- Define the non-constant feature, $$X_i\stackrel{ind}{\sim} Binomial(n=100, p=0.5), \forall i$$

Create the aggregated data by simply averaging the data points within each group for the $$X$$ and $$Y$$ values. Let's call these aggregated data values $$\bar{X}_k$$, and $$\bar{Y}_k$$. Let the vectorized version of the data be denoted as $$\bar{Y}$$ and let $$\bar{X} = \begin{bmatrix} 1 & \bar{X}_1 \\ \vdots & \vdots \\ 1 & \bar{X}_{20} \\\end{bmatrix}$$

#### Q0
TRUE/FALSE, the aggregated data will always have a higher correlation between X and Y than the correlation at the individual level. Note, ignore the constant feature.

#### Q1
TRUE/FALSE, $$\bar{Y} = \bar{X}\beta + \gamma$$ where $$\gamma$$ only depends on $$\epsilon$$

#### Q2
Let $$\gamma = \bar{Y} - \bar{X}\beta$$, TRUE/FALSE, $$E(\gamma|\bar{X}) = 0$$

#### Q3
What is the analytical expression for $$Var(\gamma_k|X)$$ and $$Cov(\gamma_k, \gamma_m|X)$$ where $$k\neq m$$. Please express the solution in terms of $$Var(\epsilon) = \sigma^2$$ and the sample sizes of the different groups. You should assume the group assignments are given.

#### Q4
TRUE/FALSE, using OLS on the aggregated data will produce unbiased estimates for $$\beta$$.

#### Q5
TRUE/FALSE, using OLS on the aggregated data vs using OLS on the individual level data will produce the same exact estimates for $$\beta$$.

#### Q6
If we only had access to the aggregate data, please produce the point-wise 95\% confidence interval for $$\beta$$ if we used OLS (i.e. pretend the variances are constant) and compare that to the interval created using WLS (i.e. the correct calculation).

#### Q7
Continuing Q6, which one would you recommend using?

#### Q8
Compute the point-wise 95\% confidence interval for $$\beta$$ using the individual level data using OLS. 

Side note, you should wonder if using the individual data is always preferable despite the calculation from $$Q3$$.


For the following problems, let's change the data generation process slightly: let $$X_i\stackrel{ind}{\sim} Binomial(n=100, p=\frac{k - 10}{200} + 0.5)$$, i.e. group 1 is distributed according to $$p=\frac{-9}{200} + 0.5$$, group 2 has $$p=\frac{-8}{200}+0.5$$, etc.  There are still 20 groups. 

Side note, you can imagine the group are different neighborhoods. $$X$$ is your parents' income when you were born and $$Y$$ is the base salary of your first job (all in weird units).

#### Q9
Compare the point-wise 95\% confidence interval for $$\beta_1$$ using OLS at the individual level data vs the method chosen in Q7 with the aggregate data.
Which one would you recommend?


#### Q10
Using the individual level data and OLS, please write the code that produces the the point-wise 95\% prediction interval for new $$Y$$ values for each hypothetical $$X$$ values, $$0, 1, \dots, 100$$. Please make the interval center the regression line. No need to report numbers, just the code is sufficient. 

Again, the prediction interval is the interval that will capture 95\% of the cases when predicting new data points.

#### Q11
For this problem, assume you only have access to the aggregate data.

Side note: if you were to create a prediction interval based on the aggregate data, you would need $$\bar{X}_{new}$$ AND its corresponding group size (notice how WLS assumes the weights are known). When you apply these intervals to individuals, this is how ecological correlation mistakes are made. 

Instead of creating an interval for $$\bar{Y}_{new}$$, let's create an interval for $$Y_{new}|\{X_{new}, \bar{X}\}$$ by computing an interval that uses $$Var(Y_{new} - X_{new}\hat{\beta}_{wls}|\bar{X}, X_{new})$$, estimates $$\hat{\sigma}^2$$ under our WLS setting, and centers $$X_{new}\hat{\beta}_{wls}$$. Please create a plot that compares this interval to the interval implied by your code from Q10.

Side note: you should think about what's specific about this set up is allowing us to do this? Is this calculation true for all WLS settings?


## NOT-the-James-Stein's estimator
Let's define MSE in estimating high dimension vectors, $$\beta$$, using an estimate $$\hat{\beta}$$, as $$E( \| \beta - \hat{\beta}\|^2)$$.

#### Q12
What is the theoretical MSE if we estimated arbitrary $$\beta$$ with the vector of $$0$$'s?

Side note: do not overthink. This is just to show anything CAN be an estimate for anything.

#### Q13
Under the usual regression settings, create the biased estimate $$\hat{\beta}_{\gamma} = \gamma * \hat{\beta}_{OLS}$$ where $$\hat{\beta}_{OLS}$$ is the coefficient estimate from the regression.
Calculate the theoretical mean squared error for $$\gamma \hat{\beta}_{OLS}$$. Express the result in terms of $$\gamma$$, $$\beta$$, $$X$$, and $$\sigma^2$$ and simplify as much as possible.

Side note: you should know why this isn't very useful in practice because $$\beta$$ and $$\sigma^2$$ are unknown.

#### Q14
To shrink a vector $$Z$$ to the origin (i.e. the vector of all 0s), we can multiple $$Z$$ by $$\gamma\in [0, 1)$$. However, we can also shrink $$Z$$ to arbitrary vector $$\mu$$ by calculating $$\gamma(Z-\mu) + \mu$$.

Let $$Y = X\beta + \epsilon$$ where $$\beta$$ is the 0 vector. Let $$\epsilon \sim N(0, 10)$$, $$n=1000$$, and create 99 random features all from a uniform random variable (between 0 and 1) and 1 constant feature for X. Let $$\hat{\beta}_{OLS}$$ be the usual regression estimate. Shrink $$\hat{\beta}_{OLS}$$ towards $$\mu = 2$$, i.e. a constant vector containing only 2's and with $$\gamma=0.99$$. Numerically approximate the MSE over 100 simulations for the shrink estimator and the OLS estimator. Report which estimator would you prefer if you're optimizing for MSE for estimating $$\beta$$.

{% include lib/mathjax.html %}
