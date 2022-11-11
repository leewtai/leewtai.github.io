# Fitting models to data

Using models to extract value from data is one of the key skills that data scientists
need to have. This module will focus on the coding steps without talking about the
"how" or "why" behind modeling.

To solidify the concept of a model, we demonstrate this in terms of an example, a function
factory, and its mathematical formulation.

#### Intuitive example of a model
Commonly, models are used to predict future outcomes.
For example, if we know a student scoring a 80 on the midterm scored 80 on the final and
another student scoring 90 scored around 90 on the final, then a model can help us extrapolate
the final score for a student with a 95 on the midterm:
- A linear model may predict a 95
- A nearest neighbor may predict a 90 (it's possible the final is capped at 90!)

This example shows that models, like a function, take in past records between 2 variables,
midterm and final, then outputs a function that make predictions for the final given
any hypothetical midterm value.

#### Models as a function factories
This is similar to the concept of a function factory, i.e. functions that output other functions:
```python
def function_factory(intercept, slope):
    def line(x):
        return intercept + slope * x
    return line

line1 = function_factory(0, 1)
line2 = function_factory(1, 1)

line1(10)
line2(10)
```

In modeling, the parameters like intercept and slope would be learned from the data, i.e.
chosen by minimizing the disagreement between model predictions and the data, rather than being manually
entered like the example above. But the key is that models are like function
factories, they take in data, X and Y, then return another function. This function
can then take in inputs similar to those in the original X to predict corresponding values
of Y. 

#### Models mathematically

To fit the linear model, $$Y = X\beta + \epsilon$$ where $$Y \in \mathbb{R}^n$$,
$$X$$ is an $$n \times p$$ matrix (over the reals), $$\beta \in \mathbb{R}^p$$, and $$\epsilon$$ is also a length $$n$$
vector. This is a generic formulation for variables with a linear relationship them, similar
to the function factory.

To make predictions for a hypothetical values of $$X^*$$, we denote our prediction for the corresponding $$Y$$ will be $$\hat{Y} = X^* \hat{\beta}$$.
This prediction depends on a speicifed $$\hat{\beta}$$ value. $$\epsilon$$ is often characterized as "noise"
or "measuremnet error" that allows the data points to deviate from a perfect linear relationship. Therefore
our prediction does not include a $$\hat{\epsilon}$$ term.

To find an appropriate $$\hat{\beta}$$, we minimize the squared loss, i.e.
$$\hat{\beta} = \arg\min_{\beta} \|Y - X\beta\|_{2}$$. This optimization step is how we learn the
parameters from the data. We will introduce optimization in coding in a separate module.


## Coding Steps in Practice

In practice, fitting a model to data involves a few common steps:
0. Pre-processing the data, e.g. converting binary labels like treatment/control into 0-1 features
1. Splitting the data, into a testing vs training dataset
   - Pre-processing that only makes sense after splitting the data, e.g. normalizing the features
2. Fitting the model
3. Validating the model

Below we'll cover the topics in the order of fitting models, validating models, splitting the data,
then pre-processing.

Here we simulate data under the linear regression model for clarity:

```python
import numpy as np

# Simulating according to the regression model
sample_size = 100
feature_impact = np.array([1, 0])
num_features = len(feature_impact)
X = np.random.rand(sample_size, num_features)
intercept = 12
measurement_error = np.random.normal(size=sample_size, scale=0.3)
true_Y = intercept + X.dot(feature_impact)
observed_Y = true_Y + measurement_error
```

`feature_impact` is how much the different columns in `X` are impacting `Y`. Notice that we set
one of the features to have 0 impact. Statisticians view all observed data to be contaminated with
noise or measurement error. This allows a flexible model that allows for some misspecification.

#### Fitting the model
To fit a linear regression model given the data `X` and `observed_Y`, we use a model under `sklearn`:

```python
from sklearn.linear_model import LinearRegression

reg = LinearRegression().fit(X, observed_Y)
```

Overall, `LinearRegression()` creates an object with many defaults, like whether to fit an
intercept, that can be changed. We can then immediately call the method `fit()` to find the
best parameters for `X` that minimizes the squared loss with `Y`, i.e. $$\hat{\beta} = \arg\min_{\beta} \|Y - X\beta\|_2$$.

You can view this `.fit()` step similar to passing the intercept and slope into the function factory above.

#### Validating

There are several ways to validate one's model but the common task is to produce predictions
from the model first. If we make predictions using our original inputs, `X`, we will get
what was minimized when the squared loss was calculated.

```python
fitted_values = reg.predict(X)
error = observed_Y - fitted_values
total_squared_loss = np.sum(np.power(error, 2))
```

With predictions from the model, a healthy exercise is to simply plot it against the original
`observed_Y` values.
```python
import matplotlib.pyplot as plt
import seaborn as sns

sns.scatterplot(x=fitted_values, y=observed_Y)
plt.show()
```

A odd problem with selecting the best fitting $$\hat{\beta}$$ is that it fits to our data better than the
true $$\beta$$ values used to generate the data.

```python
true_error = observed_Y - true_Y
ideal_squared_loss = np.sum(np.power(true_error, 2))

assert ideal_squared_loss > total_squared_loss
```

This is **undesirable** because we want the best $$\hat{\beta}$$ to coincide with the true $$\beta$$.
The key here is that our goal is to find the best coefficients that will **generalize** to new datasets,
not fit to our existing dataset. To achieve this, we can either collect new data or split
our original data into training vs testing data. Then the lowest error on the test or new dataset
should coincide with the true $$\beta$$ values much better.

A few common metrics you should know:
- mean squared error (MSE) = $$\frac{1}{n}\sum_i \mid Y_i - \hat{Y}_i\mid^2$$
- mean percent error (MPE) = $$\frac{1}{n}\sum_i \mid Y_i - \hat{Y}_i \mid / \mid Y_i\mid$$
  - This metric is useful when values are small like probability for a rare disease
- mean absolute error (MAE) = $$\frac{1}{n}\sum_i \mid Y_i - \hat{Y}_i\mid $$
- Precision (for 0-1 classification) = $$\mid {i: Y_i = 1 \cap \hat{Y}_i = 1}\mid  / \mid {i: \hat{Y}_i = 1}\mid$$
  - This is useful when the number of incidences, i.e. $$Y_i=1$$, is infrequent relative to $$Y_i = 0$$.
- Recall (for 0-1 classification) = $$\mid {i: Y_i = 1 \cap \hat{Y}_i = 1}\mid / \mid{i: Y_i = 1}\mid$$
  - This is useful when the number of incidences, i.e. $$Y_i=1$$, is infrequent relative to $$Y_i = 0$$.

#### Splitting data
A common technique to split the data is called cross-validation. To understand how our model will
perform on a new dataset, we split the data into 2 exclusive groups: training and testing. 
The training will be used to fit the model, the testing will be used to estimate our model's
accuracy on a new dataset. Since the model has never seen the records from testing, it is as if
we have new data.

```python
from sklearn.model_selection import KFold

kf = KFold(n_splits=6, shuffle=True)

for train_ind, test_ind in kf.split(X):
    print('there are {} train values and {} test values'.format(
           len(train_ind), len(test_ind)))
    train_x = X[train_ind, :]
    train_y = observed_Y[train_ind]
    test_y = X[test_ind, :]
    test_y = observed_Y[test_ind]
```

Some important things to know, as the [`sklearn.model_selection`](https://scikit-learn.org/stable/modules/classes.html#module-sklearn.model_selection)
will show is that cross-validation needs to be modified when you are dealing with different types of
data. The common different types are:
- Imbalanced datasets where the number of positive cases is much smaller than the negative cases, e.g.
  rare diseases. Running naive cross-validation will often have 0 positive cases in either the training or
  testing. To avoid this, we often sample the positive and negative cases separately to ensure
  there are positive and negative cases in the training and testing data. This is called stratified
  sampling.
- Time series or spatial data where there is correlation across records, e.g. weather. Running naive cross-validation
  often over-estimates the performance of your model. This is because the testing data points will likely
  have future data points or unrealistic neighbors in the training dataset. This requires us to
  "block" off the data so our cross validation is representative of our actual use cases, i.e. predicting
  future or distant records.
  

#### Pre-processing

In our example, there wasn't a need to pre-process the data given all the values were defined over the
same range, no missing values existed, and the values were numeric. However, this is only the norm for
pre-processed data in courses or data challenges.

We'll demonstrate some common caveats in our simulated dataset - `bad_input.csv`
```python
import csv
import pandas as pd

demo_df = pd.DataFrame(
    {'sex': ['male', 'male', 'male', ''],
     'class': [1, 2, np.nan, 3],
     'age': [-99999, 20, 20, 40]})
demo_df.to_csv("bad_input.csv", index=False, quoting=csv.QUOTE_NONNUMERIC)
```

Specifically, the errors we've embedded are:
- Missing values
- Inconsistent encoding of missing values
- Missing categories in our data, e.g. `"female"` in `sex`
- Categorical variables encoded as numeric variables, e.g. `class`
- Features with different units (this matters to some algorithms)

Something not obvious is the **order** in handling these issues could matter. For example, `pandas.DataFrame.fillna()`
allows us to "handle" the `NaN` values quickly and uniformly. However, we may want the categorical features to
introduce an `"unknown"` category instead for gender, want to impute the `class` with the most common value, or
simply keep them as `NaN` values and let the algorithm defaults handle them. Overall, pre-processing should
be thouhgt of as part of the modeling that can have consequential impact on the final result.


- Handling inconsistent encoding of missing values. It's common to addrses this when reading in the file.
  ```python
  demo_df = pd.read_csv("bad_input.csv", na_values=[-99999, ''])
  ```
- Handling missing values can be done with `pandas.DataFrame.fillna()`, we will intentinally leave some columns
  untouched, which will likely result in those records being dropped in most algorithms.
  ```python
  demo_df.sex.fillna('unknown', inplace=True)
  ```
- Converting qualitative variables into multiple 0-1 columns.
  ```python
  from sklearn.preprocessing import OneHotEncoder
  
  qual_vars = ['sex', 'class']
  enc = OneHotEncoder(
      categories=[np.array(['female', 'male', 'unknown']),
                  np.array([1, 2, 3])],
      drop='first',
      handle_unknown='ignore').fit_transform(demo_df.loc[:, qual_vars])
  qual_array = enc.toarray()
  ```
  The reason for dropping the first column is a topic covered in linear regression regarding identifiability
  issues. Note that our data here does not have a `female` record so we'll have issues between `male` and `unknown`.
- Normalizing the data, here's an example of using `numpy` to normalize the data such that the mean is 0
  and the standard deviation is 1.
  ```python
  std_age = (demo_df.age - np.nanmean(demo_df.age)) / np.nanstd(demo_df.age)
  ```
  It is important to know that normalizing should happen AFTER splitting the data. Although normalizing should happen
  to the "new data" before applying the model, the normalizing values used should be from the training dataset.




{% include lib/mathjax.html %}
