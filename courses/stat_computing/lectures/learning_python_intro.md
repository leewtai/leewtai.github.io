# Learning Python from the Data Perspective

In contrast to most programming tutorials, these notes will teach you Python
from a data perspective rather than a computer science perspective. We will
leverage examples in Tech whenever possible.

The table below will have each concept, linked to a detailed explanation for
each concept.

<table>
<tr>
  <td>Coding concept</td>
  <td>programming example</td>
  <td>Use case example</td>
  <td>statistics example</td>
</tr>
<tr>
  <td>
  <a href="python_mds/interacting_with_python.html">1. Interacting with Python and your files</a>
  </td>
  <td><pre>
  python hello.py
  </pre></td>
  <td>
  Your files and programs are located on different "paths/folders" on your computer.
  Modern computer interfaces abstract this concept away which can confuse
  beginning programmers.
  </td>
  <td>
  </td>
</tr>
<tr>
  <td>
  <a href="python_mds/python_basic_syntax.html">2. Basics syntax - interacting with the REPL</a>
  </td>
  <td><pre>
  1 + 1  # works!
   1 + 1 # fails
  </pre></td>
  <td>
  Expectations in interacting with Python after each command
  </td>
  <td>
  Makes sense:
  $$\sum_{i=1}^{10} i$$
  Doesn't make sense:
  $$i \sum_{i=1}^{10}$$
  </td>
</tr>
<tr>
  <td>
  <a href="python_mds/variables.html">3. Assigning variables</a>
  </td>
  <td><pre>
  n = 10
  print(n)
  sum(range(n))
  </pre></td>
  <td>
  N is used to estimate the cost of sampling, the
  uncertainty of our hypothetical sample average, and to calculate the
  sample average. We want the same value used throughout so we give it
  a name, the sample size.
  </td>
  <td>
  $$n = 10$$
  $$\sum_{i=1}^n i = \sum_{j=1}^n j$$
  </td>
</tr>
<tr>
  <td>
  <a href="python_mds/simple_data_types.html">4. Simple and single-valued data types</a>
  </td>
  <td><pre>
  demo_num = 1
  demo_str = "1"
  demo_bool = True
  </pre></td>
  <td>Data can be numbers or text, we handle them differently so we have data types for functions to treat them differently too.</td>
  <td>$$y \in \mathbb{R}, x \in \{0, 1\}$$</td>
</tr>
<tr>
  <td>
  <a href="python_mds/container_data_types.html">5. Simple and multi-valued data types</a>
  </td>
  <td><pre>
  a_list = [1, 2, '3']
  a_dict = {'a': 1,
            'b': 2}
  a_tuple = (1, 2, 3)
  </pre></td>
  <td>We need to differentiate a single value from a collection of data.</td>
  <td>$$y = 1, x = \{1, 2, 3\}$$</td>
</tr>
<tr>
  <td>
  <a href="python_mds/call_functions.html">6. Calling functions</a>
  </td>
  <td><pre>
  min(3, -1)
  sum([1, 2, -1])
  </pre></td>
  <td>We want to wrap up a collection of commands into a single call with certain inputs and outputs.</td>
  <td>$$f:\mathbb{R}^p \to \mathbb{R}$$</td>
</tr>
<tr>
  <td>
  <a href="python_mds/loops.html">7. Control flow - for-loops</a>
  </td>
  <td><pre>
  for i in range(3):
    print(i)
  </pre></td>
  <td>How do we ask a computer to repeat its tasks?</td>
  <td>$$\forall i, f(x_i)$$</td>
</tr>
<tr>
  <td>
  <a href="python_mds/packages.html">8. Importing packages</a>
  </td>
  <td><pre>
  import math
  math.log(1)
  </pre></td>
  <td>To leverage other people's code, we often source in their pacakges.</td>
  <td></td>
</tr>
<tr>
  <td>
  <a href="python_mds/ifelse.html">9. if/else and exceptions</a>
  </td>
  <td><pre>
  if 'a' in 'Broadway':
      print('Broadway with an "a"')
  </pre></td>
  <td>When the code changes behavior under different conditions</tdr>
  <td>$$f(x)=\left\{ \begin{array}{ccc} 
        0 & x < \theta \\ 
        x & x \geq \theta \end{array} \right\} $$
  </td>
</tr>
<tr>
  <td>
  <a href="python_mds/load_write_files.html">10. Reading and writing data to files</a>
  </td>
  <td><pre>
  x = np.loadtxt('demo.csv', delimiter=',')
  y = pd.read_csv('demo.csv')
  </pre></td>
  <td>Getting data loaded and written to and from files</td>
  <td>$$$$</td>
