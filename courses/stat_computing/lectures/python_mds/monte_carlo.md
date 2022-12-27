# Monte Carlo Methods

In real application, we often encounter situations where a certain mathematical
value is well defined but has no close form or is too expensive to calculate exactly.
For example, what is the chance the global average temperature will rise by 1 degree in
15 years? We may have the ability to simulate different climate and weather scenarios to
estimate this probability. 

These methods in general are called Monte Carlo methods, where
we estimate probabilistic events by simulate different scenarios then compute the fraction
of scenarios with the event occurring. This relies on the law of large numbers and is
one unique application in statistical computing.

## Example approximating the value of pi

We know that the area in a circle is $$\pi r^2$$, so if we
sample 2 Uniform[0,1] random variables, we know the fraction of
points within the unit circle is $$\frac{\pi}{4}$$. So we can approximate
$$\pi$$ with $$4 * \frac{1}{B}\sum_i 1[X_i^2 + Y_i^2 \leq 1]$$

```python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

Bs = [10**i for i in range(2, 7)
      for _ in range(5)]
proxies = []
for B in Bs:
    xy = np.random.uniform(0, 1, size=B * 2).reshape(-1, 2)
    dist_to_origin = np.sum(np.power(xy, 2), axis=1)
    frac_in_circle = np.mean(dist_to_origin <= 1)
    proxies.append(4 * frac_in_circle)

ax = sns.lineplot(x=Bs, y=proxies)
ax.axhline(np.pi, c='#FF0000')
plt.show()
```

- For each simulation, we produce `B` different scenarios (we increase this
  but also create replicates!)
- Each scenario creates an $$(X_i, Y_i)$$ pair from 2 independent Uniform[0, 1]
- We calculate the distance from the origin for each pair.
- We calculate the fraction within the unit circle.


{% include lib/mathjax.html %}
