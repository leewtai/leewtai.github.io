# Adding rules to code

A typical quality check before running any models is to see if there is any
data. This can happen when you are fitting a separate model for differnet
user segments and some user segments may be non-existent.

In these cases, we often want the code to behave differently. To achieve
this, we can use if/else statements to check if a condition is met (i.e. `True`)
then run different pieces of code accordingly.

## Basic if/else

If/else statements generally take the form of:
```python
if CONDITION:
    CODE_TO_RUN_IF_CONDITION_IS_TRUE
else:
    CODE_TO_RUN_IF_CONDITION_IS_FALSE
```
Again `if` and `else` are special keywords. `CONDITION` needs to be
something that can be cast into a boolean. This is often:
- a boolean operation, e.g. `len(a) >= 10`. So the output itself is already
  a boolean
- or a piece of data, e.g. `[1, 2, 3]` (to check if there is any data)

The indentation for the body of the code is important in Python. Other
programming languages use `{}` to indicate the body of the code. This
quickly fills up the script and makes it hard to read.

The simplest if/else statement only needs an `if`:
```python
x = ''
if x:
    print('x is not empty')
    print(x)
```

The code above should print nothing. The `if x:` is the declaration of
the if statement. Given `x` is not a boolean value, Python will try
to cast it to a boolean, i.e. `bool(x)` to decide whether `print(x)`
should run or not.

A slightly more complicated version explains how `else` works.
```python
x = ''
if x:
    print('x is not empty')
    print(x)
else:
    print('x seems to be empty')
```

#### elif (else if)

It is possible to have sequential conditionals:
```python
x = -2
if x < 0:
    print('x is bad')
elif x >= -3 and x < 5:
    print('x is okay')
else:
    print('x is good')
```

The above if/else is intentionally bad to demonstrate a few things:
- Python does not check if your logic makes sense, if `x = -2` then
  it is unclear which line you meant to run.
- Notice that only the first `print()` statement is ran. This is because
  `elif` and `else` will not be checked if the condition before is true.
  Therefore the ordering of your conditions matters.
- `else` will capture all possible leftover cases. This can be lead to
  surprises.


#### Defaults in if/else
Sometimes we initialize variables (like the empty list before a loop)
differently according to another variable or condition, it is then
common to do

```python
y = True
if y:
    x = 1
else:
    x = 2
```
Notice that `x = 2`  will not run at all.

However, sometimes to simplify code, it's better to write
```python
x = 2
if y:
    x = 1
```
This way it is clear that `x` is defaulted to 2 and will be overwritten
if the condition `y` is `True`. This also avoids cases where one may
forget to define `x` in the `else` clause.

An even shorter version is:
```python
x = 2 if y else 1
```

#### If/else in list comprehension

It is common to run a loop but only process certain records that satisfy
a condition.

Here is a very verbose example:
```python
nums = [1, -3, -4, 5]

output = []
for num in nums:
    if num > 0:
        output.append(num * 10)
```
List comprehension can save a lot of space. All we need to do is place the condition
after the loop
```python
nums = [1, -3, -4, 5]

output = [num * 10 for num in nums if num > 0]
```

Notice that all the `False` cases will be dropped!

For readability, some people like to separate the
conditional in the list comprehension
```python
output = [num * 10 for num in nums
          if num > 0]
```

## Control flow in a loop

Continuing the same verbose example from above. Sometimes the code
after the `if` statement has many lines. In that case, having
a lot of code indented due to a single condition seems unnecessary.
In this case we can use `continue` or `break` to rewrite the code.
```python
nums = [1, -3, -4, 5]

output = []
for num in nums:
    if num <= 0:
        continue
    output.append(num * 10)
```

`continue` will terminate the current iteration and move on the
next iteration of the loop. `break` on the other hand will terminate
the entire loop.

## Catching errors with `try` and `except`

Sometimes we know the code will break, i.e. the code throws an error
message and it is not easy to capture the logic in an if/else statement.
In these cases, we will try to "catch the error" before it terminates
the remaining code.

Below we intentionally trigger a bug when we add a `str` to an `int`.
```python
answer = 1

try:
    print('the answer is ' + answer)
except:
    print('something went wrong')
```
After running the example above, you should see the behavior when
`answer = "1"`, i.e. when no bug is triggered.

Overall, `try` will attempt the content in its body (i.e. the indented
code), if an error occurs, it will try the code in the `except` section.

#### Best practice - catching specific errors

Catching errors seem like a good feature but sometimes the errors can
go unnoticed for quite some time. To ensure you're only capturing the
type of errors you anticipated, you can catch specific errors by
specifying the type after `except`.

```python
answer = 1

try:
    print('the answer is ' + answer)
except TypeError:
    print('something about types went wrong')
```

Any `TypeError` triggered will only result in a `print()` call but
any other type of error will terminate the program!

Another common practice, is to capture the error message by rewriting

```python
answer = 1

try:
    print('the answer is ' + answer)
except TypeError as e:
    print('something about types went wrong')
    print(e)
```

#### Building error messages into my code?

It is good practice to anticipate bad input for your code so you can
provide meaningful error messages to your users. For those who want to
raise errors when bad inputs are passed. There's a keyword `raise` 
for that.

```python
input = 1

if type(input) != str:
    raise TypeError('expecting str input bur got non-str values')

```
So in this case we initiated a Type Error if the input is not of type
`str`.


{% include lib/mathjax.html %}
