# Simulation-based linear regression (without calculus)
  
Simulation-based linear regression is an undergraduate "text" that
walks through the ususal introductory linear regression theorems
through simulations rather than mathematical proofs. We will generally
take the approach of "observing" the behavior of the regression model
under different context before motivating the theoretical interpretations.
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
  - How is the regression line defined?
  - What question does it answer vs not?
  - How should I evaluate someone's regression model?
  - How should I create my own regression model?


## Prerequisites

Before divining into linear regression, it is important to have some background
in **elementary statistics** and **programming**.

### Prerequisites - Introductory Statistics 

You should understand the role statistics plays in the scientific method.
- **Observe** the world through summary statistics
- Formulating a **hypothesis** by abstracting and decomposing the problem
- Collecting the relevant **data** for the question at hand (sampling and experiments)
- **Analyzing** the relevant data with respect to randomness (hypothesis testing)
- **Decide** to reject or fail to reject our null hypothesis (understand type 1 vs type 2 errors)

#### Observations via summary statistics or graphs

When observing data, we often visualize different types
of data differently, e.g. histograms for quantitative vs bar charts for qualitative data.
But ultimately we care about the **distribution** of the data, i.e. the different
possible values and the associated relative frequencies (we care about the absolute frequency
if the occurrence for the smallest category is small).

An example of **distributions** are:
- The distribution of grades in a class could be 35% A's, 50% B's, 13% C's, and 2% F's.
- The distribution of male vs female in your city could be 49% to 51%.
- The distribution of number of children could be 0, 1, 2, 3, and 4+.


|Feature | Significance of feature | common statistics used to quantify the feature| 
|-------|--------|---------|
|Uni-modal vs multi-modal distribution| multi-modal distributions could imply multiple populations, e.g. children and adults, in the same dataset. Most summary statistics below often assume the distribution is uni-modal.| None. This is often eye-balled from graphs|
|Location| Where is data, e.g. are regrets with college majors around 10% (not bad) or 50% (yikes!)| mean, median, mode|
|Spread| Relative to the location statistic, how spread-out/variable is the data? e.g. 50% regret $\pm$ 30% is very different from 50% $\pm$ 5%| standard deviation, inter-quartile range (IQR), range|
|Skew|Are data values symmetrically distributed about the center? Long tails imply a small fraction of values are vastly different from the majority|This is often eye-balled in introductory statistics|

How can there be multiple values that serve the same purpose, i.e. different quantities that
reflect the same feature in a distribution? This is because different statistics have different
properties, these properties result from the different calculations, and for different problems
we desire different properties.

The most popular property is the sensitivity to extreme values in the distribution. Means are
sensitive to values in the tail where medians are less so. An example is income where adding a
billionaire to your neighborhood would increase the mean income a lot but not impact the median
income of your neighborhood.

This sensitivity is not always bad, different problems may want to be sensitive to the tail,
e.g. housing prices are similar to income data where there
is a long right tail. A policy maker would be interested in the median housing price
to understand the typical cost of living where a realtor would be interested in the
mean housing price because they earn commission as a fraction of the selling price and one
big sale could suffice for one's annual income.

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

The spread statistics allow us to know how much data is within a certain range. For example, the amount of data that is $k$ SD's away from the average is upper-bounded by $$\frac{1}{k^2}$$. The amount of data within one IQR from the median is at least 50%. In some sense, it allows us to know the quality of the location statistic.

#### Formulating a hypothesis

A simple idea like "Does a drug work?" requires several considerations:
- Define "work"
  When evaluating the effects of vitamin C on the common cold, it was determined that vitamin C does not prevent be lessens the severity of the common cold but the effects are not strong. Severity, however, can be difficult to measure, e.g. highest fever, number of sick-leaves taken, etc.
- Define "using the drug"
  The ability to follow a regiment is difficult. Most experiments compromise with the "intent to treat" rather than focusing on those who actually use the drug properly. 
- Model the relationship between the 2 quantities above?
  If the drug had no effect, the health outcomes should be indistinquishable between the two groups, holding all other variables constant. Specifically, the health outcomes should be like drawing tickets from the same box without replacement.

These considerations are formalizing our intuition with abstraction and decomposition.
Decomposing the different aspects of "work" into different measurable outcomes and different aspects of health. The abstraction from our variables into the standard "box model" is how we relate different problems back to familiar probability examples.

#### Collecting the relevant data

There are two main questions studied in introductory statistics: how to estimate population parameters properly with sample statistics and how to estimate the impact of a treatment? The formal is concerned with sampling bias and the latter is concerned mostly with confounding. To address these biases, statisticians propose random sampling and random assignment (for treatment vs control) to turn the biases into chance-like error.

In regression we won't talk much about sampling but you should know that the absolute sample size (not the sample size relative to the population) and proper randomization are keys to a quality sample.

In experiments, the reason we cannot simply study people who are using a drug today vs not and measure their outcomes is that confounding variables could explain someone's behavior and their health outcome rather than the drug having an impact on someone's health. The classic example is life style where people with healthy life styles tend to take supplements and also have better health outcomes. Attributing the outcomes to the supplements is ignoring the alternative explanation from the life style. There also may be unknown confounders.

To address this confounding, the most natural approach is to match people with similar life styles, then randomly assign people into treatment vs control. The first step is called "matching" which can handle known confounding issues where the second step can deal with both known and unknown confounding.


In general it's good to think about 3 sources of variability

### Prerequisites - Basic Programming


### What is a model?

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
