# Mapping functions

There's an important alternative way of coding when we repeat tasks.
Although for-loops is often the first technique taught in classes, they
do not scale nicely with big data.

Big data, where the data is distributed across different machines, often
cannot loop through every record in the data efficiently. If the operation
on one record does not affect the other records' outcome, then we could
parallelize the operations instead of going through the records sequentially.

The parallelization part is often done via a map function that distributes
the computation/code/function to different segments of the data. This is
almost always followed by a reduce call, the part that cannot be parallelized,
like putting the results in a single list.

Separating the different types of operations allows us to speed up the computation.
For-loops often mix these operations together because we often append or
update the same variable (an operation that cannot be parallelized if we
care about the order of the output) within the for-loop as well as
computation on separate records that could be parallelized.

For an example of separating the operations, imagine we had data across
3 machines, represented by the index in the list. Our goal is to calculate
the total number of words with the substring `'tox'`.
- We distribute the function `lambda x: count_words(x, 'tox')` across
  each "machine" using the `map()` function. Although in reality this is
  done sequentially with `map()`, this could be parallelized easily in the future.
- We use `reduce` to collect the results from the different "machines" and
  reducing the results into a single value we wanted.

```python
import re
from functools import reduce

records = [
    ['toxic', 'drug', 'medicine'],
    ['healthy', 'chemistry', 'toxicology'],
    ['botox', 'toxicity']]


def count_words(words, pattern):
    patt = re.compile(pattern)
    return sum([patt.search(word) is not None for word in words])

tox_freqs = map(lambda x: count_words(x, 'tox'), records)

tox_freq = reduce(lambda x, y: x + y, tox_freqs)
```
- Try casting `tox_freqs` into a `list` before and after you calculate
  `tox_freq`. The object from `map()` can only be accessed once.
- Notice the `lambda` function in `reduce()` takes 2 arguments.

Practicing how to split for-loops into `map()` vs `reduce()` operations
will be the key to big data computation in the future (not covered in this class).

#### What is a lambda function?!

There was a tricky usage of a `lambda` function above. Overall, `lambda` just allows
us to define a function without giving it a name.

Recall that defining functions often require the declaration like `def FUNCTION_NAME(INPUTS):`
Now imagine if we will only use the function once AND the function is relatively simple. Then
it does not seem useful to think of a practical name (recall WHY we have variables). The
inputs and function is sufficient. Because of this, you will see `lambda` functions
defined relatively commonly.

A lambda function has a few elements:
- Starts with the keyword: `lambda`
- Followed by the inputs separated by comma
- Followed by a colon, `:`
- Then the function body, this should be a single line of code that is easy to understand.
  Anymore then you should define a function properly with a name that summarizes its intent.

A common place to see `lambda` functions is with `pandas.Series.apply()` or `numpy.apply_along_axis()`.
For example, if I want to find the power outage events related to only Texas from a messy
dataset:
```python
power_outage = pd.DataFrame(
    {'num_customers_impacted': [1000, 2000, 3000],
     'location': ['TX', 'Texas, Oklahoma', 'OK, KS']})
hasTX = power_outage.location.apply(lambda x: 'TX' in x or 'Texas' in x)
tx_outages = power_outage.loc[hasTX, :]
```



{% include lib/mathjax.html %}
