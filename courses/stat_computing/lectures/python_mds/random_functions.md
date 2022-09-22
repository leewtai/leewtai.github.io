# Using random functions

Random functions have a unique role in statistical computing. We can use these to
simulate/draw samples from a complex process then study its behavior.
Examples include seeing if the median follows a central limit theorem, 
approximating the finite sample distribution instead of relying on asymptotic
theory to make inference. Classic sampling when the population is too large
is used for surveys, in machine learning, and in optimization methods.

The random functions are conceptually identitcal to random variables, repeated
evaluations with the same input will return potentially different values from
a distribution. For example, mathematically we migth say 
$$Y \sim Normal(0, 1)$$ and our data is $$Y_1, \dots, Y_n$$ then programmatically
we could write (the example below is an attempt to keep notation consistent):

```python
from random import gauss

n = 5
def Y():
    return gauss(0, 1)
Ys = [Y() for _ in range(n)]
```

## Common functionalities in random functions

There are a few basic functionalities one should be aware of with random functions.
These are true for most modules that support random operations.

- Shuffling/permuting a ordered collection of values. 
  ```python
  import random
  
  ordered_list = list(range(5))
  # this is an inplace operation
  random.shuffle(ordered_list)
  print(ordered_list)
  ```
- Drawing a sample from a finite set with equal probability.
  ```python
  import random

  coin = ['heads', 'tails']
  tosses = [random.choice(coin) for _ in range(10)]
  print(tosses)
  ```
- Drawing a continuous function from a well known distribution.
  ```python
  import random
  
  normals = [random.gauss(0, 1) for _ in range(5)]
  ```
- Repeating the same random sequence (please see the **warning** below on
  hash vs random functions if you really care about reproducing outcomes).
  ```python
  import random
  
  random.seed('hello world')
  print([random.uniform(0, 1) for _ in range(3)])

  random.seed('hello world')
  print([random.uniform(0, 1) for _ in range(3)])
  ```

## Notable packages with random functions

- Base python
  - The base Python has a [`random` module](https://docs.python.org/3/library/random.html)
    that supports very basic random operations.
- `numpy`
  - [Numpy's random module](https://numpy.org/doc/stable/reference/random/index.html) is
    exceptional at working with or producing a lot of random values quickly.
- `scipy.stats`
  - [scipy.stats](https://docs.scipy.org/doc/scipy-0.16.1/reference/stats.html) has the most
    comprehensive number of distributions along with features like calculating the percentiles
    (useful for p-value calculations).
    
## Random vs hash functions

A truly random continuous function, when called twice, will have 0 probability
of returning the same value.

```python
import random

# Get 3 different random values with the same input
rand_perc = [random.uniform(0, 1) for _ in range(3)]
```

Hash functions although map their inputs to a
seeming random output, are consistent in returning the same output when
provided with the same input. This is useful with ID generation or AB testing
assignment when you want the same user to be assigned to the same treatment/control
group as before.

```python
import hashlib

input = 'wayne lee - homepage v2'


def str2perc(input):
    output = hashlib.md5(input.encode())
    # a random but predictable hex value
    output_hex = output.hexdigest()
    # converting the hex value into a percentage
    output_perc = int(output_hex, 16) / 16**len(output_hex)
    return output_perc


# Get 3 identical random values with the same input
hash_perc = [str2perc(input) for _ in range(3)]
```

#### Repeating the same random numbers by fixing the seed and more

Sometimes we want to ensure our results are reproducible, this is when we fix
the seed and the order we call the random functions in.

```python
import random

random.seed('hello world')
print([random.uniform(0, 1) for _ in range(3)])

random.seed('hello world')
print([random.uniform(0, 1) for _ in range(3)])

random.seed('hello world')
#_ = random.shuffle([1, 2, 3])
_ = random.uniform(0, 1)
print([random.uniform(0, 1) for _ in range(3)])
```

In the example above, notice how the first 2 random sequences are identical
and the last one is simply shifted. The key is that in addition to fixing the
random seeds, one needs to be careful about the other calls to the random
module in order to reproduce the same results. This is not suitable for
production when multiple services are acting asynchronously.


{% include lib/mathjax.html %}
