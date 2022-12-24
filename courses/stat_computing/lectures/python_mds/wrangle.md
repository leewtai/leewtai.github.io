# Wrangling data for different purposes

People used to say that data wrangling was the most time consuming topic in data scientists'
day-to-day job. You likely also heard that many data startups' main value proposition is
around saving people's time with data wrangling. Regardless, the data scientists who are
exploring new frontiers of data likely will still be wrangling data for years to come.

## What is data wrangling?

Data wrangling is essentially the code that makes the data, from its current state, usable for
your problem at hand. This problem appears because the optimal format for storage is often
different from the optimal format for analysis, leading to a translation task between the two.

For example, to analyze productivity of a farm, we often look at yield, i.e. the amount of food
produced divided by the amount of land used (acrage). The amount of land used is known early on 
from the planting data that also includes the timing of planting, the type of seeds planted,
the amount of seeds planted, etc. The optimal format for storage requires flexibility for
different types of data and storage efficiency (e.g. avoiding repeated values), in other words, not
in a tabular format.

On the other hand, analysis would want the acrage on the same row as the production 
number, having a single number that represents planting and another for harvest (often planting
and harvesting can span over multiple days).
Here we optimizing for structure in the data that allows us to perform consistent analyses on the data.

## Common wrangling tasks

Wrangling is often considered something you will learn on the job. The skills required
are a familiarity with different data types, in particular, how to construct, subset, and aggregate values from them.

#### Long to wide

One of the most common tasks is the translation between long and wide datasets, also known as pivoting.
Long and wide datasets are both rectangular data formats but long format data often stores a single
measurement per row where a wide format would store multiple measurements per row that are related
to the same entity. For example

Example long data:

|patient_id|variable|value|units|
|-------|--------|-----|-----|
|1|'height'|178|'cm'|
|2|'height'|166|'cm'|
|1|'weight'|80|'kg'|
|1|'age'|40|'year'|
|2|'age'|30|'year'|

Contrasting this to the equivalent form of wide data where each row is an individual

|patient_id|height_cm|weight_kg|age_year|
|1|178|80|40|
|2|166|NaN|30|

To accomplish this task we use the following code:
```python
import pandas as pd

long_df = pd.DataFrame([
  {'patient_id': 1, 'variable': 'height', 'value': 178, 'units': 'cm'},
  {'patient_id': 2, 'variable': 'height', 'value': 166, 'units': 'cm'},
  {'patient_id': 1, 'variable': 'weight', 'value': 80, 'units': 'kg'},
  {'patient_id': 1, 'variable': 'age', 'value': 40, 'units': 'year'},
  {'patient_id': 2, 'variable': 'age', 'value': 30, 'units': 'year'},
])
long_df['var_w_units'] = long_df.apply(lambda x: x['variable'] + '_' + x['units'], axis=1)

wide_df = pd.pivot(long_df,
    index='patient_id', columns='var_w_units', values='value').reset_index()

print(wide_df)
```

- We first created a new column named `var_w_units` so we would have the appropriate
  labeling. This would also allow us to detect issues with different units for the 
  same variable if that exists.
- We'll use the [`pandas.pivot`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pivot.html) function to perform our pivoting. There are a few different pivot functions. My recommendation is to stick to one of them and be familiar with its behaviors (especially when there is missing values).
- The `index` argument defines the "rows" in the wide data frame, i.e.
  what dimension will constitute a single record. In this case, a single record
  is all the data associated with the same `patient_id` number.
- The `columns` argument defined the "columns" in the wide data frame. Each unique
  value will become a new column. You may think of these as the "features" in your data.
- The `values` argument defines the "entry/elements" in the wide data frame.
- If the same row/column has multiple values associated with it, a `ValueError` will be
  raised. This issue must be resolved using information about the domain + data creation
  process.
- Resetting the index just makes sure that the `patient_id` is stored as a regular column
  rather than an index.

#### Wide to long
Continuing our example from above, we could convert the wide data frame back to its long
format. This can be necessary either because of package requirements (e.g. "tidy data")
or it is easier to convert into a different wide format by first converting it back to
a long format.

```python
non_id_cols = [col for col in wide_df.columns
                if col != 'patient_id']
long_df2 = pd.melt(
    wide_df,
    id_vars='patient_id',
    value_vars=non_id_cols)
long_df2['variable'] = long_df2.var_w_units.apply(lambda x: x.split('_')[0])
long_df2['units'] = long_df2.var_w_units.apply(lambda x: x.split('_')[1])
long_df2.drop(columns='var_w_units', inplace=True)

print(long_df2)
```

#### Hierarchical data to tabular data
could be a simple statistic (e.g. how many users do we have?)
to something more complicated (e.g. please predict the lifetime value of a new customer).


There is no way we can have a comprehensive overview of data wrangling but here are some
examples for you to understand why this is the case.


## How to think about data wrangling?
The best way to approach data wrangling is to have a clear picture of your data in its
current state and its eventual state. 


{% include lib/mathjax.html %}
