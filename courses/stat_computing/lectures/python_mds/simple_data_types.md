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

#### What are boolean values and how do they come about?

Boolean values can only take on `True` or `False` two values. They may
appear in your data when
- You make a comparison, e.g. is someone's BMI over 25?
- Labeling data, e.g. does this image have a face in it?

Only allowing two values seems restrictive and unnecessary but this
restriction provides guarantees that make this easy to work with.
We will introduce booleans in more details later.

## How do I figure out the data type of something?

When in doubt, use `type()`
```python
x = 1.2
type(x)

y = 1 < 3
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

# Casting doesn't change the underlying variable
x = 2 / 1
type(int(x))
type(x)
x
int(x)
```

Casting can be expensive because Python may need to "guess"
your intent, e.g. if `x = "1"` should `x + x` be `"11"` or `2`?

Here are the functions that help "cast"

|Data type|Function|
|---------|--------|
|integers |`int(1.2)`|
|floats   |`float(10)`|
|strings  |`str(10)`|
|boolean  |`bool(0)`|

You should try to cast something that doesn't make sense, e.g. `int('abc')`

#### Casting to boolean values checks for emptiness ("nullness")

Most casting results should be somewhat intuitive. The only 2 exceptions are the
flooring behavior of `int(1.8)` and the treatment of casting to boolean values.

The latter matters because code often needs to act differently if there's no data.
You'll frequently see checks about the amount of data before executing any code.

The most common behavior when casting non-booleans to booleans is to ask the user to
be specific and throw an error otherwise (like in `int("abc")`). Python is unique in
its handling of casting with `bool()` which is
often considered a feature. The overall principle is that "empty" values are
treated as `False`, and all else is treated as `True`.

Try a few examples below to see:
```python
bool(-1)
bool(1e10)
bool(0)
bool('hello')
bool('Negative')
bool('')
bool(True)
bool(False)
```

This principle extends beyond the basic data types, in particular, data types
that contain multiple values. We show an example with a list here (we will cover
lists later).
```python
x = [1, 2, 3]
bool(x)
y = []
bool(y)
```


## Every thing in Python is an object

Python, an object oriented programming language, focuses
on designing objects that contain both the data pertaining to the object
and operations that are sensible to the object. For example, `demo_text = "abc"`
will assign a character object to the variable name `demo_text`. This object
will have `"abc"` as its data but also has functions like `demo_text.upper()`
to perform sensible operations on characters.

The data portion is often called attributes or properties and the operations/functions
portion is often called procedures or methods.

Since methods/functions must be associated with a particular object,
it is common to refer to methods/functions as OBJECT_NAME.METHOD_NAME().

Using our basic data types as an example
- String objects often require changing its capitalization to standardize
  text. Below we lowercase the string `"ABC"` by calling the method `str.lower()`
  ```python
  a = 'ABC'
  a.lower()

  # Notice that integers do not have this method
  b = 123
  b.lower()
  ```
- The absolute value can reflect a number's magnitude and is a common
  operation for numbers.
  ```python
  a = -4
  a.__abs__()
  abs(a) # Equivalent
  ```
  Side note: the `__` before and after `abs` just indicates that when
  the built-in function `abs()` is called on this object, the method
  corresponding method that has the same name as the function will be
  called.

The key is that objects will inform you what methods and data are
available to you. So when you want to operate on some data, always
search for available methods/functions before writing your own.

#### Finding the available attributes or methods

The fastest way to know the available methods is to use iPython's
autocomplete feature. For example, first create an object, `a='hello'`.
Then type out the period symbol `.` right after calling the create variable
like `a.`. Hitting "Tab" right after the period should trigger a list
for you to navigate all the available methods and attributes.

Notice that methods beginning with `__` are not shown by default. To see
these, simply type out `a.__` then hit Tab in iPython to see the hidden methods.

#### Relationship between binary functions and methods

Note that binary operators like `"+"` will **usually** invoke the method `.__add__()`
on the first object, treating the second object as inputs. This explains why
the error messages are different below. Since different methods are being used.

```python
"1" + 1
1 + "1"
```

There is some extra code that gets implemented with the binary operators because
the behavior is not always consistent:
```python
a = 3
b = 'hello'
a * b
a.__mul__(b)
```

## Common operations

#### Common numeric operations
Assume `a = 4`, and `b = 3`
- `a * b` multiply
- `a + b` add
- `a % b` modulo, i.e. get the remainder from integer division, `4 % 3`
  this is commonly used to create "random numbers" which we do not
  recommend. 
- `a ** b` exponentiate
- `a / b` divide
- `abs(a)`
- `min(a, b)` and `max(a, b)`

#### Common string operations
Assume `demo = 'i said'`
- `demo.upper()`, `demo.lower()`, `demo.capitalize()` capitalization
- `demo.find('id')` find the starting position of a substring within the string.
  We will talk about the answer of this in a later chapter.
- `demo.isnumeric()` check if the string contains only numbers, note that "." is not
  a number so `"1.4".isnumeric()` should be `False`
- `demo.isalpha()` check if the string only contains letters
- `len(demo)` checking the number of characters in the string
- `demo + ' hello'`, concatenating the strings together.
  This is actually **not** recommended to "format" strings.
- Formatting strings can be done using
  - The `str.format()`, e.g.
    ```python
    "hello {name}{tone}".format(
      name="world",
      tone="!")
    ```
  - The f-string (less backwards compatible), e.g.
    ```python
    name = 'world'
    f'hello {name}'
    ```
- Splitting a string by a particular character, e.g.
  ```python
  dates = "12/30/2022".split("/")
  ```

#### Common boolean operations
Assume `a = 1`, `b = 2`, `c = 3`
- `a < b`, `a <= a`, `a > b`, `a >= b`, order comparisons, note that
  `'a' > 'A'` is something we'll talk about later.
- `a != b`, `a is not b`, `not a == b`, checking for inequality
- `a == b`, `a is b`, checking for equality
- `a < b and b > c`, `a < b & b > c`, checking if both statements are true
  - If one case is commonly False, try to put that first to fail quickly before computing the second statement.
- `a < b or b > c`, `a < b | b > c`, checking if at least one statement is true
  - If one case is commonly True, try to put that first to avoid computing the second statement.

Note that `not` is a special keyword to negate a boolean, i.e. turn `True` into
`False` and vice versa.

## Interacting different data types with each other
Every now and then we perform operations with multiple data types. Python is
somewhat unique in how these interactions unfold.

In general, the best way is to try it out and see. The programmer has to implement
the allowed interactions one by one. Here we list some of the common ones:
- `int * str` will replicate the `str` as many times as the `int`. For example `"!" * 3`
  - Values less than or equal to 0, will be treated as 0, returning an empty string
- Any mathematical operation between an `int` or `float` with a `bool` will
  first convert the `bool` value to `1` (if it's `True`) or `0` (if it's `False`).


{% include lib/mathjax.html %}
