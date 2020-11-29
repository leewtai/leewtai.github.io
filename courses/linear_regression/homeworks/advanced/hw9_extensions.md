# Homework 9: High Dimensional Regression + Instrumental Variables

## High dimensional regressions

For lecture 16, we've used a dataset from NOAA to demonstrate PCA. In this homework, we will contrast the various high dimensional regression techniques using this dataset.
The dataset is available on Canvas `/Files/Data/cleaned_tmax_201001_201905.csv`, the data is the monthly average of the daily maximum temperature from 2010 Jan to 2019 May. 
Each row represents a month/year where each column represents a different weather station in the US. The data is in chronological order where the first record is 2010 Jan and the final record is 2019 May. The data are in units of 0.01 Celsius (i.e. divide by 100 to get Celsius). 

#### Question 1
How many stations have missing data in our dataset?
Side note: in general you want to check whether the missing data has a certain pattern that could suggest bias that could influence your final model but we will not do that here.


To continue the following problems, please follow the instructions:
- remove the stations with missing values before answering.
- extract the station "USH00487388" as our dependent variable and the remaining stations as independent variables.
- For context, pretend that the last 12 records of Y are missing (i.e. a year's worth of data) and we need to now impute the values using the other stations. You can call the last 12 records as your test set and the rest as your train set.

#### Question 2
True/False, we need to center and scale the independent variables for this problem otherwise performing PCA would be dominated by outliers.

#### Question 3
Perform SVD on the train set for the independent variables and plot the ratio of the total of the first k eigen values relative to the total of all eigen values.

#### Question 4
Using the training data, calculate $$W=XV_2$$, i.e. the new features using only the first 2 eigen vectors. Since $$X$$ was in chronological order, the same should hold for $$W$$. 
- Please plot the time series of the first and second column of $$W$$ on the same plot (no need to label your axis) with a horizontal line corresponding to the value 0.
- Report the period you observe in the data, i.e. how many records until a repeated pattern appears again.

Side note, you should be able to tell which line corresponds to the first vs second eigen vector judging by the magnitude of these lines.

#### Question 5
Please fit a regression using the training data using PCA on $$X$$ and $$Y$$ (when unspecified like now, you should include an intercept). 
To make a prediction, you'll need to create $$W_{test} = X_{test} V_2$$, where $$V_2$$ is based on your training data alone. Please report $$\sqrt{\frac{1}{|Test|}\sum_{i\in Test} |Y_i - \hat{Y}_i|^2}$$ to 6 decimals as your prediction error.

Side note, depending on your problem, sometimes it's feasible to perform SVD on the training and testing data collectively. Given the prediction error is an estimate of how well you'll do on new data, the question is whether you'll be able to train your PCA features every time new data arrives (usually not).

Side note, when you report a number, you should always ask yourself whether it's reasonable or not.

#### Question 6
- True/False, would changing the units to Celsius change the graph from Question 3?
- True/False, would changing the units to Celsius change the graph from Question 4?
- True/False, would changing the units to Celsius change the prediction error from Question 5? 

#### Question 7
Perform Lasso regression using the training data (i.e. the choice of the tuning parameter should be done only using the training data) and report the same prediction error as above.

Hint: if your best tuning parameter is one of the boundary values, it probably means you should adjust the range of your tuning parameter.

#### Question 8
Perform Ridge regression using the training data (i.e. the choice of the tuning parameter should be done only using the training data) and report the same prediction error as above.

Side note, you cannot perform the usual cross validation with temporal data without some assumptions. This goes beyond the scope of this class.

## Instrumental variable

#### Question 9
In the context of instrumental variables, we have 
- $$Y=\beta_0 + \beta_x X + \beta_z Z + \epsilon$$ where $$Z$$ is unobserved
- $$X=\alpha_0 + \alpha_w W + \alpha_z Z + \rho$$ where $$W$$ is the instrument and $$Z$$ is the confounder.
- Let $$W = \mu_w + \gamma$$
- Let $$Z = \mu_z + \zeta$$
$$\epsilon$$, $$\rho$$, $$\zeta$$, and $$\gamma$$ are all independent, random, and unobserved error terms with mean 0. $$\mu_w$$ and $$\mu_z$$ are both constants like other parameters.

We can obtain an unbiased estimate using a 2 stage regression, i.e. regress $$X$$ on $$W$$, then regress $$Y$$ on the fitted values from the first regression. 
Using the notation here, give an example when we can simply regress $$Y$$ on $$W$$ to obtain an unbiased estimate for $$\beta_x$$ (this can be one sentence).

{% include lib/mathjax.html %}
