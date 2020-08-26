import json
import numpy as np
import yaml
import matplotlib.pyplot as plt


coeffs = json.load(open('coeffs_bs.json', 'r'))

with open("x.yaml", "r") as file:
    x = yaml.load(file)

with open("y.yaml", "r") as file:
    y = yaml.load(file)

intercepts = [coeff['opt_x'][0] for coeff in coeffs]
slopes = [coeff['opt_x'][1] for coeff in coeffs]

[i for i, j in enumerate(intercepts) if j < -16]
i = 674

[y[irrep][i] for irrep in y]

irrep = 9
xs = np.linspace(-0.03, 0.26, 100)
plt.scatter(x[irrep], y[irrep])
plt.plot(xs, coeffs[i]['opt_x'][0] + coeffs[i]['opt_x'][1] * xs)
plt.show()
plt.close()

ys_pred = np.stack([
    coeff['opt_x'][0] + coeff['opt_x'][1] * xs for coeff in coeffs
    if coeff['success']])

bounds = np.apply_along_axis(
    lambda z: np.percentile(z, [2.5, 97.5]),
    0, ys_pred)
bounds.shape

for irrep in y:
    plt.scatter(x[irrep], y[irrep], color="black", s=0.5)

plt.plot(xs, bounds[0, :], color="red")
plt.plot(xs, bounds[1, :], color="red")
plt.ylim([-1, 3])
plt.savefig('fit_with_ptwise_95conf.png')
plt.close()

plt.scatter(intercepts, slopes)
plt.ylim(np.percentile(slopes, [0.5, 99.5]))
plt.xlim(np.percentile(intercepts, [0.5, 99.5]))
plt.show()
