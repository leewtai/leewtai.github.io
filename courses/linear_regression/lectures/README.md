# Simulation-based linear regression (with calculus shown but not used)

Simulation-based linear regression is an undergraduate "text" that
walks through the usual introductory linear regression theorems
through simulations rather than mathematical proofs. We will generally
take the 1-2 step approach of
- "observing" the behavior of the regression model (and code) under different context
- Talk about its implication in practice
- Motivating the theoretical notation
We will also help you translate between problems, simulation code, and
mathematical expressions of a model.

- Why bother with linear regression in the modern age?
  - Linear regression is still used widely today. Many social sciences still use
    linear regression as **the model** when understanding the relationship between
    variables. It's also a great instructional tool for people to understand how
    to assess models, understand common challenges models face, and it is easy to
    run. There are many modern papers that understand the behavior of deep learning
    models via linear regression.
- What to expect from this text?
  - What question does it answer vs not?
  - What is linear regression, a summary, an algorithm, or a model?
  - How should I evaluate someone's regression model?
  - How should I create my own regression model?


## Prerequisites

Before divining into linear regression, it is important to have some background
in **elementary statistics** and **programming**.
### [Prerequisites - Introductory Statistics](modules/prereq-intro-stat.md)
### [Prerequisites - Basic Programming]

## Why do we need linear regression?

Imagine this question, do men and women make different salaries? Let's take a look, with the tools from your prerequisites, at New York City's annual salaries given to different civil servants in 2022.

```R
library(tidyverse)
salaries <- read.csv("clean_police_salaries_2022.csv")

salaries %>% groupby(gender_from_name) %>% select(mean_salary = mean(salary))
# 
#
```

Do you have your answer? Do you have any follow-up questions? Hopefully you believe that New York City (NYC) has fair compensation practices so some piece(s) of the puzzle is likely missing. 

If you take a deeper look, the compensation data is much more complicated, part-time vs full-time, overtime vs salaried individuals, different departments, different titles etc. How can we make the men and women in our data comparable given all these factors?

But before we dive too deep, what information would you need to trust the data first? What do we expect to be true or not true in our data?

Also, if someone worked in the police department for 5 years, what should their expected salary be?

These are very different questions, but can all be solved with linear regression! However, how we use linear regression will differ.

### Should I just learn AI or deep learning instead?

Learning linear regression is not a waste of time because:
- Linear regression can help us understand complicated models and the typical challenges when models interact with data.
- Many scholars still study AI models using our understanding with linear regression
- Regression can still solve some problems faster and better relative to AI

#### One sentence please, what is linear regression?

Linear regression is an algorithm that fits a "best" line to the data. 

Let's look at the scatter plot of the salary vs tenure (your inputs) and place a line through the data. Different people may place a slightly different line, but linear regression unifies some aspects of what best means. We will make this concrete soon but you should think about data being your input and the line (specifically the slope(s) and intercept) as the output of this algorithm.

##### What problems are solved with a line?
This is the **most important** lesson, knowing when and how to apply linear regression will be a key focus here. Overall, a line can:
- **Summarize** data (is there a correlation between "manager" in your title and being "full-time"?)
- **Predict** within and beyond the data at hand (If one works for what about 3 years as a police officer, how much would their salary be? What about 10 years?)
- **Model** the relationship between different variables (how much does gender impact salary?)

We will dive deeper into each of these later.

##### How do I run regression?

There is a built-in function in R called `lm()`, ("lm" stands for linear models), here's an example of fitting the regression line
```R
# Define some fake data
df <- read.csv("demo.csv")
x2 <- c(1, 2, 3)
y2 <- c(-3, -2, -1)

# R will first look for "y" and "x" among the columns of df
demo_lm <- lm(y ~ x, data=df)
# If the variables are not among the columns of df, R will find them in your global name space
demo2_lm <- lm(y2 ~ x2, data=df) # data=df is redundant, try it out!
# This should throw an error
demo3_lm <- lm(y3 ~ x3, data=df)

# To "see" the line
plot(demo_lm)
summ_tab <- summary(demo2_lm)
summ_tab
```

Easy? Yes! But the challenge is not in calling the function on the data, but knowing what questions to ask, when to fit the regression, how to improve the regression, and knowing the pitfalls of the regression line.

For Python users, a good package called `statmodels.OLS` behaves very similarly to R's `lm()` if you want to stick in Python. We will only show the code in R.

## Revisiting some introductory statistics through simulations

Here we will cover some new applications of programming onto some old concepts that will be useful in understanding regression later.

### Optimization - finding the best

Imagine finding the "best" number to represent the NYC police salaries in our data. What would we need to fix so there's only one solution? 

