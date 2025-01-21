# HW1 - Reviewing prerequisites

### Context - Olist E-commerce data
Please find the dataset on Kaggle named ["Brazilian E-Commerce Public Dataset by Olist"](https://www.kaggle.com/olistbr/brazilian-ecommerce).
The goal is to refresh your computing and statistics basics with this homework.

#### Q1 basic data checks

For each of the following statements, please write a short paragraph that explains
your logic and data to verify this question.

- Does each order correspond to a single payment? 
- Does each customer make at least one payment?

#### Q2 understanding the orders

Please plot the relationship between "order value" vs "the number of unique products" for
each order in the dataset. You should decide what is the most appropriate graphic given
the dataset.

#### Q3

Please visualize the temporal pattern of Olist orders. Are there seasonal patterns
like in the US, e.g. Christmas?

#### Q4

Do the 2 largest cities, defined by total order amount, have different "total order payment" distributions?
Please perform a permutation test to test this statement.

#### Q5

Try to predict the time for an order to be delivered after it was paid for using a basic regression model.
- Define a relevant metric for this, should arriving early be treated the same as arriving late?
- Make sure you perform cross validation
- Are there features that were helped your model performance metric by 2% or more?

WARNING: there are some bad data points you'll have to make a decision how to handle the data (e.g. if no delivery was ever made)


{% include lib/mathjax.html %}
