# Homework 6: Multivariate Regression

#### Q1
Define a random vector with 3 random variables:
- $$X \sim Normal(0, 10)$$
- $$Y \sim Exp(\lambda = 0.1)$$
- $$Z = Y + 2 * X + \epsilon$$, where $$\epsilon \sim Unif[-5, 5]$$

Please assume that $$X$$, $$Y$$, and $$\epsilon$$ are all independent from one another.

Please calculate the theoretical values of $$Cov\left(\begin{bmatrix} X\\ Y \\ Z \end{bmatrix}\right)$$, hint: it's 3 by 3 matrix.

#### Q2, numerically approximating covariances
Please test out 2 sample sizes, 100 and 10000 to numerically approximate the 3 by 3 covariance matrix from **Q1** via simulation.

You should use the sample covariance to approximate the theoretical covariance matrix, i.e. $$\hat{\Sigma}_n \approx \Sigma$$.  $$\hat{\Sigma}_n$$ is the sample covariance based on sample size $$n$$.

Create 200 simulations for each sample size to approximate the covariance matrix above (i.e. you would have 200 covariance estimates for each sample size).
If the theoretical covariance matrix is $$\Sigma$$ and the estimate is $$\hat{\Sigma}$$, define the error as $$\| \Sigma - \hat{\Sigma} \|_2 = \|D\|_2 = \sqrt{\sum_{i=1}^{3} \sum_{j=1}^{3} D_{i,j}^2)}$$. This is called the Frobenius norm for the matrix $$D$$. 
Please report the 2.5 to 97.5 percentile values of the Frobenius norm, across the 200 simulations for each sample size. Please comment on the sample size's effect on the accuracy of the numerical approximation of $$\Sigma$$.

#### Q3, a common abuse of the word "sample size"
In this question, the word "sample size" is used in 2 different ways that is common and confusing.

In the regression setting, we often describe $$Y = X\beta + \epsilon$$, where $$Cov(\epsilon|X) = \sigma^2 I$$ as a $$n \times n$$ matrix. This $$\sigma^2I$$ is the theoretical covariance.

In the case where $$n=20$$, i.e. the sample size of the regression is 20, please write the code that would numerically approximate the covariance matrix $$\sigma^2 I$$ using the sample size with the smaller error from Q2 by simulating different $$\epsilon$$ vectors.
Please set $$\sigma^2=4$$. I'm intentionally not prescribing the distribution of $$\epsilon$$, choose your favorite distribution. :)

#### Q4
Let there be 20 samples. Let $$X1 \sim Bernoulli(0.3)$$, let $$X2 \sim Unif[-10, 10]$$, let $$X3 \sim Normal(100, 10)$$, let $$X4 = 2 * X1 - X2 + 0.3 X3$$, let $$X5=1-X1$$, and finally define $$X0$$ as the constant feature of 1's.
Please examine the eigen values for the matrix $$X^TX$$ with the following definitions of $$X$$ and report whether $$(X^TX)^{-1}$$ exists.

Note, the notation below indicates combining the vectors by columns
- $$X = \begin{bmatrix} X0 : X1 : X2 : X3 : X4 : X5 \end{bmatrix}$$
- $$X = \begin{bmatrix} X1 : X2: X3: X4: X5 \end{bmatrix}$$ 
- $$X = \begin{bmatrix} X1: X2: X3: X5 \end{bmatrix}$$ 
- $$X = \begin{bmatrix} X0: X2: X3: X4: X5 \end{bmatrix}$$
- $$X = \begin{bmatrix} X2: X3: X4: X5 \end{bmatrix}$$
- $$X = \begin{bmatrix} X0: X1: X2: X3: X4 \end{bmatrix}$$
- $$X = \begin{bmatrix} X0: X1: X5 \end{bmatrix}$$

### Simultaneous inference
#### Q5
Imagine $$Z\sim Binomial(n=100, p=0.05)$$, please report an 95% prediction interval for $$Z$$. Note, by convention, prediction intervals **centers** the expected value, but this is not technically required.

A 95% prediction interval is any interval such that, when predicting the value of $$Z$$, will have a 95% chance of containing $$Z$$.
 
#### Q6
Let the sample size be 1000, $$Y \sim Normal(0, 10)$$ then create 99 random features that are completely uncorrelated with $$Y$$ and each other.
Please regress $$Y$$ on these features and report the number of significant features using point wise hypothesis tests, i.e. $$|\frac{\hat{\beta}_i}{SE_{\hat{\sigma}^2}(\hat{\beta}_i}| \geq t(n-p, 97.5)$$ would identify a significant feature.

Recall that $$SE_{\hat{\sigma}^2}(\hat{\beta}_i) = \sqrt{\left[Cov(\hat{\beta}|X)\right]_{i,i}}$$ where we use $$\hat{\sigma}^2$$ to approximate $$\sigma^2$$.
Since you have the intercept, there should be a total of 100 tests being performed. 


#### Q7
Continuing from Q6, let us adjusted the problem by using the Bonferroni correction to perform simultaneous inference. Please write the code that would numerically show that the false positive rate from Bonferroni is at most 5% over 1000 simulations. In other words, the probability of calling at least one feature significant when all coefficients are 0, is upper bounded by 5%.

### Interpreting your model

#### Q8
Let the sample size be 200.
Define $$X \sim Normal(10, 10)$$, let $$Z \sim Bernoulli(0.4)$$, and let $$Y = 5 - X + 2 * Z + 3 * X* Z + \epsilon$$ where $$\epsilon \sim Unif[-3, 3]$$.
Please run the regression using all the data that includes the interaction effect and report the coefficients, let's call these $$\hat{\beta}$$. You should have 4 coefficients.

Side note, this is an example of how you can imagine data to be generated from different groups that have different intercepts and slopes.

#### Q9
Please regress $$Y$$ on $$X$$ only using the values where $$Z=0$$. Repeat this regression only using the values where $$Z=1$$. Report those coefficients, let's call them $$\hat{\beta}_0$$ and $$\hat{\beta}_1$$ respectively.

#### Q10
Assume the parameters below refer to the coefficients from $$\hat{\beta}$$, $$\hat{\beta}_0$$ and $$\hat{\beta}_1$$. Please answer the following:
- The intercept for $$\hat{\beta}$$ equals which other parameter?
- The intercept for $$\hat{\beta}_1$$ is the sum between which 2 parameters?
- The slope for $$\hat{\beta}_0$$ is the same as which other parameter?
- The slope for $$\hat{\beta}_1$$ equals to the linear combination of which other parameters?

#### Q11
Q8-Q10 shows a case where we can obtain identical regression estimates by regressing with interactions or by training 2 separate regression models, are the standard errors for these estimates the same, yes/no?

A thought you should have: "which method would you choose if someone asked you to choose?" (No need to answer this question for Q11).

{% include lib/mathjax.html %}
