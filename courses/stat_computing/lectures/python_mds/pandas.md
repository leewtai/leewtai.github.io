# Pandas - Handling tabular data with mixed data types

`numpy.array` forces the data type for every value to be the same, this creates issues
when the data has both numeric **and** categorical information
(e.g. sex, occupation etc).

Although all algorithms ultimately only work with numeric values, e.g. by
converting categories into counts or a collection of 0-1 columns, the data is rarely ever encoded in
that format. For example, the variable `gender` is commonly coded as `M`, `F`, `Other`,
`NA`. Then most algorithms will create multiple columns/variables **like**
`gender_is_M`, `gender_is_F`, `gender_is_Other` where each is 0 or 1 depending
on the actual value of `gender` (`gender_is_NA` is often not created for statistical
reasons).

The 0-1 flags, however, are hard to explore since users often handled the values jointly.
This becomes very awkward when there are multiple categorical variables that have different
number possible values. Given these usecases, a new data type was necessary since
`numpy`'s speed depends greatly on the single data type constraint.

`pandas` is the package that provides a data type `pandas.DataFrame` that can solve this issue!
To introduce the data frame, we'll use the [train.csv from the Titanic dataset on Kaggle.com](https://www.kaggle.com/c/titanic/data?select=train.csv)
as an example.

```python
import pandas as pd

df = pd.read_csv("train.csv")
```

## Pandas data frame Attributes

A `pandas.DataFrame` is similar to a `numpy.array` in it often has 2 dimensions.
- The columns often represent the different features/variables in the data. These
  are often labeled by the column names (called `columns`) which is often provided
  by the first row in a CSV file.
  ```python
  df.columns
  # Index(['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
  #        'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'],
  #       dtype='object')
  ```
- The rows often represent different records in the data. These are often labeled
  by something called `index` which defaults to the row number in the
  CSV file.
  ```python
  df.index
  ```
- To get the size of the data frame, pandas preserved the same attribute as `numpy`
  ```python
  df.shape
  ```
- We can also access any of the columns (all rows) as an attribute. This will return
  a `pandas.Series`
  ```python
  surv = df.Survived
  ```

#### Subsetting a Data Frame

Similar to `numpy`, we generally subset data frames by columns and rows. 
However, since data frames have additional features, they need to be subsetted
using particular methods with different types of data.
- `pandas.DataFrame.head`, allows us to look at the first few rows of data.
  ```python
  df.head()
  ```
- `pandas.DataFrame.loc`, which allows us to subset using boolean Series
  ```python
  cheap_tickets = df.Fare < 5
  cheap_df = df.loc[cheap_tickets, ]
  ```
- `pandas.DataFrame.iloc`, which allows us to subset by the row position and
  column position. Here we will grab the first 3 rows and first 3 columns
  from the data frame we got above. Notice that the `index` (179, 263, and 271)
  retained the values from `df` instead of restarting at 0 again.
  ```python
  cheap_df.iloc[:3, :3]
  #        PassengerId  Survived  Pclass
  # 179          180         0       3
  # 263          264         0       1
  # 271          272         1       3
  ```
- `pandas.DataFrame.loc` also allows us to subset using index values
  and column names.
  ```python
  cheap_df.loc[:263, ['Survived', 'PassengerId']]
  #      Survived  PassengerId
  # 179         0          180
  # 263         0          264
  ```
  Notice that `:263` which usually subsets for the first 263 records, now returned
  all the records until the `index` value that corresponded to 263. In the data
  frame `cheap_df`, this returned only 2 rows. This shows that
  the `index` **may not always correspond to the row number**.

#### Each column is a pandas.Series

We hinted that each column in a data frame is a `pandas.Series`. These work similarly to
`numpy.array` where all values share a data type and methods exist to calculate
summary statistics on these.

```python
df.Fare / 10            # returns a pandas.Series with each value divided by 10
df.Fare.mean()          # calculates the mean
df.Age.isna().mean()    # calculates the frequency of NaN values
df.Sex.value_counts()   # calculates the frequency of each possible value
df.Fare.argmax()        # returns the row number with the largest value
df.Age.fillna(df.Age.mean()) # Replaces all the NaN values with the average
```

