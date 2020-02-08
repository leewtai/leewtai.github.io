# Standard Error

When estimating a numeric value, there are various methods to estimate it.
**Standard error** is one particular way to measure the magnitude of the estimation error.

#### Intuitive example
For example,

For the purposes of estimation, a smaller $$SE(\hat{\theta})$$ is always better. On the other hand,
the same cannot be said for $$SD(\hat{\theta})$$ because an arbitrary constant, not dependent on data,
will have $$SD(\hat{\theta})=0$$ but its $$SE(\hat{\theta})$$ will be high due to bias (see the bias-variance
trade-off).


#### Mathematical formalism
Mathematically, if we call the quantity we are estimating $$\theta$$ and
an arbitrary estimate as $$\hat{\theta}$$. Then mathematically, the standard error is

$$\sqrt{E([\hat{\theta} - \theta]^2)}$$

This is very similar to the standard deviation calculation but 
$$\theta$$ here is replaced by $$E(\hat{\theta})$$. This can be confusing to students
when $$E(\hat{\theta})=\theta$$ (i.e. when $$\hat{\theta}$$ is unbiased).

##### Special case - The average


#### Coding example
```python
import numpy as np

theta = 3
n = 100
sim_num = 1000

data = np.random.exponential(scale=theta, size=n)

# Intro Stat
se_samp_avg = 

theta_hats = {'mean': np.mean,
              'bad_est': lambda x: 0,
              'median': np.median}

for _ in range(sim_num):
    data = np.random.exponential(scale=theta, size=n)
    [map(theta_hat, data) for theta_hat in theta_hats]

```


## Concept inventory
TBD

## Common misconceptions
- "SE is $$SD(Y)/\sqrt{n}$$"
    - The issue with this that you have not specified your estimate.
    - The reason you'll see this sometimes is because the context
      is focused on using the sample average, $$\bar{Y}$$ as an estimate
      for the population average.


## Dependent concepts
- Expectation
- Estimation
- standard deviation

{% include lib/mathjax.html %}
