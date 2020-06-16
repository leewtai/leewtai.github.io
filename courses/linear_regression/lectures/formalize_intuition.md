# Formalizing Intuition into an Equation

One of the key skills of an applied statistician or data scientist is the
ability to formalize, mathematically and programmatically, people's intuition.

This sounds complicated but its application is quite familiar
to the general public. When we go for a physical exam, there's an abstract concept of health that
we often formalize into statistics like Body-Weight-Index, blood pressure,
lung capacity, etc. In gymnastics, there are judges who score the
completion of the different routines. In a tech company, there are metrics
like pageviews, likes, numebr of followers etc. The goal of these
metrics is to provide guidance for monitoring and optimization for various
problems. The formalization of these applications often require a partnership
between domain expert with a quantitatively minded person. Here we will focus
mostly on the quantitative side of topics.


## How is this related to regresion?
One of the most familiar applications of regression is when people use the
"best fit line" functionality in Excel or Google Spreadsheets. Behind the scenes,
a regression calculation is being performed. But have you wondered what
does "best fit" mean? We will explain this below.

## Starting from the histograms and summary statistics
Below is a histogram of some people's weights. What would you say is the
"typical" person's weight?

![histogram of weight]()
To plot this data yourself, please find the data from [HERE]()

Most people would eyeball this hisrogram and be able to point to roughly the same
region but likely not same exact location. Ultimately, ten different people would
have ten different answers, which one should we choose? This is why the mathematical
formalism is necessary.

If you ask people how they arrived at their answer, the immediate answer is likely
they did not think much about it. But once you start asking about alternatives
to their chosen answer, people will often start explaining their intuition. A
common one for histograms is that they're trying to balance the points to
the left and right of the chosen answer.

How would we define "the points to the left"? Let's start with programming first:
```python
import pandas as pd

mlb = pd.read_csv("mlb_height_weight.csv")
mlb.head(3)

chosen_location <= 150

left_of_choice = mlb.weight < chosen_location
records_to_left = left_of_choices.index
```
There are a few choices that we made above:
- `chosen_location` was arbitrarily set to some plausible value
- For "points to the left", we actually used the "indices"
- By convention, we assumed "to the left" meant "smaller". But for later reasons,
  we will define this as "smaller or equal"

Let's now translate that into math!
To formalize this concept, we would need to first define some notation:
- Let $$i$$ be the index of the subject and $$i$$ could take any value within the set $${1, 2, \dots, n}$$.
  You can imagine that we assigned everyone a number starting at $$1$$ and exhausted our data at $$n$$, i.e.
  $$n$$ is the sample size.
  - The $${}$$, curly bracket notation is just indicating that this is a collection of values.
    Similar to programming, a single scalar is different from a collection of values. 
- Let $$W_i$$ be the weight of subject $$i$$
- Let $$a$$ be the arbitrary chosen location

Given this notation, the simplest form to describe all the records with weight smaller than $$a$$ would be

$${j: W_j <= a}$$

Do not worry too much if you do not understand this expression immediately. In words, it represents the collection
of indices such that (i.e. $${j: CONDITION}$$) the weight associated with that index (i.e. $$W_j$$) is smaller or
equal to (i.e. $$<=$$) the chosen location (i.e. $$a$$).

Notice the similarities between the mathematical and programming translation, both had
to separate the definition of a single scalar vs a collection of values, both had to
separate the concept of the subject vs the weight of the subject, also both had to represent
the potential solution. These are important concepts to know before continuing with this course.

Seeing this mathematical translation, we could also avoid choosing a value for `chosen_location`
if we rewrote our programming translation using a function. In other words, we want to write a function
that takes in a chosen location, then returns the indices to the left.

```python
def record_on_left(a, values):
    left = values <= a
    return left.index
```

Now we have defined "points to the left", let's continue translating the idea of "balancing the
points to the left and right". The word "balance" can be interpreted in multiple ways which
again requires some formalism. Does balancing imply the number of data points are equal, does a point
far to the right balance out 2 closer points to the left?

A popular choice here is to balance the squared distances to the left to the squared
distances to the right. To express this mathematically, this would look
like, the optimal value $$a^*$$ could be expressed as the point where the following is true:

$$\sum_{j \in {j: j\leq a^*} (W_j - a)^2 = \sum_{j \in {j: j> a} (W_j - a^*)^2|$$

To code this idea up, we could compute the squared distances then return whether the right and left values equal.
```python
import pandas as pd


def left_equal_right(a, weights):
    left = weights <= a
    sq_dist_left = (weights[left] - a)**2
    sq_dist_right = (weights[~left] - a)**2
    diff = sq_dist_right - sq_dist_left
    
    return abs(diff) <= .Machine.double_precision


mlb = pd.read_csv("mlb_height_weight.csv")
left_equal_right(150, mlb.weights)
left_equal_right(160, mlb.weights)
left_equal_right(170, mlb.weights)
```

The above code is not incorrect but notice that most of your attempts will return `False`.
Hopefully you felt a slight irritation in the lack of information whether your current guess
is too large or too small and whether you are close or far from the optimal choice.

Mathematically, it turns out that the optimal $$a^*$$ that obtains the same left and right squared distances
is equivalent to minimizing the total squared distances from both sides. In other words, 
for any other location, $$b$$:

$$\sum_{j=1}^{n} (W_j - a^*)^2 <= \sum_{j=1}^{n} (W_j - b)^2$$

Another way to express this is

$$a^* = \arg\min_b \sum_{j=1}^{n} (W_j - b)^2$$

From your introduction statistics course, you might recall one of these expressions described as the "least squares"
and that the mean (average) satisfies this property! In mathematical terms, define the mean as $$\bar{W} = \frac{1}{n}\sum_j W_j$$,
then this satisfies the least square condition:

$$\sum_{j=1}^{n} (W_j - \bar{W})^2 <= \sum_{j=1}^{n} (W_j - b)^2$$

for any other competing alternative value $$b$$. 

It requires a little calculus to show that this is
true but the key is to realize that the mean minimizes a certain objective. If we changed
the objective, the mean may not be the optimal location anymore. Recall that we had choices
when we were defining the concept of balancing, another popular objective is to replace the squaring
operation with the absolute value operation:

$$a^* = \arg\min_b \sum_{j=1}^{n} |W_j - b|$$

An objective achieved by the median.

These formalized expressions allow us to understand why the mean is more
sensitive to outliers than the median. This is because the squaring operation will
penalize outliers more than the absolute value so the mean will change more relative to the
median if you introduce outliers.

To wrap up this subsection, the mean and median are both valid choices that "balancing the data
to the left and right" under different objectives. These formalized objectives are
necessary to avoid any confusion in the final answer. From an academic standpoint,
these formalisms also allow us to derive many other properties.

## From the mean to the regression line
Before we were summarizing the histogram with a mean, now what if we are trying to
summarize a scatter plot?

![graph of weight by height]()

Imagine drawing a line through the scatter plot, many people would draw similar yet
different lines through this point cloud. To capture each of these possible alternatives,
we need a general yet formal expression for all the possible lines. If you recall
from geometry, all lines can be written as $$Y = a + b * X$$ where $$a$$ represents
the intercept and $$b$$ represents the slope. Conceptually, this is equivalent to
our arbitrary location, $$a$$ before in the histogram example.

To summarize the data in the best fashion, we need to formalize an objective.




Turns out 

$$\arg\min_(a, b) \sum_{j=1}^{n} (Y_j - (a + b* X_j))^2$$


A running theme will be the translation from 

## Concepts
- indices vs values
- collection of values vs scalar values
- formalism as mathematical equations

{% include lib/mathjax.html %}
