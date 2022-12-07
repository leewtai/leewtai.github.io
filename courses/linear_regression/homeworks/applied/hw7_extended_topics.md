# Homework 7: Multivariate Regression

## Q0: Logistic Regression
There's a [dataset on Kaggle to help people detect pulsars from Dr. Robert Lyon](https://www.kaggle.com/datasets/colearninglounge/predicting-pulsar-starintermediate?select=pulsar_data_train.csv). Please read the following post then download its corresponding dataset `pulsar_data_train.csv`:


The labels are binary whether an object is a pulsar or not and the features are continuous values. 

#### Q0.1 - Interpretation of metrics
Please read the following metrics that are common in classification then answer the following questions afterwards.

For each record, its label, $$Y$$, and our prediction for its label, $$\hat{Y}$$ will place it in one of the categories below:


|         |$$\hat{Y} = 1$$ | $$\hat{Y} = 0$$|
|---------|----------------|-----------------|
|$$Y = 1$$| A | B |
|$$Y = 0$$| C | D |

Using the definitions above, here are the list of metrics:
- Classification error: $$\frac{A + D}{A + B + C + D}$$
- Precision: $$\frac{A}{A + C}$$
- Recall/Sensitivity: $$\frac{A}{A +B}$$
- Specificity: $$\frac{D}{C + D}$$

Here are the list of questions:
- As an astronomer, the amount of images is often overwhelming so we need to allocate manual hours carefully if we decide to study a particular region of the cosmos. In other words, if we decide to study a particular region, we would like a pulsar to exist, which metric above best captures this idea? Please add a maximum 2 sentence explanation. 
- In our dataset, what accuracies would you get if your model is a simple rule of classifying everything as not a pulsar, i.e. $$\hat{Y}_i = 0$$ for every data point? Side comment: something should look oddly good for such a terrible classifier
- If we created an algorithm that randomly labels according to the overall percentage of labels in the training data, what is the expected value for each of the metrics? You can calculate or simulate this.

#### Q0.2 - Comparing models
A common way to compare models is to calculate the trade-off between recall and precision over different thresholds.
In our setting, the thresholds, $$\alpha$$, would be the cutoff used to convert $$\hat{p}(X)$$ to $$\hat{Y}$$, i.e.

$$\hat{Y}|X = \begin{cases}
              1 & \text{if } p(X) \geq \alpha \\
              0 & \text{otherwise}\\
\end{cases}
$$

For linear regression, let $$\hat{p}(X) = X\hat{\beta}$$ and the definition for $$\hat{Y}$$ is change to the function above.

Please compare the linear regression model against the logistic regression model with the following criteria:
- You should have at least one test set to calculate the precision and recall values
- the test set should be the same for the 2 models (side comment: why is this important?)
- the two models will have different thresholds to create the different values of precision and recall, please choose what these should be!
- Please decide what features you decide to include into the models but keep those features the same (no unique solution here) between the models
- Please create a graph that shows the precision and recall on different axes (labeled)
  - The range of the axes should be at their maximum ranges possible (side comment: why is this important?)
  - Please add a line to your plot that represents a third model: $$\hat{Y}=1$$ for every record.

Side comment: The models should be similar but are they identical in their prediction? This answer can be different depending on the number of features!

## Q1 - Wrong models are not always wrong

Let's create $$n=1000$$ samples from the following data generation process. 
- Let $$X\stackrel{i.i.d.}{\sim} Normal(-5, 1)$$
- Let $$Y\stackrel{i.i.d.}{\sim} Normal(5, 1)$$
- Let $$Z = \alpha_x X + \alpha_y Y + \epsilon$$ where $$\epsilon \stackrel{i.i.d.}{\sim} Normal(0, 1)$$.
- Let $$\alpha_x$$ and $$\alpha_y$$ both be 1.

To give some context, you can imagine that $$X$$ is the number of seeds, $$Y$$ is the amount of fertilizer, and $$Z$$ is the amount of yield.

#### Q1.1 - DAG
Is $$Z$$ a confounder, collider, or mediator in the data generation process?

#### Q1.2
Please train 3 models (please include intercepts for all of the following):
- regression of $$Y$$ on $$Z$$ alone, let's call this $$model_z$$
- regression of $$Y$$ on $$Z$$ and $$X$$, let's call this $$model_{xz}$$
- regressing $$Z$$ on $$Y$$ and $$X$$ (i.e. the correct model), let's call this $$model_{true}$$

