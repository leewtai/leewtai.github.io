# Homework 2: Simulations and Programming and Simple Least Squares

#### Goals

Homework 2 encourage you to challenge the reasoning behind the "least square" choice.
In particular, we have shown that the regression line minimizes the total squared vertical distance between each data point and any other line.
In this assignment, we challenge this choice by proposing to minimize the a different distance.

#### Q1 - an alternative distance

Between an arbitrary point $$(u_1, v_1)$$, and another arbitrary point $$(u_2, v_2)$$, the Euclidean distance between them can be written as $$\sqrt{(u_1 - u_2)^2 + (v_1 - v_2)^2}$$.
Given arbitrary point  $$(u, v)$$ and arbitrary line $$y = a + b * x$$, there exists a point, $$(x^*, a + b * x^*)$$, on the line that minimizes the Euclidean distance between the point $$(u, v)$$ and the line. The expression for $$x^*= \frac{u + b(v - a)}{1 + b^2}$$.

Please write a function that takes in 3 inputs: a vector named `par=c(a,b)` with the intercept and slope, a vector of `u`, and a vector `v` then outputs the total shortest Euclidean distance between these points and the given line. The length of `u` and `v` are both `n` and should correspond to points.

You are NOT allowed to use a for-loop in this function.


#### Q2 - Translating mathematics to code

We will test out our function on the [file `hw2_q2.csv`](hw2_q2.csv). 
- Please use the `u` and `v` provided in the file `hw2_q2.csv` then report the total shortest Euclidean distance for $$par=(2.5, -2.5)$$.
- Please use the `u` and `v` provided in the file `hw2_q2.csv` then report the total shortest Euclidean distance for $$par=(1.5, -3.5)$$.
- Please use the `u` and `v` provided in the file `hw2_q2.csv` then report the total squared error for $$par=(2.5, -2.5)$$ used in regression.
- Please use the `u` and `v` provided in the file `hw2_q2.csv` then report the total squared error for $$par=(1.5, -3.5)$$ used in regression.


#### Q3 - Using programming to find the best line by brute force

Let's perform a grid search for the best value of `a` and `b` by doing the following:
- Create `50` equally spaced values for `a` between `0` and `4`.
- Create `50` equally spaced values for `b` between `-4` and `0`.
- Create all `2500` possible combinations between the 2 sets of values above, I recommend storing these in a matrix of size 2500 by 2, hint: `ab_combo = matrix(NA, nrow=2500, ncol=2)`
- Please report the set of values of `a` and `b` with the smallest value among the 2500 numbers above.
- Calculate the total shortest Euclidean distance for each 2500 possible combinations using the same `u` and `v` values from `hw2_q2.csv`. Please plot the scatter plot of these values by the corresponding `a` and `b` values (you can use 2 separate scatter plots).

#### Q4 - Grid search vs numeric optimization

There are packages that can find the best value for `a` and `b` for us that does not perform a grid search. Let `u` and `v` respectively indicate the columns in the file `hw2_q2.csv`and let's call the function you wrote in Q1, `q1_fun`, then the follow code should return the best values for `a` and `b` (EDIT: this was previously `q2_fun` in last year's version, the intent is clear to your grader):

```r
opt_ab <- optim(par=c(2, -2), q1_fun, u=u, v=v, method="BFGS")
best_a <- opt_ab$par[1]
best_b <- opt_ab$par[2]
```

Comment: the `(2, -2)` is just a place for the algorithm to start searching, 

- Please compare the answer from the your grid search answer. Which set of values are better, those from `optim()` or from the grid search?
- In preparation for the next question, please write a function that takes in potential new vectors `u` and `v` (similar to the code above) then returns a vector with the best values for `a` and `b`. In other words, if we call the best values $$\tilde{a}$$ and $$\tilde{b}$$, the function should take in 2 vectors `u` and `v` then returns a vector with $$(\tilde{a}, \tilde{b})$$. You should keep the starting value `(2, -2)`.


#### Q5 - Uncertainty from different datasets

We can simulate a different dataset for `u` and `v` by running (this is the regression model for data generation):

```r
n <- 100
u <- runif(n, -5, 5)
v <- 2 - 3 * u + rnorm(n, sd=2)
```

Please simulate `5000` different datasets and use your function from Q4 to create 2 histograms:
- A histogram of the 5000 different $$\tilde{a}$$ values across the 5000 datasets with a vertical line marking the value $$2$$.
- A histogram of the 5000 different $$\tilde{b}$$ values across the 5000 datasets with a vertical line marking the value $$-3$$.


#### Q6 - Visualizing unbiasedness

In Q5, the value `2` and `-3` are respectively the true intercept ($$a_{true}$$) and true slope ($$b_{true}$$) that generated the data. Given any dataset, our current method could use $$\tilde{a}$$ and $$\tilde{b}$$ to estimate $$a_{true}$$ and $$b_{true}$$ respectively. Using your results from Q5, please answer whether you believe $$E(\tilde{a}) = a_{true}$$ AND $$E(\tilde{b}) = b_{true}$$, i.e. unbiased, your answer should be a single Yes/No with a short explanation.

#### Q7 - Different objectives lead to different solutions
Recall that regression minimizes the total squared residual instead of the total shortest Euclidean distance. Let's name the coefficients from the regression $$\hat{a}$$ and $$\hat{b}$$ respectively. You can get the regression coefficients using `lm(v ~ u)$coefficients` in R. 

Please plot the scatter plot using the data `hw2_q2.csv` with `u` on the x-axis and `v` on the y-axis along with 2 lines: a dotted line with the intercept $$\tilde{a}$$ and slope $$\tilde{b}$$ and a solid line with intercept $$\hat{a}$$ and slope $$\hat{b}$$.

Hint: `abline(a = 0, b=1)` plots a line with intercept=0 and slope=1 on a plot.

#### Q8 - Comparing methods

Please repeat Q5 but use the regression coefficients $$\hat{a}$$ and $$\hat{b}$$ instead of $$\tilde{a}$$ and $$\tilde{b}$$.
You should use the same dataset as those generated from Q5.

#### Q9 - Making a decision

Comparing your plots from Q5 vs Q8, if you want to estimate $$a_{true}$$ and $$b_{true}$$, do you prefer $$\hat{a}$$ and $$\hat{b}$$ or $$\tilde{a}$$ and $$\tilde{b}$$? Please give a short explanation.


#### Q10 - Standard errors

Please show your code and the resulting values for the following:
- What is the standard error of $$\tilde{a}$$ and $$\tilde{b}$$?
- What is the standard error of $$\hat{a}$$ and $$\hat{b}$$?


#### Q11 - Prediction

Please use the dataset from `hw2_q2.csv` for this problem.

Please show the code for the following steps:
- Please separate the data into 2 groups, those with `u` beyond `(-4, 4)` and those `u` within `(-4, 4)`.
- Please calculate $$(\hat{a},\hat{b})$$ **only** using the values where the corresponding `u` is within `(-4, 4)`.
- Please predict for the values with `u` values beyond `(-4, 4)` using $$(\hat{a}, \hat{b})$$
- Please compare your predicted values and answer whether they are "good" by comparing them to one of the following:
  - The typical error you see between the fitted line and the data used to obtain the line
  - The overall spread of the `v` values
- Please explain your choice above and perform the comparison (you'll have to choose a metric to quantify the statement).


{% include lib/mathjax.html %}
