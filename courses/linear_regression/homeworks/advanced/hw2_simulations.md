# Homework 2: Simulations and optimization

Homework 2 is meant to give you some practice with simulation, optimization, and how it relates to the mathematics!

#### Q0
For the following problems, please generate exactly 33 Normal random variables called `X`, with $$\mu=50$$, and $$\sigma^2=10^2$$. With an $$\beta_0=10$$, $$\beta_1=-2$$, and 33 additional Normal random values with $$\mu=0$$, and $$\sigma^2=5^2$$ (let's call these $$\epsilon$$), calculate the value `Y` by using the following equation $$Y = \beta_0 + \beta_1 X + \epsilon$$. `X` refers to the first 33 values you created where $$\epsilon$$ refers to the second 33 values generated. You should have 33 `X` and `Y` value pairs at the end.

Please store your initial `X` and `Y` values in a CSV file called `xy.csv` with headers corresponding to `x` and `y` and upload these to CourseWorks.

#### Q1
Another objective function for finding a best line could be the sum of the perpendicular distances from the data points to the line.
What is the length of the line, i.e. euclidean distance, from an arbitrary point $$(u, v)$$ to an arbitrary point $$(x,y)$$ on the line $$y=a+bx$$? Please express the length in terms of $$u, v, a, b, x$$.

#### Q2
Please find the value $$x$$ that will minimize the length of the line, please express this value in terms of $$u, v, a, b$$.

#### Q3
Continuing from above, you now can calculate each data point's shortest distance to arbitrary line. Please write down the objective function, in code, that helps find the constants, $$\hat{a}$$ and $$\hat{b}$$, that will minimize the total squared distance where distance is defined as the shortest Euclidean distance between each data point and a line $$a+bx$$.

#### Q4
Use your `X` and `Y` generated values, what are the mean values for them respectively?

#### Q5
Find the optimal intercept and slope values using your data and objective function from **Q3**. Please plot two lines, the line implied by $$\hat{a}$$ and $$\hat{b}$$ and the regression line, on top of the scatter plot of the data.

#### Q6
True/False: Does the line from your fit in **Q5** pass through the point `(mean(X), mean(Y))`?

#### Q7
True/False: the total length calculated between your data points and your fitted line will always be smaller or equal than the total length between the data points and the true line (i.e. using $$\beta_0$$, $$\beta_1=-2$$) from the original simulation.

#### Q8
Please simulate the generation of Y values 1000 times without changing the value of the `X`, $$\beta_0$$, or $$\beta_1$$. Plot the two histogram of the fitted values $$\hat{a}$$ and $$\hat{b}$$. Please mark in the plots where the true value of $$\beta_0$$ and $$\beta_1$$ are. For this problem, you only need to submit a graph with 2 histograms, no code is necessary.

#### Q9
True/False, these optimized values are unbiased.

{% include lib/mathjax.html %}
