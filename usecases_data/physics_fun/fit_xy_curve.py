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
    # The s parameter here may need to be tuned if the data changes
    tck = interpolate.splrep(x=x_arr[x_ord], y=y_arr[x_ord], s=1e-3)

    # It's important to define the defaults to force an evaluation in Python
    # Otherwise lazy evaluation will later only use the last set of parameters
    def fun_temp(x, spline_rep=tck):
        return(interpolate.splev(x, spline_rep, der=0))
    funs.update({irrep: fun_temp})

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


# If the graphs here look bad, tune the s parameter when fitting splines
# smaller s = less smoothing = more volatile curve behavior between data
# points. Given how smooth your functions are, I think you can deal with
# larger s values.

logging.info('plotting to see distance comparison')
for i in y:
    fig, axes = plt.subplots(1, 2)
    axes[0].scatter(x[i], y[i])
    xs = np.linspace(np.min(x[i]), np.max(x[i]), 2000)
    ys = funs[i](xs)
    axes[0].plot(xs, ys, color='black')
    axes[0].set_xlabel('x')
    axes[0].set_ylabel('y')
    axes[1].scatter(x[i], dist_to_avg[i], s=0.2)
    axes[1].set_ylabel('distance in length to avg')
    axes[1].set_xlabel('x')
    plt.savefig('len_vs_y_dist_irrep_{}.png'.format(i))
    plt.close()


# logging.info('Compute inverse covariance matrix')
# If you empirically derive it from the "Y", this is less desirable
# because it's then fixed for all possible x values
# len_mat = np.stack([dist_to_avg[i] for i in x])
# len_cov = np.cov(len_mat)
# len_prec = np.linalg.inv(len_cov)


def intersect(x, fun1, lin_fun2, xtol=1e-8):
    opt = minimize(lambda z: np.power(fun1(z) - lin_fun2(z), 2),
                   x, method="Nelder-Mead", options={"xatol": xtol})
    assert opt.fun < 1e-8 or opt.success

    return opt.x


def obj(par, eval_locs, funs, delta_funs, len_prec):
    def lin_fun(x):
        return par[0] + x * par[1]

    dists = []
    for xi, fi, dfdxi in zip(eval_locs, funs, delta_funs):
        # For each irrep, where does the line intersect the curve
        # the xi is used as a starting value to find the intersection
        intersect_x = intersect(xi, fi, lin_fun)
        dists.append(calc_len(intersect_x[0], xi, dfdxi))

    dist_vec = np.stack(dists).reshape(-1, 1)
    weighted_dist = dist_vec.T.dot(len_prec).dot(dist_vec)

    return weighted_dist


def get_len_prec(x_vals, delta_funs, x_cov):
    grad = np.diag([dfdxi(xi)
                    for xi, dfdxi in zip(x_vals, delta_funs)])
    len_cov = grad.T.dot(x_cov).dot(grad)
    len_prec = np.linalg.inv(len_cov)
    return len_prec


# Making sure all the values are ordered by `irreps`
irreps = [i for i in x]
x_df = np.stack([x[irrep] for irrep in irreps])
x_cov = np.cov(x_df)
ordered_funs = [funs[i] for i in irreps]
ordered_delta_funs = [delta_funs[i] for i in irreps]
x_avgs = [np.mean(x[i]) for i in irreps]
# calculate y_avgs for initial values from OLS
y_avgs = [np.mean(y[i]) for i in irreps]

len_prec = get_len_prec(x_avgs, ordered_delta_funs, x_cov)
ols_start = sm.OLS(np.array(y_avgs), sm.add_constant(np.array(x_avgs))).fit()
# Trial run
opt = obj(ols_start.params, x_avgs, ordered_funs, ordered_delta_funs, len_prec)

logging.info('Optimizing per bootstrap average')
coeffs_bs = []
for i in range(len(x[irrep])):
    if i % 100 == 0:
        logging.info('bootstrap {}'.format(i))
    x_avgs = [x[irrep][i] for irrep in irreps]
    y_avgs = [y[irrep][i] for irrep in irreps]
    ols_start_bs = sm.OLS(np.array(y_avgs),
                          sm.add_constant(np.array(x_avgs))).fit()
    len_prec = get_len_prec(x_avgs, ordered_delta_funs, x_cov)
    try:
        opt = minimize(obj, ols_start_bs.params,
                       args=(x_avgs, ordered_funs,
                             ordered_delta_funs, len_prec),
                       method='Nelder-Mead', options={"xatol": 1e-8})
        coeffs_bs.append({'opt_x': opt.x.tolist(),
                          'success': opt.success,
                          'opt_fun': opt.fun})
    except:
        coeffs_bs.append('failed at boot index {}'.format(i))

num_failed = np.sum(isinstance(coeff, str) for coeff in coeffs_bs)
logging.info('Number of failed optimizations is {}'.format(num_failed))
logging.info('Storing optimal values')
json.dump(coeffs_bs, open('coeffs_bs.json', 'w'))

logging.info('Plotting uncertainty bounds')
x_vals = list(chain.from_iterable(x.values()))
y_vals = list(chain.from_iterable(y.values()))
xs = np.linspace(np.min(x_vals), np.max(x_vals), 100)
ys_pred = np.stack([
    coeff['opt_x'][0] + coeff['opt_x'][1] * xs for coeff in coeffs_bs
    if coeff['success']])
uncertainty_bounds = np.apply_along_axis(
    lambda z: np.percentile(z, [16, 84]),
    0, ys_pred)

# Plot the bananas
for irrep in y:
    plt.scatter(x[irrep], y[irrep], color="black", s=0.5)
plt.plot(xs, uncertainty_bounds[0, :], color="red")
plt.plot(xs, uncertainty_bounds[1, :], color="red")
plt.ylim(np.percentile(y_vals, [0.1, 99.9]))
plt.savefig('fit_with_ptwise_68conf.png')
plt.close()
