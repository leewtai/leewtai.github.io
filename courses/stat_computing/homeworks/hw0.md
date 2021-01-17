# Homework 0 - Applied Statistical Computing

In introductory statistics, a metric called the standard deviation
is often used to calculate the "spread" in the data. Formally, for
a collection of data points, $$y_1, \dots, y_n$$, the standard
deviation is defined as:

$$SD(y_1, \dots, y_n) = \sqrt{\frac{1}{n}\sum_{i=1}^{n} (y_i - \bar{Y})^2}$$

where $$\bar{Y}$$ is the average of values $$\bar{Y}=\frac{1}{n}\sum_{i=1}^n y_i$$.

## Q0
Please create a numeric vector called `die` that contains each of the integer values from `1` through `6` (inclusive) in the following ways (order does not matter). Please use `print(die)` after each method so we can see the output.
- Using the `c()` function (please ignore the fact that if you check the `class()` here you will see `numeric` instead of `integer`)
- Using the `:` operator after seeing how it behaves after running the following examples:
  - `4:10`
  - `0:1`
  - `-3:3`
- By modifying the code `sample(k)` where `k` is an integer. Please read the documentation in `?sample` and see how `sample()` will behave when its first argument is an integer.

## Q1
Please calculate the standard deviation of `die` without using the `sd()` function but by **correcting** the following code. You should not need to add lines of code to complete this.

```r
die <- 
n <- length(die)
die_avg <- mean(die]
sum_sq_diff <- 0
for i in die {
    diff_from_avg <- die_avg - i
    sq_diff <- diff_from_avg^2
    sum_sq_diff <- sq_diff
}
theoretical_sd <- sqrt(sum_sq_diff)
print(theoretical_sd)
```

## Q2
Please apply the `sd()` function on `die` from Q1 and use this information to verify if the `sd()` function is calculating the same standard deviation as we have defined above?

## Q3
What happens when you forget to the closing parentases when calling a functionin the R console (i.e. the console section in Rstudio)? E.g. `c(1, 2, 3`
Please use words to describe the behavior (notice the symbol change in the prompt).

## Q4
In class, we've shown that the sample average follows the law of large numbers, please verify if `sd()` seems to follow the law of large numbers using our
dice roll example, i.e. does applying `sd()` on a larger samples of dice rolls converge towards the theoretical standard deviation of a die, Yes/No and please describe the output you see from your code that supports your answer?

Important: this is NOT a proof of any kind!

Side comment: in your introductory statistics course, you will learn that the statistic used based on the sample to "estimate" the population statistic is often slightly different.

## Q5
The documentation on `prob` within `?sample` is not entirely obvious. Please use a for-loop to simulate larger and larger sample sizes from the following piece of code:
`sample(c(1, 0), n, replace=TRUE, prob=c(3, 1))`

then analyze the output to answer what does `prob` do? Please write the code and explain your answer. You should decide what sample sizes are reasonable.

{% include lib/mathjax.html %}
