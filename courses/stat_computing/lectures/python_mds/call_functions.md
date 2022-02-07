# Calling Built-in Functions in Python

Similar to calculators with basic transformations, Python has a suite of
functions to help you work with data.

But unlike calculator functions that take in a single number (e.g. `abs(-1)`),
there can be multiple inputs and inputs can be lists or other more complicated
objects.

## Functions with multiple arguments
Sometimes it's useful to sort the data according to a feature before examining
the data so you can focus on the outliers. `sorted()` is such a function that
can help:

```python
demo = [10, 9, 9, 1, 5, 8, 6, 7, 7, 10]
asc_demo = sorted(demo)
print(asc_demo)

dsc_demo = sorted(demo, reverse=True)
print(dsc_demo)

print(demo)
```

This example shows:
- Multiple inputs can be passed into functions separated by `,`
- Inputs can be different types (e.g. list and boolean).
- Inputs can have names like `reverse` where `=` again assigns the input to the
  particular argument.
- The input list, `demo`, itself was not changed. This may not be true for some
  functions that have "in-place" manipulations.


## Passing arguments by position vs keywords
Continusing the example above, the first input `demo` was passed in as the first
input which is considered a positional argument. The second input `True` was
passed as a keyword argument because we referenced the keyword `reverse`.

Notice that keyword arguments cannot be used before position arguments since
the intent is unclear: do you expect the keyword argument to count as one of
the positions or not?
```python
sorted(reverse=True, demo)
  File "<ipython-input-18-9383389be95f>", line 1
    sorted(reverse=True, demo)
                         ^
SyntaxError: positional argument follows keyword argument
```

How did we know what the keywords were called? Look up the documentation
```python
help(sorted)

# or in iPython
?sorted
```

## Writing your own function
Imagine that we would like to standardize text data by lowercasing the
words then split the text up by spaces.

```python
def standardize_text(text):
    return text.lower().split()
```

- We use the `def` keyword to let Python know we're defining our own function
- The name of the function is `standardize_text`
- The function takes in one input called `text`, the name would suggest the
  input is a string
- The body of the function comes after `:`
- The indentation of 4 spaces for the body of the function is necessary
- The `return` keyword will pass the resulting output and terminate the function.
  All commands after the `return` function is run will be ignored.
- We did not have to specify the data type of the output

You should always test the function with various types of input to see what could
go wrong. It is good to have cases that will for sure fail!
```python
standardize_text('hello world!')
standardize_text('#2022HereWeComeAgain')
standardize_text('George Washington')
standardize_text('STOP')
standardize_text('')
standardize_text(['i said x', 'you said y'])
```

#### Setting defaults in functions

You can give your function default values for its parameters by assigning the
parameter during its definition. For example, if we wanted a log function 
that defaulted to `base=10` instead of `base=e`:

```python
from math import log


def my_log(x, base=10):
    return log(x, base)    


my_log(100)
my_log(100, 100)
```
- By assigning `base=10` in the parameter specification, we default the value
  of `base` to `10`.
- We can still override the value of `base` like a normal parameter.

#### In-place functions

Python has a few in-place functions/methods that modify the object directly
and usually returns nothing (this is a coding pattern in Python, not a result of
in-place algorithms). Here's an example of a common **mistake**

```python
demo = [1, -1, 0]
sorted_demo = demo.sort()

print(demo)         # prints [-1, 0, 1]
print(sorted_demo)  # prints None
```

`list.sort()` sorts the list `demo` directly so `demo` is modified.
The method, however, does not return anything so `sorted_demo` will
be assigned `None`. The common mistake is to assume all functions will
return an object and see code crash because `sorted_demo` is `None` instead
of a `list`.

In-place operations are attractive because they do not require doubling the
memory when working with data. If `demo` and `sorted_demo`
both existed, then you now have two copies of the data (different order).
If these lists were much larger, this will quickly become a problem.

There unfortunately is no standard around naming for in-place functions and
you need to read the documentation. The popular package `pandas` often has
options to do in-place operations.

{% include lib/mathjax.html %}
