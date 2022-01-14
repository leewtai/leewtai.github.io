# Simple data types in Python

Different types of data are often handled differently. You can add and divide
numbers, you may want to identify keywords in text, you may want to count
the frequency of positive tests from a disease, and you may have missing data
in each of these.
These different use cases demand different computer operations and so different
"data types" were created. This is also one of the most common sources for
errors in code so understanding data types is important.

The simplest forms of data in Python are
- Numbers
  - Integers vs floating numbers (e.g. `1.513`)
- Character strings, e.g. `"Lil Wayne"`
- Boolean values, e.g. `True` or `False`

## How do I figure out the data type of something?

When in doubt, use `type()`
```python
x = 1.2
type(x)

y = True
type(y)

z = "True"
type(z)
```

## How can I change the data type of something?

This is called "casting".

```python
x = 2 / 1
type(x)
y = int(x)
type(y)

# Be careful
x = 2 / 1
type(int(x))
type(x)
x
int(x)
```

The key is to know that casting can be expensive because Python may need to "guess"
what your intent is, e.g. the example above rounded downwards even though $x > 1.5$.

There are functions 

#### Casting to boolean values

## 

{% include lib/mathjax.html %}
