# Importing Packages

If you haven't noticed yet, Python's default functionality is quite minimal.
For example, `log()` which is commonly available in most calculators is not
available by default. You need to source the function from a package.

## Using built-in packages

Continuing the `log()` example, there are 2 ways to obtain access to `log()`:
- Import the package, then call the function as if it's a method in the package.
  ```python
  import math

  math.log(1)
  ```
- Import the function
  ```python
  from math import log
  
  log(1)
  ```

The first method is useful when you're developing your code since you may not
know all the functions you'll need upfront.
The latter is common when you only need a specific function from the package
and the package is relatively large, e.g. sklearn.

#### Popular functions

- `collections.Counter` is useful for counting the frequency of different things,
  e.g. word count in an article, then behaves similarly to a dictionary.
  ```python
  cnt = Counter(['a', 'b', 'a'])
  cnt['a']
  ```
- `itertools.product` is useful when creating the possible combinations between
  two lists of variables. This often turns a double loop into a single loop.
  ```python
  for i, j in product([1, 2], [4, 5]):
      print(i + j)
  ```
- `itertools.chain.from_iterable` is useful to flatten nested lists (or other
  containers!)
  ```python
  from itertools import chain
  x = [[1, 2], [3, 4, 5]]
  x_flat = chain.from_iterable(x)
  list(x_flat)
  ```

## Using custom packages

There is no difference in how to access the functions from a custom package
vs built-in package except in how the package is retrieved.

Built-in packages come with the Python installation. Custom packages require
an additional step that could create problems when working across projects.

Packages may depend on different versions of the same package,
creating a "dependency conflict". This can cause **major** pains if not handled
carefully. For example, installing a package may force you to downgrade another
package which may lead to your old code crashing.

Familiarizing yourself with a package manager will come in handy in the future.
[conda](https://packaging.python.org/en/latest/key_projects/#conda)
is popular with the scientific community,
providing additional features like virtual environments, allowing you to have
different environments with different dependencies.

[pip](https://packaging.python.org/en/latest/guides/tool-recommendations/)
is also quite popular but you would need to pair it with
[virtualenv](https://packaging.python.org/en/latest/key_projects/#virtualenv).
This is more programmer friendly.

Most data science packages can be installed easily through Anaconda.

For those unfamiliar with the command line, the Anaconda Navigator may be
a better start but this isn't well supported given most data practictioners are
reasonably comfortable with the command line.

#### Recommended general flow

- Keep your base environment relatively simple, i.e. do not install too
  many packages in your default Python environment.
- For each project, have an isolated environment for it. Here we
  show the conda command to create an environment called `proj1` with Python
  version 3.8, then including packages like `pandas`, `numpy` etc.
  ```
  conda create -n proj1 python=3.8 pandas ipykernel numpy
  ```
  This would handle all the dependencies between the packages.
- Before working on a projet, activate the environment then launch Python
  from the environment to use the proper functions.
  ```
  conda activate proj1
  ipython
  ```

#### Dominant packages in data science
- `numpy` for matrix computation
- `pandas` for basic data wrangling and jointly manipulating multiple
  data types
- `matplotlib` the foundational visualization package
  - `seaborn` is prettier :)
- `requests` is used to interact with different APIs (e.g. websites) 
- `beautifulsoup4` is used to parse websites' HTML or XML code
- `scikit-learn` is where most machine learning and statistical algorithms
  are stored.

When sourcing these packages, it's common to shorten their name. Below
we shorten `numpy` to `np` so the code is shorter.
```python
import numpy as np

demo_array = np.array([1, 2, 3])
```

{% include lib/mathjax.html %}
