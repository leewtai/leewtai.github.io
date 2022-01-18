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

We will introduce the for-loop in Python, the 4 lines above can be replaced
with the code below. Note that the list can be arbitrary length but the code
to repeat tasks would remain the same.

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
  intentionally chosen to match the plurality in `nums` but you could have named it
  anything. This variable, `num` will change for each iteration of the loop.
  The number of iterations depend on the length of `nums`, the first iteration
  `num` will take on the value of `1`, then `3`, then `-1`, and then `10`.
  This is the only variable that will change in the loop.
  - if you run `print(num)` after the loop, you should see `10` being printed.


#### A different type of loop

Sometimes it makes more sense to loop over the position of the data, i.e. the indices,
instead of the different values themselvse. For example, where there are 2 sets of data that
have the same order (e.g. midterm vs final where the order is sorted by name).

To iterate (or loop) over the indices, we could rewrite the loop above:
```python
nums = [1, 3, -1, 10]
n = len(nums)

for index in range(n):
    num = nums[index]
    print(num)

```

- `n` is just the length of the list, i.e. the number of iterations.
- `range(n)` creates an object that can be converted into a list `[0, 1, 2, 3]`.
  This will start at `0` and increment by `1` until `n-1`
  - `range(n)` itself it NOT a list, it's something much more efficient (generator) that
    we will introduce later
  - Side question: how would you cast `range(n)` into a list?
- We could replace the body with just `print(nums[index])`
- `index` again is just a variable that will take on different values on different
  iterations of the loop. In this case, it'll first be `0`, then `1`, then `2`, then `3`.
  We then use subsetting by position (the index) to extract the specific value from `nums`.

In most programming langauges, you'll see `index` abbreviated as `i`.
Looping over the indices is convenient because you may another list, e.g. `denoms` that
you want to loop over at the same time.

#### Looping over the index and values
Somtimes people want access to both the index and the value in a list. Rather than
defining `num = nums[index]` with an extra line. There's a function called `enumerate()`
that can help.

```python
nums = [1, 3, -1, 10]

for index, num in enumerate(nums):
    print('index is {}'.format(index))
    print('num is {}'.format(num))
```

`enumerate(nums)`, similarly to `range(n)` from before is a generator. It's easiest to
understand it by casting it to a list. You should see a list of tuples, where the first
element in the tuple is the index and the second is the corresponding value in `nums`.
```python
In [98]: list(enumerate(nums))
Out[98]: [(0, 1), (1, 3), (2, -1), (3, 10)]
```

This is exploiting Python's ability to assign multiple variables at once, e.g.
`a, b = (1, 2)`.

#### Recording the output from each loop
Since the body of the loop is identical, any variables assigned in the loop will
be overwritten and only keep the value from the last loop.

To avoid this problem, the usual approach is to define a variable outside the loop
and allow the loop to **update** the variable rather than assign over the variable.

The variable that will keep the records should be a data type that can hold multiple
values and can be updated (e.g. tuples wouldn't work). We give an example below with
some random transformation dependent on the same set of values.
```python
nums = [1, 3, -1, 10]

record_keeper = []
for num in nums:
    record_keeper.append(42 * num % 13)

print(record_keeper)
```

`record_keeper` now has the output from each iteration of the loop that you can access
outside the loop.

It's important to know that re-running the for-loop requires you to re-assign `record_keeper`
as an empty list otherwise it'll hold the records from the previous run as well.

#### Aggregating data
Another common pattern is where the loop is intended to aggregate the data. 
Imagine trying to sum up the values in our list, `nums` without using the function `sum()`.

```python
nums = [1, 3, -1, 10]

total = 0
for num in nums:
    total = total + num

# The two should equal
print(total == sum(nums))
```
The logic is similar as before, i.e. define a variable outside the loop and update it in each
iteration. Except our update can be dependent on the aggregate to date and the new value.

## List comprehension
This is another uniquely Python feature that you'll see commonly used to replace loops.

The example in **Recording the output from each loop** can be simplified into

```python
nums = [1, 3, -1, 10]

record_keeper = [42 * num % 13 for num in nums]

print(record_keeper)
```

List comprehension basically allows users to simplify a lot of the for-loop into a single
line, keeping the important logic at the front and the looping information towards the end.
Wrapping this all into a list is a common choice but other containers can do this as well.
This is appropriate only for loops with little amount of calculations.

{% include lib/mathjax.html %}
