# Pseodo Code

Pseudo code is an outline of how your code would be structured in a format
that is friendly to people who do not understand the syntax of the programming language you're using but is familiar with for-loops, functions, and the algorithm you're coding up.

An example is "use programming to demonstrate the central limit theorem". Such a task involves several steps. In particular:
- What does demonstrate mean?
- What is the central limit theorem?

First, the central limit theorem states that if a random variables $Y\sim F$ where $E(Y^2) < \infty$ (but $F$ may not be Normal) then $\sqrt{n} \bar{Y} \Rightarrow N(E(Y), Var(Y))$. 

To demonstrate this, we should
- Draw samples from a random variable that is not Normal with finite variance.
- Calculate the average of a sizable sample of $Y$.
- Examine the distribution of $\bar{Y}$

The bullet points above are almost an outline, pseudo code just asks
you to add in the for-loops and some key function calls. The key is to
give clarity in the structure of the code even if one does not program
in Python specifically (but does know programming).

- Repeat the following `B` times:
  - Draw `n` values of $Y\sim\Bernoulli(0.1)$
  - Calculate and record $m = mean(Y)$
  - Store the resulting mean in a list called `ms`
- Plot the histogram of the `B` values of `ms` against the density plot of a $Normal(E(Y), \frac{1}{n}Var(Y))$

Here's an example of what the pseudo-code above could be translated into:

```python
import numpy as np
import seaborn as sns

# It's best practice to place all tunable parameters together
B = 1000
n = 100
p = 0.1

# Simulations
ms = []
for _ in range(B):
    ys = np.random.binomial(n=1, p=p, size=n)
    m = np.mean(ys)
    ms.append(m)

# Theoretical target
x_range = np.linspace(np.min(ms), np.max(ms), B)

def normal_density(x, m=0, v=1):
    kernel = np.exp(-0.5 * np.power(x - m, 2) / v)
    norm = np.sqrt(2 * np.pi * v)
    return kernel / norm

y_dens = normal_density(x_range, m = p, v = p * (1 - p) / n)

# plotting
sns.lineplot(x=x_range, y=y_dens, alpha=0.5)
sns.kdeplot(ms, alpha=0.5)
plt.show()
```

Notice that the actual execution includes:
- Python specific syntax
- Parameters necessary for the code to run, e.g. `B`, `p`, `n`, ...
- Distracting code related to our plotting libraries



{% include lib/mathjax.html %}