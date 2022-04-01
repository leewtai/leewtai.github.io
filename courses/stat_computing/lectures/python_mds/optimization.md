# Optimization

Optimization is a useful framework when making a decision. One has to narrow
down an objective, decide on what decisions are within your control, then
"search" for the best option.

In other words, all optimization problems have:
- parameters that can be tuned that will yield different results
- An objective function that depends on the parameters
  - This function may have constraints like the parameters must be non-negative

Therefore all optimization algorithms will require us to pass the objective
function (a function of the parameters) as an input to the algorithm. The algorithm
will then solve for the best set of parameters that will yield the optimal value from the
objective function.

#### Examples - linear regression

One classic example of optimization is solving for the regression coefficients,
i.e. given $$(x_i, y_i), i=1,\dots,n$$, how can we pick the best line that "fits"
to the data.

The objective function in this case is the squared error, $$f(\beta) = \|Y - X\beta\|_2$$
is how we have chosen to formalize the concept of "fit" between arbitrary line and our data.

```python
import numpy as np

sample_size = 100
X = np.random.rand(sample_size, 1)
measurement_error = np.random.normal(
    size=sample_size, scale=0.3).reshape(-1, 1)
# Slope is 1, intercept is 0
Y = X + measurement_error

def ols_obj(beta, X, Y):
    interc, coeffs = beta[0], np.array(beta[1:])
    error = Y - interc - X.dot(coeffs.reshape(-1, 1))
    return np.sum(np.power(error, 2))
```

In the example above, `beta` are the "parameters" that can be tuned where `X` and `Y`
are simply inputs required to calculate the objective function.

## Ways to solve for an optimum

It is important to know the different approaches, even bad ones, to searching
for an optimum.

#### Using calculus
In our regression example above, by design, i.e. the quadratic equation, our objective function
will have a global solution that can be derived from basic calculus. An analytical 
solution would be accurate and fast to compute. However, not
all objective functions are so easily calculated.

Specifically, the regression coefficients have the solution of $$\hat{\beta} = (X^TX)^{-1}X^TY$$

#### The grid-search
The most naive approach is the grid-search. Imagine we have an unknown objective function
that can be evaluated at different parameters. A grid-search would evaluate the function
across possible parameters with an acceptable resolution.

```python
from itertools import product


def unknown_obj(params):
    return np.abs(params[0] - 1.3111111) + np.abs(params[1] + 2.212)

poss_param1 = np.linspace(-3, 3, 1000)
poss_param2 = np.linspace(-3, 3, 1000)

out = []
# Search across all combinations between the two poss_params*
for p1, p2 in product(poss_param1, poss_param2):
    out.append([unknown_obj([p1, p2]), p1, p2])


# Sort by the objective value
print(sorted(out, key=lambda x: x[0])[:1])
```

Notice that our grid-search is limited by the resolution, i.e. `1000` values between `-3` and `3`.
If we wanted a more accurate result, we can perform a finer grid-search closer to our current optimum.
This method is extremely inefficient but it is easy to implement, understand, and can catch surprises.

#### Using optimization algorithms

There are some efficient algorithms that can search for the optimum much more efficiently.
The most efficient ones tend to rely on the gradient to be mathematically exist and can be
numerically approximated. The gradient-free methods often depend on some intuition that drives
the search.

Since our `unknown_obj` above is not differentiable at the minimum, methods that depend on a the
gradient may not perform well. On the other hand, gradient-free methods may do much better.
All of these algorithms are coded behind different "methods" in [`scipy.optimize.minimize`](https://docs.scipy.org/doc/scipy-0.15.1/reference/generated/scipy.optimize.minimize.html)

Before implementing these methods, similar to how the grid-search requires users to provide
a reasonable range, these algorithms often require the user to provide an initial guess
for the optimal parameters so it begins its search around the initial guess. This is often randomized
a bit to ensure the final solution is not too sensitive to the initial guess.

```python
from scipy.optimize import minimize


initial_guess_xs = [0, 0]
default_min = minimize(unknown_obj, initial_guess_xs)
print(default_min.success)
print(default_min.message)
nelder_min = minimize(unknown_obj, initial_guess_xs, method='Nelder-Mead')
print(nelder_min.success)
print(nelder_min.x)
```

## Validating optimization outcomes

Similar to how we validate models fitted to data, we are also able to judge the quality of the research.

That said, it is vital to check the convergence of the algorithm. Most algorithms stop once the objective
function improvement is less than a threshold or if the gradient indicates that we have reached
an optimum (local or global). If the algorithm stops before reaching these stopping criteria,
a `message` is often associated and one would need to react to the message.

Common solutions to solve for non-convergence in optimization algorithms are:
- Chcek if we hit the maximum number of function evaluations or if we hit the boundary for
  the parameter. The former can be solved by simply increasing the maximum, where the second
  could be fixed by expanding the search area or relaxing the constraints.
- Check if the objective function evaluations are smooth near the optimum. Some calculations
  can lead to floating point issues that can cause optimization algorithms to fail. The solution
  here tends to be to fix the source of the issue. If this is caused by the lack of data,
  then collect more. If this is caused by some calculation that can be done more robustly, you
  should fix that.
- Check if different initial_guesses changes the final `x` value. If this is the case, then it is
  important to save the attempted objective function evaluations. The objective function may have
  multiple optimums and the algorithm may be stuck locally.


{% include lib/mathjax.html %}