Many of these methods **also apply to the data frame** although this is
generally discouraged because data frames often have mixed data types.

#### Creating a Data Frame

There are 2 main ways you'll get a pandas data frame:
- Reading it from a file using `pandas.read_csv()`
  ```python
  import pandas as pd
  df = pd.read_csv("demo.csv")
  ```
- Creating it from scratch
  ```python
  # A dictionary of lists
  df = pd.DataFrame({'a': [1, 2], 'b': [5, 6]})
  # A list of dictionaries
  df1 = pd.DataFrame([{'a': 1, 'b': 5}, {'a': 2, 'b': 6}])
  ```

#### Merging/Joining 2 Datasets

Sometimes we have information across 2 different datasets but we want
combine them, e.g. combining the geographic information of a city and
the health statistics of a city allows us to plot the health statistics
on a map for easy comparisons.

This operation is often called a "join", a word from SQL. The records
that share a key across the two datasets will be merged. In pandas, 
the parameter `on` lets us indicate which columns the datasets will be
merged on. To demonstrate the different merges, we will show use the
following example, notice `city` is shared across both datasets but
the values under city do not fully overlap.

```python
a = pd.DataFrame([{'city': 'new york', 'lon': 100},
                  {'city': 'san francisco', 'lon': 120}])
b = pd.DataFrame([{'hospital': 'A', 'city': 'new york', 'beds': 90},
                  {'hospital': 'B', 'city': 'new york', 'beds': 20},
                  {'hospital': 'A', 'city': 'austin', 'beds': 210}])
```

- Inner join (the default), will only merge records that exist in
  both datasets. Notice that duplication will happen when there are
  multiple matches.
  ```python
  a.merge(b, on='city')
  #        city  lon hospital  beds
  # 0  new york  100        A    90
  # 1  new york  100        B    20
  ```
- Outer join, will keep all records across both datasets. Missing
  values will all be filled in with NaN.
  ```python
  a.merge(b, on='city', how='outer')
  #             city    lon hospital   beds
  # 0       new york  100.0        A   90.0
  # 1       new york  100.0        B   20.0
  # 2  san francisco  120.0      NaN    NaN
  # 3         austin    NaN        A  210.0
  ```
- Left join, will keep all records on the left, i.e. the data frame
  that we call `merge()` on.
  ```python
  a.merge(b, on='city', how='left')
  #             city  lon hospital  beds
  # 0       new york  100        A  90.0
  # 1       new york  100        B  20.0
  # 2  san francisco  120      NaN   NaN
  ```

#### Applying a function across rows or columns

Similar to `numpy`, we can "apply" the same function across multiple
rows or columns without explicitly calling a for-loop.

- Calculating the number of unique values in each column
  ```python
  df.apply(lambda x: x.unique().shape[0], axis=0)
  ```
  Here we used a `lambda` function, which is a function that we are passing
  to the function `pandas.DataFrame.apply()` without defining it properly with `def`.
  Ultimately, each column is treated as `x`, and for each column we call the
  method `pandas.Series.unique()` chained by obtaining the attribute `pandas.Series.shape`.
  Notice `apply()` is called as a method on the data frame so the data used
  is the entire data frame.
- Changing the `axis=0` to `axis=1` will apply the function on each row.

#### Grouping
A rather handy feature with pandas is its ability to partition the data frame into
groups according to certain features. For example, we can group the data by `Sex` and
`Pclass` then perform certain calculations.

```python
df_grp = df.groupby(['Sex', 'Pclass'])
df_grp.Survived.mean()
# Sex     Pclass
# female  1         0.968085
#         2         0.921053
#         3         0.500000
# male    1         0.368852
#         2         0.157407
#         3         0.135447
```

For more custome calculations, `df_grp.groups` is an attribute that is a dictionary
containting the group label as the key and the `index` of all recorsd belonging to
the group.

```python
for grp, inds in df_grp.groups.items():
    surv_rate = df_grp.get_group(grp).loc[:, 'Survived'].mean()
    print('Survival rate for group with Sex {} and Pclass {} is {}%'.format(
        grp[0], grp[1], round(100 * surv_rate, 2)))
    
```
