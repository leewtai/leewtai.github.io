# Repeating the same task in Python

Humans are bad at repeating the same task consistently, computers are not.

You may want to try out multiple algorithms on the same dataset.
You may want to try the same algorithm on multiple datasets. Python has a
simple way to repeat the same task.

## Loops

#### Recognizing repeated tasks

One of the biggest signs of repeated tasks is duplicated code.
Below is an example where a repeated call to the same function, `print()`,
is being applied to different numbers.

```python
print(1)
print(3)
print(-1)
print(10)
```

Imagine if we suddenly wanted to take the absolute value before printing.
We would have to edit the code at 4 different lines, risking a typo or
inconsistent code.

What about writing a custom print function?
```python
def my_print(num):
    print(abs(num))


my_print(1)
my_print(3)
my_print(-1)
my_print(10)
```
Changes to the function would propagate to all instances, resolving our
initial concern.

Unfortunately, if the data changed, you would have the same problem of
visiting multiple lines of code. Also, you may not want to introduce
all the logic into a single function.

In general,
- Identical operations should be avoided, a principle called don't repeat
  yourself (DRY) is quite popular.
- Data should be not be hard-coded, i.e. they should come
  from a single source so changes to the data will propagate to all
  references to the set of data. We often source data from files which
  is a topic for later.

#### Introducing the for-loop

Since data will likely come from a file, we will assume it can be represented
as a list for now. Now we need something that can step through each of the
data points for us.

We will introduce the for-loop in Python

```python
nums = [1, 3, -1, 10]

for num in nums:
    print(num)

```

- `n` records the number of values in the list (i.e. 4)
- The `for` and `in` are special keywords where the `:` indicates the end of the
  for-loop declaration (delcaration just tells Python to anticipate a for-loop).
  For-loops always have the structure of:
  ```python
  for VARIABLE in COLLECTION:
      CODE_THAT_WILL_BE_REPEATED
      CODE_THAT_WILL_BE_REPEATED
  ```
- The body of the loop is any code that is indented properly (4 spaces here) after
  the declaration, here we only have one line `print(num)` but there is no limit.
- `num` is a variable created during the loop, its singular noun choice is
  intentionally chosen to separate it from `nums` but you could have named it
  anything. This variable, `num` will change for each iteration of the loop.
  The number of iterations depend on the length of `nums`, the first iteration
  `num` will take on the value of `1`, then `3`, then `-1`, and then `10`.
  This is the only variable that will change in the loop.
  So if you run `print(num)` after the loop, you should see `10` being printed.

#### Some variations
- `range(n)` creates an object that can be converted into a list `[0, 1, 2, 3]`
  this will start at `0` and increment by `1` until `n-1`
  - `range(n)` itself it NOT a list, it's something much more efficient that
    we will introduce later
  - Side question: how would you cast `range(n)` into a list?


## List comprehension

{% include lib/mathjax.html %}
