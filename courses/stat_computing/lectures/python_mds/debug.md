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
To prevent issues like the one above is to create test cases, i.e. ex con
According to our understanding We created 

## Identifying the location of the error
The location of an error is often printed in the error message but this sometimes
is not the true cause of the  error.

## Create a minimum reproducible example


## Type of debugging

### Bugs in code

### Bugs in data

## Identifying the source of the error


### 




{% include lib/mathjax.html %}