Please generate 1000 new data points $$(X, Y, Z)$$ triplets from the true data generation. 
When doing prediction, please assume the new values of $$Z$$ and $$X$$ are given but $$Y$$ is not observable (these are only observable when you're calculating the error rate). To do prediction with $$model_{true}$$, please calculate $$\hat{Y}_{true} = (Z - \hat{\alpha}_x X - \hat{\alpha}_0) / \hat{\alpha}_y$$.

- Please report the average squared prediction error for these 3 models on these 1000 new data points?
- Which model would you use for predicting $$Y$$?

Side comments: in our context, imagine I'm a seed dealer, I know the yield of my customers, and now I want to estimate the amount a typical customer is spending on fertilizer. Notice how something intuitive can be quite bad.

#### Q1.3 - Diagnosing issues
From Q1.2, you should have seen that $$model_{true}$$ performed worse than the other 2 models.

- Please plot the scatter plot of the new $$Y$$ values against the prediction from $$model_{true}$$, then overlay the scatter plot of the new $$Y$$ values against the predictions from $$model_{xz}$$, then add the 1 to 1 line (i.e. 45 degree angle line) to the plot.
- Which model is more "unbiased" in its predictions?

Side comment: why is $$model_{true}$$ doing worse? The answer is in the plot!

#### Q1.3 - Inference
For $$model_{xz}$$, we fitted a model $$Y = \beta_0 + \beta_x X + \beta_z Z + error$$. It seems reasonable to use the estimate $$\hat{\alpha}_y^{xz} = \frac{1}{\hat{\beta}_z}$$ where $$model_{true}$$ has a natural estimate from the regression model for $$\alpha_y$$.

Please use simulation to understand if we should use $$model_{xz}$$ or $$model_{true}$$ to estimate $$\alpha_y$$?
- Please state which model is preferable
- Please show one visualization that justifies your answer above.

Side comment: in the future, you'll be using different components of models for different purposes, to understand which is better, simulate it!

## Q2 - Marketing

In question, we will highlight the impact of adding variables to your model.

Imagine the following distribution of variables:

- Let $$S_i \sim Bernoulli(B_i)$$
- Let $$C_i \sim Exponential(\frac{0.1}{B_i + A_i})$$
- Let $$B_i \sim Unif(0, 1)$$
- Let $$A_i \sim Bernoulli(0.2)$$

You can imagine this as a simulation for **S**ubscriptions are a function of someone's **B**ackground, the number of **C**licks is a function of someone's **B**ackground whether they have been exposed to an **A**dvertisement.

In general, companies often run **randomized trials** to estimate the impact of marketing campaigns. So it's not unrealistic to imagine that people exposed to the advertisement are randomly chosen.

In general, you will not observe/measure someone's background but only know of their online activity (e.g. clicks) and whether they are exposed to your advertisement. The goal for many businesses is for people to subscribe to their services.


#### Question 2.0

Most advertisement campaigns are run by the marketing teams, who are interested in **estimating the impact of the campaign**.

- Please draw out the DAG for this setting. This can be an image or you can type a sequence of edges like "B -> S" to denote the graph.
- From the data generation process above, does the advertisement encourage users to subscribe?
- Please generate this dataset with `n=1000`, each record $i$ should have one realized value for each of the variables.
- Please perform a hypothesis test on those exposed to the advertisement vs not, whether the subscription rates are significantly different.
- The advertisement was meant to target 20% of the users, is 200 enough data to determine if the percentage of users actually exposed to the advertisement is more than 1% off from 20%? (I recommend simulating this!)


#### Question 2.1

Remember that you do not have access to the **B**ackground variable!

- According to the "truth", is the likelihood of subscribing a function of the clicks?
- Please fit a logistic regression `glm(YOUR_SUB ~ YOUR_CLICKS, family=binomial(link=logit))` of the subscription probability based on the clicks. Please comment on whether you're surprised by the outcome or not.
- Please fit a logistic regression of hte subscription probability based on the clicks AND the advertisement.
- Comparing the 2 models in Q2.1, please show graphically or numerically which model aligns with the data better?

#### Question 2.2

- You fitted 3 models so far, one on ads, one on clicks, and one with both, which one should you use given we're trying to determine if the advertising worked or not.

{% include lib/mathjax.html %}
