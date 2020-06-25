from itertools import product

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import statsmodels.api as sm
from scipy.optimize import minimize


age_cap = 18

sns.set()
df = pd.read_csv("../../../../usecases_data/health_nutrition_survey"
                 "/nhanes_2015_2015_demo.csv")
# We intentionally choose the minors to avoid the extreme bimodal distribution
# that might confuse the students. We also ignore the "sampling weights" in
# NHANES
youth = df.loc[df.age_years < age_cap, :]
sns.distplot(youth.weight_kg, kde=False)
plt.title('Weight Dist of Minors in NHANES 2015-2016 (Unweighted)')
plt.xlabel('Weight (kg)')
plt.savefig('../graphs/nhanes_weight_dist.png')
plt.close()

sns.distplot(youth.weight_kg, kde=False)
plt.title('Weight Dist of Minors in NHANES 2015-2016 (Unweighted)')
plt.vlines(x=[youth.weight_kg.mean() + np.random.uniform(-3, 3, 2),
              youth.weight_kg.median() + np.random.uniform(-3, 3, 2)],
           ymin=-1, ymax=450)
plt.xlabel('Weight (kg)')
plt.savefig('../graphs/nhanes_weight_dist_with_guesses_for_center.png')
plt.close()

sns.scatterplot(x=youth.height_cm, y=youth.weight_kg)
plt.title('Weight by Height of Minors in NHANES 2015-2016 (Unweighted)')
plt.ylabel('Weight (kg)')
sns.scatterplot(x=youth.height_cm, y=youth.weight_kg)
plt.xlabel('Height (cm)')
plt.savefig('../graphs/nhanes_height_weight_scatter.png')
plt.close()

sns.scatterplot(x=youth.height_cm, y=youth.weight_kg)
lin_loc = [youth.height_cm.min(), youth.height_cm.max()]
lin_y = [youth.weight_kg.mean() for x in lin_loc]
plt.plot(lin_loc, lin_y)
plt.title('Weight by Height of Minors in NHANES 2015-2016 (Unweighted)')
plt.ylabel('Weight (kg)')
plt.xlabel('Height (cm)')
plt.savefig('../graphs/nhanes_height_weight_scatter_with_avg.png')
plt.close()

X = sm.add_constant(youth.height_cm)
ols = sm.OLS(youth.weight_kg, X, missing='drop').fit()
lin_y = [ols.params[0] + ols.params[1] * x for x in lin_loc]

sns.scatterplot(x=youth.height_cm, y=youth.weight_kg)
plt.plot(lin_loc, lin_y)
plt.title('Weight by Height of Minors in NHANES 2015-2016 (Unweighted)')
plt.ylabel('Weight (kg)')
plt.xlabel('Height (cm)')
plt.savefig('../graphs/nhanes_height_weight_scatter_with_ols.png')
plt.close()


def weight_sqloss1d(parameters, data):
    error = data.weight_kg - parameters
    sq_error = error**2
    return sq_error.sum(skipna=True)


weight_sqloss1d(35, youth)
weight_sqloss1d(40, youth)
weight_sqloss1d(34, youth)


vals_to_seed = [30 + i for i in range(10)]
obj = [weight_sqloss1d(i, youth) for i in vals_to_seed]
sns.scatterplot(vals_to_seed, obj, hue=obj)
plt.title('Objective by Best Weight')
plt.xlabel('Weight (kg)')
plt.savefig('../graphs/obj_1D_parameter_sweep.png')
plt.close()


def weight_sqloss2d(parameters, data):
    # \hat{W}_j = a + b * H_j
    est_weights = parameters[0] + parameters[1] * data.height_cm
    error = data.weight_kg - est_weights
    sq_error = error**2
    return np.sqrt(sq_error.mean(skipna=True))


num_cands = 100
params = {
    'intercept': (-300, 200),
    'slope': (-2, 4)}
param_sweep = {
    par: np.linspace(low, high, num_cands)
    for par, (low, high) in params.items()}

xyz = np.empty((num_cands**2, 3))
for i, (x, y) in enumerate(product(param_sweep['intercept'],
                                   param_sweep['slope'])):
    z = weight_sqloss2d([x, y], youth)
    xyz[i, :] = x, y, z

fig = sns.scatterplot(xyz[:, 0], xyz[:, 1], hue=xyz[:, 2])
fig.legend_.remove()
plt.title('Squared Loss: dark=high, light=low')
plt.xlabel('Intercept')
plt.ylabel('Slope')
plt.savefig('../graphs/obj_2D_parameter_sweep.png')
plt.close()

opt_out = minimize(lambda x: weight_sqloss1d(x, youth), 35)

reasonable_start = [0, 0.5]
opt_out = minimize(lambda x: weight_sqloss2d(x, youth),  # Objective function
                   reasonable_start)  # starting value


def sqloss_deriv(parameter, data):
    n = data.shape[0]
    return 2 * parameter * n - 2 * data.weight_kg.sum()


deriv = [sqloss_deriv(i, youth) for i in vals_to_seed]
sns.scatterplot(vals_to_seed, deriv, hue=deriv)
plt.title('Objective Derivative')
plt.xlabel('Weight (kg)')
plt.savefig('../graphs/obj_1D_derivative.png')
plt.close()