This is somewhat unintuitive at first but a convenient way to think about the best is to think about the least bad option. This is called the objective function, it takes in a candidate solution and reports how bad the candidate value was. By trying out different candidates, we'll then arrive at the best one. We'll walk through this below:

Pretend you pick an arbitrary number `loc` to represent all of the salaries in our data, the further this value is from an individual data point $i$, the worse it is representing data point $i$. This concept can be expressed as

|Idea |Programming | Math|
|---|---|---|
|How far is the $i$th salary from arbitrary `loc`|`abs(salaries[i] - loc)`|$\|X_i - loc\|$|

So now imagine all $n$ data points in our data, a natural way to aggregate the numbers is to add them together, i.e.

|Idea |Programming | Math|
|---|---|---|
|How to aggregate the "far-ness" across all data points|`sum(abs(salaries - loc))`|$\sum_{i=1}^n\|X_i - loc\|$|

So how can we assess different values of `loc`? Well, let's try to plot it!
```R
k <- 1000
locs <- seq(min(salaries), max(salaries), length.out=k)

obj <- function(loc){
    return(sum(abs(salaries - loc)))
}

df_holder <- matrix(0, nrow=k, 2)
for(i in seq_along(locs)){
    df_holder[i, ] <- c(locs[i], obj(locs[i]))
}

plot(df_holder[, 1], df_holder[, 2],
	 xlab="Candidate loc values", ylab="Objective function")
abline(v=mean(salaries), col="red")
abline(v=median(salaries), col="blue")
legends("topright", legends=c("Mean", "Median"), fill=c("red", "blue"))
```
So is the median or mean better in this case?

#### Different objective functions

What if instead of $\sum_{i=1}^n \|X_i - loc\|$ , I preferred $\sum_{i=1}^n \|X_i - loc\|^2$?
Would our answer change? Turns out both are legitimate objective functions but the latter one penalizes extreme values more than the former one.

##### Verification - squaring penalizes extreme values
How could we verify this statement?
```R
library(tidyverse)
# Pick an arbitrary loc
loc <- salaries[100]

salary_diff <- salaries - loc
badness1 <- abs(salary_diff)
badness2 <- abs(salary_diff)^2

df <- cbind(salary_diff, badness1, badness2)
# ggplot2.point_geom / facet
```

##### Optimization through calculus
Turns out when we use the squared penalty, we can rephrase this in terms of math:
$$\arg\min_{loc} \sum_i \|X_i - loc\|^p$$
And by doing some calculus, i.e. differentiate by $loc$ then setting that to 0, we can find that the optimal number to represent all the data points is the mean, the algorithm that adds all the numbers then divides the total by the number of values added.

#### Review
In review, we tried to find the best number by defining the least bad 


### [What is a model?]
A model is a mathematical description for a process. An example process is how the measured weights for a group of sampled Americans in 2016 could be?


#### Example of "show, observe, then mathematize"
For statistics that describe the location, a mathematical way to describe "desirable properties
for a statistic" is to define objective functions for the statistic. An objective function
compares the statistic, a single number,
to each value in the dataset and computes a "penalty score" for how different the  that the mean, median, and mode are statistics meant to minimize
the different "lack of fits" to the data.

|Objective |Objective in English| Solution|
|----|----|-----|
|$$\sum_{i=1}^{n} 1[Y_i == \alpha]$$ |A bad representative value $$\alpha$$ is one that is **different** from the data points| $$\beta_0=$$mode$$(Y_1, \dots, Y_n)$$, i.e. the most common value|
|$$\sum_{i=1}^{n} \|Y_i - \alpha\|$$ |A bad representative value $$\alpha$$ is one that is far (in an absolute distance) from the data points| $$\beta_0 =$$median$$(Y_1, \dots, Y_n)$$, definition is not unique|
|$$\sum_{i=1}^{n} \|Y_i - \alpha\|^2$$ |A bad representative value $$\alpha$$ is one that is far (in a squared distance) from the data points| $$\beta_0 = \frac{1}{n} Y_i$$|

The mean's sensitivity to the tails is a direct result of minimizing the squared distance. A data point that is far away will have its distance squared.

  - Using statistics like mean/median
  - Statistics
  - Programming
- Generalizing the mean
- Simple linear regression
  - alternatives to regression
  - interpretations
- Regression as a model for data generation
- Questions for model parameters and/or model output
  - Error
    - Bias
    - Variance
- Best linear unbiased estimator
- Hypothesis testing with regression
- Multivariate linear regression
  - conditional interpretations
  - common sources for additional features
- Challenges with linear regression
  - high dimensions
- Remedies
  - PCA
  - Regularization

{% include lib/mathjax.html %}