</tr>
<tr>
  <td>
  <a href="python_mds/numpy.html">11. Numpy</a>
  </td>
  <td><pre>
  import numpy as np
  demo = np.array([[1, 2, 3],
                   [4, 5, 6]])
  demo.reshape(-1, 2)
  </pre></td>
  <td>The foundational mathematics package that offers many features similar to R's vectors.</td>
  <td>$$X(X^TX)^{-1}X$$</td>
</tr>
<tr>
  <td>
  <a href="python_mds/pandas.html">12. Pandas</a>
  </td>
  <td><pre>
  import pandas as pd
  pd.DataFrame([{'sex': 'M', 'score': 2},
                {'sex': 'F', 'score': 8}])
  </pre></td>
  <td>Python needed something like R's data frames that could handle multiple types of data in a tabular format</td>
  <td></td>
</tr>
<tr>
  <td>
  <a href="python_mds/regular_expression.html">13. Text manipulation and regular expression</a>
  </td>
  <td><pre>
  import re
  re.compile('[A-Z][a-z]+').search('Python')
  </pre></td>
  <td>How can we express general rules in text like how proper nouns start with a capital letter followed by one or more lower-cased letters.</td>
  <td></td>
</tr>
<tr>
  <td>
  <a href="python_mds/mapping.html">14. Mapping functions instead of looping</a>
  </td>
  <td><pre>
  from functools import reduce
  abs_nums = map(abs, [-1, 2, 0])
  tot_mag = reduce(lambda x, y: x + y, abs_nums)
  </pre></td>
  <td>How can we separate the parallizable operations from the ones that cannot?</td>
  <td>$$$$</td>
</tr>
<tr>
  <td>
  <a href="python_mds/date_time.html">15. Date and Time Objects</a>
  </td>
  <td><pre>
  import datetime
  datetime.datetime.now()
  </pre></td>
  <td>How can we handle date/time values since they have different conventions
  from usual numbers. E.g. 60 secs is in 1 minute.</td>
  <td>$$$$</td>
</tr>
<tr>
  <td>
  <a href="python_mds/plotting.html">16. Data visualization with seaborn</a>
  </td>
  <td><pre>
  import matplotlib.pyplot as plt
  import numpy as np
  import seaborn as sns
  x = np.linspace(-1, 1, 100)
  y = (0.1 * x - 0.5 * np.power(x, 2)
       + np.random.normal(size=len(x),
                          scale=0.03))
  sns.relplot(x, y)
  plt.show()
  </pre></td>
  <td>A picture is worth a thousand words</td>
  <td>$$$$</td>
</tr>
<tr>
  <td>
  <a href="python_mds/api.html">17. Interacting with APIs</a>
  </td>
  <td><pre>
  </pre></td>
  <td>To interact with machines, especially online, there is a standard protocol
      to give and get data.
  </td>
  <td>$$$$</td>
</tr>
<tr>
  <td>
  <a href="python_mds/model_fitting.html">18. sklearn and fitting models</a>
  </td>
  <td><pre>
  from sklearn.linear_model import LinearRegression
  ols = LinearRegression().fit(X, Y)
  pred = ols.predict(X2)
  </pre></td>
  <td>Models are mathematical instruments that can help scientist understand patterns in
      the data, understand how the world works, or to simply predict future outcomes.
      These models are tuned and validated using data. This module talks about fitting
      different models with data using `sklearn`.</td>
  <td>$$Y = f(X, \beta) + \epsilon$$
      $$\hat{\beta} = \arg\min_\beta Loss(Y, \hat{Y}(\beta))$$
  </td>
</tr>
<tr>
  <td>
  <a href="python_mds/optimization.html">19. Basic Optimization</a>
  </td>
  <td><pre>
  from scipy.optimize import minimize

  min_out = minimize(obj)
  </pre></td>
  <td>To fit a model to data, we need to define what a good model (or bad model) looks like. Finding the least bad or best model is an optimization exercise.</td>
  <td>$$$$</td>
</tr>
<tr>
  <td><a href="python_mds/sql.html">20. SQL</a></td>
  <td><pre>
  SELECT
    COUNT(DISTINCT(customer_id)) AS uniq_users
  FROM
    orders
  </pre></td>
  <td>Data often sits in a database and SQL is one of the most popular languages we use to query data from databases. Python3 has a built-in library that allows us to interface with SQLite.</td>
  <td>$$$$</td>
</tr>
<tr>
  <td>
  <a href="python_mds/random_functions.html">21. Random functions</a>
  </td>
  <td><pre>
  import random
  random.gauss(0, 1)
  random.choice(['heads', 'tails'])
  </pre></td>
  <td>To sample from a large list of items, we need something that can generate pseudo-randomness.</td>
  <td>$$Y \sim F$$</td>
</tr>
<tr>
  <td>Bootstrapping</td>
  <td><pre>
  </pre></td>
  <td></td>
  <td>$$$$</td>
</tr>
</table>


{% include lib/mathjax.html %}
