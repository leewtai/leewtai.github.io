from time import time
from itertools import chain

import matplotlib.pyplot as plt
import numpy as np
import yaml
import statsmodels.api as sm
from scipy.optimize import approx_fprime, minimize
from scipy.integrate import simps


with open("x.yaml", "r") as file:
    x = yaml.load(file)

with open("y.yaml", "r") as file:
    y = yaml.load(file)


def poly_design_matrix(x, deg):
    powers = list(range(deg + 1))
    x_arr = np.array(x).reshape(-1, 1)
    x_poly = np.power(x_arr, powers)

    return x_poly


# This should be replaced with the Zeta function fits
funs = {}
delta_funs = {}
poly_deg = 3
for irrep in x:
    x_mat = poly_design_matrix(x[irrep], poly_deg)
    ols_est = sm.OLS(y[irrep], x_mat).fit()

    # It's important to define the defaults to force an evaluation in Python
    # Otherwise lazy evaluation will later only use the last set of parameters
    def fun_temp(x, coeff=ols_est.params):
        return(poly_design_matrix(x, poly_deg).dot(coeff))
    funs.update({irrep: fun_temp})

    # Skip the first parameter since the intercept dr
    def nabla_fun_temp(x, fun_temp=fun_temp, tol=1e-8):
        return approx_fprime(x, fun_temp, tol)

    delta_funs.update({irrep: nabla_fun_temp})


# To calcualte the covariance necessary for the weighted line,
# we need to calculate the position of (x, y) along the curve
def calc_len(x0, x1, delta_fun, tol=1e-4):
    ''' The formula of the arc len along a differentiable line is
    \int_a^b \sqrt{1 + f'(x)^2} dx
    '''
    if x0 > x1:
        x_temp = x0
        x0 = x1
        x1 = x_temp
    steps = int(np.ceil((x1 - x0) / tol))
    xs = np.linspace(x0, x1, steps)
    dfx = np.concatenate([delta_fun(xii) for xii in xs])
    ys = np.sqrt(1 + np.power(dfx, 2))

    return simps(ys, xs)


dist_to_avg = {}
for irrep in x:
    x_avg = np.mean(x[irrep])
    dist_to_avg.update({
        irrep: [calc_len(xi, x_avg, delta_funs[irrep]) for xi in x[irrep]]
        })


for i in y:
    fig, axes = plt.subplots(1, 2)
    axes[0].scatter(x[i], y[i])
    axes[0].scatter(x[i], funs[i](x[i]), color='black', s=0.2)
    axes[0].set_xlabel('x')
    axes[0].set_ylabel('y')
    y_diff = y[i] - np.mean(y[i])
    axes[1].scatter(dist_to_avg[i], y_diff, s=0.2)
    axes[1].plot([0, np.max(y_diff)], [0, np.max(y_diff)], color='black')
    axes[1].plot([0, -np.min(y_diff)], [0, np.min(y_diff)], color='black')
    axes[1].set_xlabel('distance in length')
    axes[1].set_ylabel('distance in y')
    plt.savefig('len_vs_y_dist_irrep_{}.png'.format(i))
    plt.close()


len_mat = np.stack([dist_to_avg[i] for i in x])
len_cov = np.cov(len_mat)
len_prec = np.linalg.inv(len_cov)

len_cov = np.empty((len(y), len(y)))
for i in range(len(y)):
    for j in range(len(y)):
        np.sum(dist_to_avg[i] * dist_to_avg[j])


def intersect(x, fun1, lin_fun2, xtol=1e-8):
    opt = minimize(lambda z: np.power(fun1(z) - lin_fun2(z), 2),
                   x, method="Nelder-Mead", options={"xatol": xtol})
    assert opt.fun < 1e-8 or opt.success

    return opt.x


def obj(par, eval_locs, funs, points=[]):
    def lin_fun(x):
        return par[0] + x * par[1]

    dists = []
    for xi, fi in zip(eval_locs, funs):
        new_x = intersect(xi, fi, lin_fun)
        dists.append(calc_len(new_x[0], xi, fi))

    dist_vec = np.stack(dists).reshape(-1, 1)
    weighted_dist = dist_vec.T.dot(len_prec).dot(dist_vec)

    return weighted_dist


irreps = [i for i in x]
ordered_funs = [funs[i] for i in irreps]
x_avgs = [np.mean(x[i]) for i in irreps]
y_avgs = [np.mean(y[i]) for i in irreps]

ols_start = sm.OLS(np.array(y_avgs), sm.add_constant(np.array(x_avgs))).fit()
# Trial run
obj(ols_start.params, x_avgs, ordered_funs)

a = time()
opt = minimize(obj, ols_start.params,
               args=(x_avgs, ordered_funs),
               method='Nelder-Mead', options={"xatol": 1e-8})
time() - a

x_vals = list(chain.from_iterable(x.values()))
y_vals = list(chain.from_iterable(y.values()))
xs = np.linspace(np.min(x_vals), np.max(x_vals), 100)
for i in x:
    plt.scatter(x[i], y[i], color='black')

x_mat = poly_design_matrix(xs, 1)
plt.plot(xs, x_mat.dot(opt.x), color='blue')
plt.plot(xs, x_mat.dot(ols_start.params), color='green')
plt.ylim(np.percentile(y_vals, [0.1, 99.9]))
plt.scatter(x_avgs, y_avgs, color='red')
plt.savefig('len_weighted_best_fit.png')
plt.close()
