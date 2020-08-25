import logging
import json
from itertools import chain

import matplotlib.pyplot as plt
import numpy as np
import yaml
import statsmodels.api as sm
from scipy.optimize import minimize
from scipy.integrate import simps
from scipy import interpolate


log_file = 'opt_xy.log'
logging.basicConfig(format="%(asctime)-15s %(message)s",
                    filename=log_file,
                    level=logging.INFO)
with open("x.yaml", "r") as file:
    x = yaml.load(file)

with open("y.yaml", "r") as file:
    y = yaml.load(file)


# This should be replaced with the Zeta function fits
logging.info('fitting splines between y and x')
funs = {}
delta_funs = {}
for irrep in x:
    x_arr = np.array(x[irrep])
    y_arr = np.array(y[irrep])
    x_ord = np.argsort(x_arr)
    tck = interpolate.splrep(x=x_arr[x_ord], y=y_arr[x_ord], s=0)

    # It's important to define the defaults to force an evaluation in Python
    # Otherwise lazy evaluation will later only use the last set of parameters
    def fun_temp(x, spline_rep=tck):
        return(interpolate.splev(x, spline_rep, der=0))
    funs.update({irrep: fun_temp})

    # Skip the first parameter since the intercept dr
    def nabla_fun_temp(x, spline_rep=tck):
        return interpolate.splev(x, spline_rep, der=1)

    delta_funs.update({irrep: nabla_fun_temp})


# To calcualte the covariance necessary for the weighted line,
# we need to calculate the position of (x, y) along the curve
def calc_len(x0, x1, delta_fun, tol=1e-5):
    ''' The formula of the arc len along a differentiable line is
        \int_a^b \sqrt{1 + f'(x)^2} dx
    '''
    if x0 > x1:
        x_temp = x0
        x0 = x1
        x1 = x_temp
    steps = int(np.ceil((x1 - x0) / tol))
    xs = np.linspace(x0, x1, steps)
    dfx = np.stack([delta_fun(xii) for xii in xs])
    ys = np.sqrt(1 + np.power(dfx, 2))

    return simps(ys, xs)


logging.info('computing distance along curve for each irrep')
dist_to_avg = {}
for irrep in x:
    logging.info('irrep {}'.format(irrep))
    x_avg = np.mean(x[irrep])
    dist_to_avg.update({
        irrep: [calc_len(xi, x_avg, delta_funs[irrep]) for xi in x[irrep]]
        })


logging.info('plotting to see distance comparison')
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


logging.info('Compute inverse covariance matrix')
len_mat = np.stack([dist_to_avg[i] for i in x])
len_cov = np.cov(len_mat)
len_prec = np.linalg.inv(len_cov)


def intersect(x, fun1, lin_fun2, xtol=1e-8):
    opt = minimize(lambda z: np.power(fun1(z) - lin_fun2(z), 2),
                   x, method="Nelder-Mead", options={"xatol": xtol})
    assert opt.fun < 1e-8 or opt.success

    return opt.x


def obj(par, eval_locs, funs, len_prec=len_prec):
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
opt = obj(ols_start.params, x_avgs, ordered_funs)

logging.info('Optimizing per bootstrap average')
coeffs_bs = []
for i in range(len(x[irrep])):
    if i % 100 == 0:
        logging.info('bootstrap {}'.format(i))
    x_avgs = [x[irrep][i] for irrep in irreps]
    y_avgs = [y[irrep][i] for irrep in irreps]
    ols_start_bs = sm.OLS(np.array(y_avgs),
                          sm.add_constant(np.array(x_avgs))).fit()
    opt = minimize(obj, ols_start_bs.params,
                   args=(x_avgs, ordered_funs),
                   method='Nelder-Mead', options={"xatol": 1e-8})
    coeffs_bs.append({'opt_x': opt.x.tolist(),
                      'success': opt.success,
                      'opt_fun': opt.fun})

logging.info('Storing optimal values')
json.dump(coeffs_bs, open('coeffs_bs.json', 'w'))
x_vals = list(chain.from_iterable(x.values()))
y_vals = list(chain.from_iterable(y.values()))
xs = np.linspace(np.min(x_vals), np.max(x_vals), 100)
x_mat = sm.add_constant(xs)
for opt_i in coeffs_bs:
    plt.plot(xs, x_mat.dot(np.array(opt_i['opt_x'])), color='blue')
for i in x:
    plt.scatter(x[i], y[i], color='black')

plt.plot(xs, x_mat.dot(ols_start.params), color='green')
plt.ylim(np.percentile(y_vals, [0.1, 99.9]))
plt.scatter(x_avgs, y_avgs, color='red')
plt.savefig('fix_w_len_weighted_best_fit.png')
plt.close()
