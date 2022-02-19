# Numpy

Numpy is the package that enables fast matrix computation in Python.

Numpy has 2 main features, the numpy.array data type and several
functions that are extremely efficient with numpy arrays.

## Numpy array

You can think of a numpy.array as a matrix, with rows, columns, and
each cell has a basic data type in it.

Numpy arrays can be created manually or sourced from a file.

- Generating a 2D (3 by 2) numpy arrays from a list of lists.
  Notice that the lists were stacked by rows.
  ```python
  import numpy as np

  demo1 = np.array([[1, 2], [3, 4], [5, 6]])
  demo1.shape
  print(demo)
  ```
- Generating 2D numpy arrays with 200 $Normal(0, 1)$ random numbers
  to simulate data.
  ```python
  import numpy as np
  
  demo2 = np.random.normal(loc=0, scale=1, size=(100, 2))
  ```
- Generating an array of 0's or 1's as default values. The argument
  specifies the dimension of the array.
  ```python
  import numpy as np
  
  demo3 = np.zeros((3, 2))
  ```
- Reading in a 2 by 3 [CSV file](data/demo.csv).
  ```python
  import numpy as np

  demo4 = np.loadtxt("demo.csv", delimiter=",")
  ```
- Creating values incrementing by a certain amount. Notice
  that the top value does not get created.
  ```python
  import numpy as np

  demo5 = np.arange(0, 1, 0.1)
  ```


#### A single numpy array can only hold one type of data

An important feature of numpy arrays is that each array
can only hold a single data type, unlike lists/dictionaries/tuples
that can hold multiple data types.

This seemingly restrictive choice allows numpy arrays to run very fast.
To check the data type within the array we check the `np.array.dtype`
attribute.
```python
demo2.dtype
```

Another common attribute is the shape, i.e. the number of rows and
number of columns of the array.
```python
demo2.shape
```

#### Subsetting numpy arrays
Subsetting numpy arrays similarly uses the square brackets `[]`.
However, since we have rows and columns now, we subset for them
together.

Subsetting with integers, the first value indicates the row (3rd row),
and the second value represents the column (2nd column).
```python
demo1[2, 1]
```
Similar to lists, we can slice a segment of values using `:`.
```python
demo1[1:, 1]
demo1[:1, 0]
demo1[:, 0]
demo1[0, :]
```

If we subset with boolean arrays, the boolean array provided for the row
must have the same size as the number of rows. The columns work similarly.
```python
# Creates a boolean array
small_col1 = demo1[:, 0] < 2
# Subset the rows using a boolean array
demo1[small_col1, :]
```

#### Special values
Two important special values in `numpy` are `numpy.inf` and `numpy.nan`.

The first is the infinite value, which operates as expected.
```python
1 / np.inf
2 + np.inf

np.inf - np.inf
```

The second is the `numpy.nan` value which is commonly used for missing
values. This value is unique becaues any value aggregated with it will
become another `numpy.nan` value. This is useful because it'll be clear
when there are missing values in the data.

```python
np.nan * 2
np.nan + 1

# max/min ignores nans
max(2, np.nan, 5, -3)
```

#### Common methods
We will demonstrate some of the common methods using the demos above.

- `numpy.array.reshape()` Often we want to "reshape" the matrix so the
  dimensions work in our favor. Notice that order this happens in.
  ```python
  demo1_reshaped = demo1.reshape(2, 3)
  demo1_reshaped = demo1.reshape(2, -1)
  ```
  `-1` asks `numpy` to figure out the size of the remaining dimension
  such that no data is loss.
- `numpy.array.sum()` adds everything up `demo1.sum()`
- `numpy.array.T` takes the matrix transposes of the array.
- `numpy.array.dot()` takes the dot product and can be chained nicely.

## Numpy functions

Numpy has a lot of mathematical functions built-in to it.
- `np.matmul()` performs matrix multiplication
- `np.hstack()` or `np.vstack()` stack the the lists of equal length
  into an array.
- `np.isnan` and `np.isinf` are useful to detect if there are `np.nan`
  or `np.inf` values.
- `np.where()` returns the indices that correspond to `True` in a boolean
  array. `np.where(np.array([1, 2, 3]) > 2)`
- `np.logical_not()` negates a boolean array, `np.logical_not(np.array([True, False]))`
...

#### Applying functions along a column or row

A common calculation with tabular data is to calculate the same summary
statistic for each column or row in the data. Rather than writing a loop,
`numpy.apply_along_axis()` allows a concise way to do this.

Below we calculate the sum for each column, i.e. along the rows. To remember
which axis is 0, just recall that when calling `np.array.shape` that the first
value, i.e. 0'th index, corresponds to rows.
```python
import numpy as np

col_sum = np.apply_along_axis(np.sum, 0, demo)
print(col_sum)
```

If we changed the axis to `1` then we would have obtained the row totals instead.

#### Broadcasting

Broadcasting is how numpy distributes calculations across arrays that can be
of different sizes. This is often orders of magnitude faster than running
loops. A common usecase is to calculate pairwise distances between two arrays.

- An array of arbitrary size operated with a single value will
  distribute that calculation to each element in the array.
  ```python
  demo1 = np.array([[1, 2], [3, 4], [5, 6]])
  demo1  - 2
  ```
- An array of arbitrary size operated with an array that has
  dimension size 1 in one dimension and shares the dimension size
  on the remaining dimension, will act as if the smaller array
  was replicated until it matches the larger array
  ```python
  demo1 = np.array([[1, 2], [3, 4], [5, 6]])
  demo1 * np.array([[1, 2]])
  demo1 - np.array([[1], [3], [5]])
  ```

{% include lib/mathjax.html %}
