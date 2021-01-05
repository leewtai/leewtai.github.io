# Homework 8: Modeling

## Significance in prediction vs inference

Let's create $$n=1000$$ samples from the following data generation process. 
Let $$X\stackrel{i.i.d.}{\sim} Normal(-5, 1)$$, let $$Y\stackrel{i.i.d.}{\sim} Normal(5, 1)$$, and let $$Z = \alpha_x X + \alpha_y Y + \epsilon$$ where $$\epsilon \stackrel{i.i.d.} Normal(0, 1)$$. Let $$\alpha_x$$ and $$\alpha_y$$ both be 1.

#### Q1
Continuing the settings from above, without any knowledge of the true data generation process, it's easy to just fit the wrong linear models like $$Y$$ on $$X$$ and $$Z$$.  Please draw out two different DAGs, one representing the true data generation process, and the other representing the (bad/wrong) regression of $$Y$$ on $$X$$ and $$Z$$. 

#### Q2
Please train 2 models using your existing data:
- regression of $$Y$$ on $$Z$$ alone, let's call this $$model_z$$
- regression of $$Y$$ on $$Z$$ and $$X$$, let's call this $$model_{xz}$$
Please generate 100 new data points (X, Y, Z) triplets.  When doing prediction, please assume the new values of $$Z$$ and $$X$$ are given but $$Y$$ is not observable (these are only observable when you're calculating the error rate).
Please report the average squared prediction error from $$model_z$$ vs $$model_{xz}$$ on these 100 new data points?

#### Q3
Please numerically demonstrate that the difference observed in Question 2 is significant or not with 95\% confidence. You should generate data under the true model for calculating the squared prediction error but not for training your model. 

Side note, please notice that we're using the concept of significance in a prediction setting!

#### Q4
Similar to Question 3, try to estimate whether the differences between the 2 models are significant, however, please pretend that you cannot generate new data but can only do cross validation on the original 1000 data points.

Side note: Try to imagine the steps yourself before looking at the steps below.

- Split your data into 10 groups of roughly equal sizes (hint: permute a vector that repeats $$[1, 2, \dots, 10]$$ 100 times then treat the permuted outcome as the group assignment for each sample).
- Loop through the 10 groups
  - Treat the current group as the testing data points.
  - Train $$model_z$$ and $$model_{xz}$$ on the remaining 900 data points
  - calculate the 2 squared prediction errors
- Perform a two-sample t-test to test if the difference is significant based on the outcome from the loop. (Please figure out what is the appropriate sample size and variance calculations!)

Side note: is the use of the t-test still good if we didn't know the residuals were Normal?

Side note: please look at the estimated testing error from your cross validation vs your testing error from generating new data. What would happen if the overall sample size for our training set decreased?

#### Q5
In our data generation process, the only parameters that describe the relationship between variables are $$\alpha_x$$ and $$\alpha_y$$. 
On the other hand, you have coefficients estimated from the predictive models of $$model_z$$ and $$model_{xz}$$ that estimate some relationship between the variables as well.
Are your coefficients from the predictive model estimating the parameters in the data generation process? Yes/No

Hint/Side note: from $$model_z$$, if you followed the formula to calculate $$\hat{\sigma}^2$$, you will get a number. What parameter is being estimated in our data generation by $$\hat{\sigma}^2$$ and what are the implications on the significance you calculated for the coefficients?

Hint/Side note: can you identify the difference between the significance in Q5 vs the significance in Q3/Q4?


## DAG

#### Q6
Obesity is an important factor for health. However, "obesity stigma" can also make people suffering from obesity to be less likely to do routine checkups. This can lead to issues where preventable diseases are not caught in the early stages and lead to more health complications. Please draw out the DAG that explains the relationship between health, obesity, obesity stigma, and checkups. For now, since the problem does not specify obesity stigma's direct impact on health, assume there is no direct link between these. 

Side note: If you're interested in a [summary paper from NIH](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4381543/).

Side note: If we did not "model" the impact from stigma on checkups, would the coefficients for obesity on health be overestimated or underestimated? (you should be able to simulate this!)

## Validation - simulating from your model

#### Q7
Generate true data under the settings of: n=100, let $$X\stackrel{i.i.d.}{\sim} Normal(mean=0, SD=0.9)$$, and let $$Y = 1 + 5 * sin(X) + \epsilon$$ where $$\epsilon \stackrel{i.i.d.}{\sim} Normal(0, 1)$$.

Now fit a regression of $$Y$$ on $$X$$ directly (without the transformation of $$sin$$). Let's instead generate simulated samples from $$Y_{new} \stackrel{indep}{\sim} N(X_{new} \hat{\beta}, \hat{\sigma}^2)$$, where the estimated values, $$\hat{\beta}$$ and $$\hat{\sigma}^2$$, are from the usual OLS calculation. Please use these simulated samples to create a 90\% prediction interval at 10 equally spaced values of $$X_{new}$$ ranging from the smallest to largest value in your original data $$X$$. Please plot the interval on top of your original data.
 
hint: to use samples to empirically construct an interval, you need a sufficient sample size.

side note: There are several key notes I hope you notice:
  1. the wrong model can do reasonably at certain regions of the data.
  2. if you didn't know the true data generation process, see how this method lets you know how your model is deficient.

{% include lib/mathjax.html %}
