# Research and project ideas

This folder stores all the different projects and ideas


## Ideas

#### Model for Liebig's Barrel
In agriculture, the belief is that the shortest resource will dictate
the growth of the crop. Is there a way to recover the cause or threshold
for each resource?

#### Approximate Bayesian Computation
Besides avoiding the likelihood calculation, ABC is more intuitive to scientists.
Can ABC methods be more robust/correct when the model is incorrect?

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
see physics-fun/ for the details. trouble looking weighted least seems to
cause a negative bias.
