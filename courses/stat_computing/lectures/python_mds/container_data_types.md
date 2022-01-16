# Containers of data in Python

Data is often a collection of values and the operations we require
for a collection of data is often different from a single datum.
This is why we have new data types for a collection of objects.

We will cover the native data types that can "contain" multiple
values of data:
- lists
- dictionaries ("maps")
- tuples
- set

## Overview

|Data type|Are the values ordered|Can you changed the values|Does each value have a name?|Can it hold multiple types of data?|
|---|---|---|---|---|
|Lists|Yes|Yes|No|Yes|
|Dictionaries|No|Yes|Yes|Yes|
|Tuples|Yes|No|No|Yes|

More advanced data containers like numpy arrays will restrict all values to
share the same data type to speed up calculations.

#### Lists are flexible
Lists stand out with their flexibility to hold multiple types
of values (include lists themselves) while requiring relatively little input
from the user.
These are commonly used to quickly hold the outputs from simulations
or intermediate outputs that will be stored more efficiently later on.

To create a list, we use the square brackets `[]` and separate
each value using `,`.
```python
demo_list = [1, 'failed', 'missing', -10]
print(demo_list)
```

To add additional values to the list, we would use the `list.append()` method.
```python
demo_list = [] # An empty list
demo_list.append(20)
print(demo_list)
demo_list.append([50])
print(demo_list)
```

#### Dictionaries are descriptive
Dictionaries stand out with their self-description and ability to query values
using a human-readable key (rather than memorizing which value is which).
A popular data format used between websites, JSON, naturally translate into
dictionaries.

Each value in a dictionary has 2 parts: the key and the value associated with it.
For example, the key `"first_name"` could map to the value `"John"`.
We create dictionaries by using the curly brackets `{}`, separating each value
again with `,`. To distinguish between the key and value, we use the colon `:`.
Specifically, the key comes before the colon and the associated value follows the colon.
```python
demo_map = {'first_name': 'Wayne',
            'last_name': 'Lee',
            'height_cm': 179,
            'vaccine_dates': ['4/20', '5/20', '11/20']}
```

Keys are normally human-readable strings but other values can be keys as well. 
The key must be "hashable" which is a concept we'll introduce later. There are
almost no restrictions on what a dictionary can be.

To add OR change a field, we would use the `dict.update()` method.
```python
demo_map = {}
demo_map.update({'class': 'intro to python'})
print(demo_map)
demo_map.update({'class': 'stat comp'})
print(demo_map)
```

#### Tuples are predictable
Tuples stand out with their predictability because they cannot be changed
after they are formed. This is useful with larger projects where some code
may update your data and cause some unintended consequences.
These are not as popular for data users but more useful for data engineers.
The concept that some values are not changable (a.k.a. mutable) is important though.

```python
demo_tuple = ('wayne', 179)
```

You cannot add or remove values from a tuple once they're created.

## Common operations with containers

#### Subsetting particular values - Python starts counting at 0
We can subset specific values from each of these containers using the square
bracket `[]`.

Given that lists and tuples are both "ordered", we can use the position
on the list/tuple, i.e. index, to specify which value we want. Dictionaries
are not ordered but instead uses the key to retrieve the corresponding value.

```python
demo_list = [1, 2, 3]
demo_map = {'a': 1, 'b': 2, 'c': 3}
demo_tuple = (1, 2, 3)

demo_list[0]
demo_tuple[1]
demo_map['c']
```

The example above shows that Python starts its counts at 0. We call this
0-index and this will keep the code cleaner in the future. Some programs,
like R, start their index at 1.

An important error to know is when one misspells the key or if the key
does not exist within the dictionary.

```python
demo = {'abc': 1}
demo['abs']
# Guess at this error message, remember dictionaries have no order
demo[0]
```

Sometimes it's recommended for data users to use `dict.get()` to retrieve
the value because a missing key would not result in an error that terminates
the code.
```python
demo.get('abs')
```

Subsetting is done not only to view the particular data value but also
allows one to assign a new value.

```python
first_letters = ['a', 'b', 's', 'd', 'e']
first_letters[2] = 'c'
print(first_letters)
```

#### Slicing data - peeking at a segment of data
When validating data, it's common to peek at a segment of the data. 
One could think of this exercise as subsetting multiple consecutive values
from the container, also known as slicing.

To view the 2nd to 3rd value, I would pass `1:3` inside the square brackets, `[]`,
for the list of tuple. 
```python
demo_list = [1, 2, 3, 4]
demo_tuple = (-4, -3, -2, -1)

demo_list[1:3]
demo_tuple[1:3]
```
`1` represents starting from the 2nd position, although `3`
stands for the 4th position but the expression should be thought as retrieving
the values "starting from the 2nd position and stop before the 4th position".
This may seem awkward but it's useful because often we retrieve
data starting at a position and having a budget, e.g. the willingness to look at 2 values.
Therefore one could view the slicing expression as `1:(1 + 2)` instead.

Some convient syntax for slicing "the first 3 values" or "the 2nd value and on"
can be done by omitting the starting or ending index.
```python
demo_list[:3]
demo_list[1:]
```

#### Iterating through the container
Another important operation is to iterate through each value in the container
and perform a calculation for each one. We will introduce this concept later.

Notice that we cannot slice dictionaries because they are not guaranteed to preserve
the order when you defined them.

## Variables behave differently with containers

Look at this example
```python
x = 1
y = x
print(x)
print(y)
y = 2
print(x)
print(y)

x = [1, -2, 3]
y = x
y[0] = 2
print(x)
print(y)
```

With integers, changing the value in `y` didn't affect `x`, but the behavior
changed once we switched to lists.

For the integer case, notice that `y` is being completely re-assigned to a new
value. Overwriting the original `y=x` with `y=2` severes the relationship between `y=x`.

In the second case, it's easier to think of `[1, -2, 3]` as a set of Google slides
with a shared link called `x`. Now imagine if you created another shared link
called `y`, referencing the same set of slides, then `y[0]=2` is equivalent to editing
the first slide. Since `x` and `y` are still referencing the same set of slides,
both would see the effect of the edit. `y[0] = 2` subsetted the first value within
the list referenced by `y` but did not reassign `y` to a new variable.

This behavior of variables acting as references to the data is called "copy by reference",
i.e. `y = x` copied the reference to the variable `y` instead of creating another identical
list (the other behavior is called copy by value).

If you want to copy by value, you could use `list.copy()`
```python
x = [1, -2, 3]
y = x.copy()
y[0] = 2
print(x)
print(y)
```

{% include lib/mathjax.html %}
