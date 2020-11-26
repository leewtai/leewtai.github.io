# Homework 2: Simulations and Programming and Simple Least Squares

#### Goals
Homework 2 is meant to encourage you to challenge the reasoning of the "least square".
In particular, we have shown that the regression line minimizes the total squared vertical distance between each data point and any other line.
In this assignment, we challenge this choice by proposing to minimize the a different distance.

#### Q1 - an alternative distance
Between an arbitrary point $$(u_1, v_2)$$, and another arbitrary point $$(u_2, v_2)$$, the Euclidean distance between them can be written as $$\sqrt{(u_1 - u_2)^2 + (v_1 - v_2)^2}$$.
Given arbitrary point  $$(u, v)$$ and arbitrary line $$y = a + b * x$$, there exists a point, $$(x^*, a + b * x^*)$$, on the line that minimizes the Euclidean distance between the point $$(u, v)$$ and the line. Please solve for the expression for $$x^*$$ using $$a$$, $$b$$, $$u$$, $$v$$. 

Hints:
- If $$k < w$$, then $$k^2 < w^2$$ so the point that minimizes the Euclidean distance also minimizes the squared Euclidean distance. 
- The Euclidean distance can be thought as a function of $$x^*$$. According to calculus, the derivative of this distance with respect to $$x^*$$ should be 0 at the minimum.


#### Q2 - Translating mathematics to code
Continuing from Q1, if we had multiple data points, $$(u_1, v_1), \dots, (u_n, v_n)$$, then we could compute the smallest Euclidean distance between each data point to an arbitrary line, then sum up all of those distance values. 
- Please write a function that takes in a vector named $$par=(a, b)$$, a vector named $$u = (u_1, \dots, u_n)$$, and another vector named $$v = (v_1, \dots, v_n)$$, then returns the total shortest Euclidean distance between the $$n$$ data points and an arbitrary line $$y = a + b * x$$. In other words, the function takes in 3 vectors and returns a single numeric value. No need to simplify any expressions.
- Please use the `u` and `v` provided in the file `hw2_q2.csv` then report the total shortest Euclidean distance for $$par=(2.5, -2.5)$$.
- Please use the `u` and `v` provided in the file `hw2_q2.csv` then report the total shortest Euclidean distance for $$par=(1.5, -3.5)$$.
You should submit your code for the function and report both numbers.

#### Q3 - Using programming to find the best line by brute force
Let's perform a grid search for the best value of `a` and `b` by doing the following:
- Create `50` equally spaced values for `a` between `0` and `4`.
- Create `50` equally spaced values for `b` between `-4` and `0`.
- Create all `2500` possible combinations between the 2 sets of values above.
- Calculate the total shortest Euclidean distance for each 2500 possible combinations using the same `u` and `v` values from `hw2_q2.csv`. Please plot the scatter plot of these values by the corresponding `a` and `b` values (you can use 2 separate scatter plots).
- Please report the set of values of `a` and `b` with the smallest value among the 2500 numbers above.

#### Q4 - Grid search vs numeric optimization
There are packages that can find the best value for `a` and `b` for us that does not perform a grid search. Let `u` and `v` respectively indicate the columns in the file `hw2_q2.csv`and let's call the function you wrote in Q2, `q2_fun`, then the follow code should return the best values for `a` and `b`:

```r
opt_ab <- optim(par=c(2, -2), q2_fun, u=u, v=v, method="BFGS")
best_a <- opt_ab$par[1]
best_b <- opt_ab$par[2]
```

If you are a Python user, note that you should work with numpy arrays. 

```python
from scipy.optimize import minimize
opt_ab = minimize(q2_fun, [2, -2], args=(u, v), method="BFGS")
best_a = opt_ab.x[0]
best_b = opt_ab.x[1]
```
Comment: the `(2, -2)` is just a place for the algorithm to start searching, 

- Please compare the answer from the snippet above to your answer from the grid search. Which set of values are better, `optim()` or grid search? Better is defined by having a smaller total shortest Euclidean distance. In the future, I would expect you to infer what "better" means given the context.
- In preparation for the next question, please write a function that takes in potential new vectors `u` and `v` (similar to the code above) then returns a vector with the best values for `a` and `b`. In other words, if we call the best values $$\tilde{a}$$ and $$\tilde{b}$$, the function should take in 2 vectors and returns a vector with $$(\tilde{a}, \tilde{b})$$. You should keep the starting value in the snippet above.


#### Q5 - Uncertainty from different datasets
We can simulate a different dataset for `u` and `v` by running:

```r
n <- 100
u <- runif(n, -5, 5)
v <- 2 - 3 * u + rnorm(n, sd=2)
```

Or 

```python
import numpy as np
n = 100
u = np.random.uniform(-5, 5, n)
v = 2 - 3 * u + np.random.normal(scale=2, size=n)
```

Please simulate `5000` different datasets and use your function from Q4 to create 2 histograms:
- A histogram of the 5000 different $$\tilde{a}$$ values across the 5000 datasets with a vertical line marking the value $2$.
- A histogram of the 5000 different $$\tilde{b}$$ values across the 5000 datasets with a vertical line marking the value $-3$.


#### Q6 - Visualizing unbiasedness
In Q5, the value `2` and `-3` are respectively the true intercept ($$a_{true}$$) and true slope ($$b_{true}$$) that generates the data. Given any dataset, our current method could use $$\tilde{a}$$ and $$\tilde{b}$$ to estimate $a_{true}$ and $b_{true}$ respectively. Using your results from Q5, please answer whether you believe $E(\tilde{a}) = a_{true}$ AND $E(\tilde{b}) = b_{true}$, i.e. unbiased, your answer should be a single Yes/No with a short explanation.

#### Q7 - Different objectives lead to different solutions
Recall that regression minimizes the total squared residual instead of the total shortest Euclidean distance. Let's name the coefficients from the regression $\hat{a}$ and $\hat{b}$ respectively. You can get the regression coefficients using `lm(v ~ u)$coefficients` in R. For Python users, 

```python
import statsmodels.api as sm

ols = sm.OLS(v, sm.add_constant(u)).fit()
ols.params
```

Please plot the scatter plot using the data `hw2_q2.csv` with `u` on the x-axis and `v` on the y-axis along with 2 lines: a dotted line with the intercept $$\tilde{a}$$ and slope $$\tilde{b}$$ and a solid line with intercept $$\hat{a}$$ and slope $$\hat{b}$$.

Hint: `abline(a = 0, b=1)` plots a line with intercept=0 and slope=1 on a plot.

#### Q8 - Comparing methods
Please repeat Q5 but use the regression coefficients $\hat{a}$ and $\hat{b}$ instead of $\tilde{a}$ and $\tilde{b}$.

#### Q9 - Making a decision
Comparing your plots from Q5 vs Q8, if you want to estimate $a_{true}$ and $b_{true}$, do you prefer $\hat{a}$ and $\hat{b}$ or $\tilde{a}$ and $\tilde{b}$? Please give a short explanation.


{% include lib/mathjax.html %}
