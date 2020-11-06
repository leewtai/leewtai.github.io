# Research and project ideas

This folder stores all the different projects and ideas


## Ideas

#### Model for Liebig's Barrel
In agriculture, the belief is that the shortest resource will dictate
the growth of the crop. Is there a way to recover the cause or threshold
for each resource using statistical learning?

#### Approximate Bayesian Computation
Besides avoiding the likelihood calculation, ABC is more intuitive to scientists.
Can ABC methods be more robust/correct when the model is incorrect?
- Use ABC for amazon review problem: one product with 10 reviews but 5 stars, one product with 100 reviews but 4.5 stars, which one is better?
    - Conjugate priors are not intuitive.
- Approximate Frequetist Computation?
    - Is replacing the likelihood in MLE with summary statistics just a peusdo-likelihood? What should we expect?
    - Should we teach confidence intervals as "candidate intervals" instead?


#### Bayesian Optimization Numerical issue
We know that the joint predictive distribution can be expressed as the product
of a conditional distributions. This allows us to sample sequentially without
pre-determining the sample locations. 

$$P(Y_1, \dots, Y_N | Y) = P(Y_1|Y)P(Y_2|Y_1, Y)\dots P(Y_N|Y, Y_1, \dots, Y_{N-1})$$

The problem with this, however, is that the conditional distribution is numerically
unstable. Are there ways to mitigate this?

#### Data anti-trust as an idea
Can we quantify when someone has "too much" data?
How would we even go about doing this?
Legal definitions for adverse impact is defined for discrimination,
anti-trust also has similar metrics but is more applicable to non-data
businesses.

#### Connecting research farm data with grower farm data
It's common that plant research is done in highly controlled environments but
farmer's data is often much noisier. It's not obvious how to connect the
2 different sets of data together.

#### WLS in non-linear cases producing bias?
see physics-fun/ for the details. Weighted least squares can produce very biased
predictions if the data is highly non-linear and non-Gaussian, why is this
given regression can be phrased as a weighted average.

#### Are there usecases for an algorithm that gets "bored"?
Recommendation algorithms dwell on repeated recommendations and can discourage
users to continue their subscription. Is there a way to modify the objective function
such that algorithms will constantly adapt? Do we need to model boredom?

#### Can we train a linear model without using all the data?
Sufficient statistic, differential privacy, core sets, data sketching, Nyström approximations

#### Data science with dance
Can we detect emotion from people's movement?

#### Can we create a mapping between problems and concepts automatically?

#### Quantum computing configuration using ML?

#### Analyzing restaurant photos + menus

#### Poverty metric
This is currently done by performing PCA on "assets owned".
This method isn't necessarily robust and is calibrated against consumption.

#### Help students find professors to work with
Explore the citation graphs on professor's recent publications for students to see.

#### Multi-armed bandit vs A/B testing
Tech companies often start off with A/B testing then start to wonder
about replacing it with the multi-armed bandit.
The problem is these methods are doing 2 different things: one is effect estimation
and the other is optimization.


{% include lib/mathjax.html %}
