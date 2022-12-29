# Debugging

Now that you've done a bit of coding, it might help to learn a few tricks about debugging
your program.

What's important in this chapter is also the ability to generate quick examples to reproduce errors.

## Understanding the error messages

The most common errors a beginner will see are:
- Errors related to typos OR you're referring to something (variables/attributes/methods) that
  is defined else where (e.g. inside a function, in a different type of objects, etc). For example:
  - `NameError` where there's likely a typo in the name or a variable is defined
    inside a function but not outside the function.
    ```python
    # Scope
    def x_times_2(x):
      X = x * 2
      return X
    x_times_2(0)
    print(X)

    # Typo
    print(X_times_2(0))
    ```
  - `AttributeError`: where you are calling a method or attribute from a variable but
    you either have a typo or the variable is not of the type you're expecting.
    ```python
    bad_tuple = (1) # should be (1, )
    bad_tuple.count(1)
    ```
- Basic syntax violations with Python:
  - `SyntaxError`: Python cannot understand your command because it does not follow its rules
    ```python
    (1 2)

    for i in range(10)
        print(i)
    ```
    It might be tempting to think Python should just fix your code for you for these but sometimes
    the suggestions are not appropriate and we would rather things to fail.
  - `IndentationError`: this can be viewed as a specific case of SyntaxError where your indents
    do not make sense.
    ```python
    if 3 < 1:
    print('true')
    ```

- Errors related to illegal operations. This likely means you need to convert
  the data to the correct type or you need to re-examine the type of objects you
  have.
  - `TypeError`: where an operation is applied to the wrong "type" of data, e.g.
    ```python
    1 + '2'
    abs('hello')
    ```
  - `ValueError`: where the type of data is correct but the value is illegal.
    ```python
    import numpy as np
    np.array([1, 2]) + np.array(1)  # Works!
    np.array([1, 2]) + np.array([1, 2])  # Works!
    np.array([1, 2]) + np.array([1, 2, 3])  # Does not work!
    ```

Understanding these different type of errors in your context would be key to debugging.

### Failing fast is good!
In general, seeing error messages is good! It means you are trying and
there are easy mistakes to fix!

## The worst errors do not produce error messages
It is important to know that not all errors result in an error message.

Here is a common mistake that produces no error message.

```python
def is_positive(x):
    is_pos = [xi > 0 for xi in x]
    answer = 'negative'
    if is_pos:
        answer = 'positive'
    return answer

is_positive([1])
is_positive([-1])
```

This code is incorrect because we would want `[-1]` to return negative.
But more importantly, the desired behavior is another list, the same
length as the inputs, reflecting if each element is negative or positive.

The only time `is_pos` will return `False` in this case is if `x` is an
empty list. Try `bool([])` for why this is the case!

Surprisingly, if we converted the input to `numpy.ndarray`, we would get
helpful error messages, i.e. the True/False status of an array is ambiguous!
Sadly, its suggestion for fixing the error is not correct for this particular
example.

The code really should be something like:
```python
import numpy as np

def is_positive(x):
    if not isinstance(x, np.ndarray):
        x = np.array(x)
    return np.where(x > 0, 'positive', 'non-positive')


is_positive([1, -1])
is_positive([-1])
```

## Creating test cases
To prevent issues like the one above is to create test cases, i.e. examples with
known solutions to test the correctiness of the code. This unfortunately just helps
with identifying the correctness but does not fix your code.

For example
```python
input_output = [
  {'input': [1, 2, 0, -1],
   'expected_output': ['positive', 'positive', 'non-positive', 'non-positive']},
  {'input': 1,
   'expected_output': ['positive']},
  {'input': 1,
   'expected_output': ['positive']},
  {'input': -1,
   'expected_output': ['non-positive']},
  {'input': 0,
   'expected_output': ['non-positive']},
  {'input': np.nan,
   'expected_output': [np.nan]}]

for i, case in enumerate(input_output):
  print(i)
  output = is_positive(case['input'])
  try:
      check = (output == case['expected_output']).all()
  except AttributeError as e:
    print('could not perform check')
    break
  assert check
```

The code above should show that the case with NaN values caused the except statement to trigger. This should inform us that the code should handle the case when NaN values are introduced.

There is a whole framework of coding called "test driven development" if you want
to learn more from this perspective. Python also has many testing frameworks that makes testing a lot more automated. In general, it's impossible to cover all edge
cases.

## Identifying the location of the error

The location of an error is often printed in the error message but this sometimes
is not the true cause of the error.

For beginners, I recommend using something similar to the test cases above and double check if objects are behaving as expected when running the code line by line.

To do this, often you may need to unindent your code and fix your for-loop at a specific iteration, remove the function initiation and `return` statement, or let errors pause your code so you can verify the state of all variables at certain points. 

When things get complicated, when you have functions calling your other functions, it may be worthwhile to learn about the `pdb` package.

## Create a minimum reproducible example
The test cases often require you to create example data quickly. Here are a few things to keep in mind when creating examples:

- "Happy-path", this case should cover the ideal situation, e.g. no missing values, multiple records and multiple features, unified spelling, etc. After defining the happy-path, it's often more obvious what the edge cases are.
- Missing or illegal values. In our class we will assume the data is "correct" so illegal values will be rare. Their treatment is often the same as handling missing or NaN values where you need to explicitly code up the logic when that happens (e.g. if you're expecting non-negative values, you could replace any negative values with 0 or NaN depending on the question).
- Singular values, since data is often plural, edge cases often exist when there's only a single record (data could be represented as a single number or a list with one number), single feature (e.g. `pandas.DataFrames` becoming `pandas.Series`). In general, the best practice is to convert things to have the same structure (e.g. a single number should be a list with one number) so the same downstream code can run.

But here are some quick templates
```python
demo_int = -2
demo_float = 1.1
demo_bool = True
demo_list = [1, 'hello']
demo_list = ['world', 'hello']
demo_list = [1, 2]
demo_str = 'hello'
demo_map = {'a': 1, 'b': [1, 2]}
demo_map = {'a': 1, 'b': 2}
demo_set = {1, 2}

import numpy as np
demo_array = np.arange(10).reshape(-1, 2)
demo_nan = np.nan
demo_list = [1, np.nan]

import pandas as pd
demo_df = pd.DataFrame({
  'a': [1, 2, 3],
  'b': [-4, 2, 10]})
```


{% include lib/mathjax.html %}