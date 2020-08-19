# Research and project ideas

This folder stores all the different projects and ideas


## Ideas

#### Model for Liebig's Barrel
In agriculture, the belief is that the shortest resource will dictate
the growth of the crop. Is there a way to recover the cause or threshold
for each resource?

#### Approximate Bayesian Computation
Besides avoiding the likelihood calculation, ABC is more intuitive to scientists.
Are there ways to produce samples more efficiently for ABC methods?
Can ABC methods be more robust when the model is incorrect?

#### Bayesian Optimization Numerical issue
We know that the joint predictive distribution can be expressed as the product
of a conditional distributions. This allows us to sample sequentially without
pre-determining the sample locations. 

$$P(Y_1, \dots, Y_N | Y) = P(Y_1|Y)P(Y_2|Y_1, Y)\dots P(Y_N|Y, Y_1, \dots, Y_{N-1})$$

The problem with this, however, is that the conditional distribution is numerically
unstable. Are there ways to mitigate this?

####
