import random
import numpy as np
import matplotlib.pyplot as plt

# Exercise 1
n = 100
num_sim = 1000
outcome = []

for i in range(num_sim):
    new_data = np.random.normal(0, 5, n)
    y_avg = np.mean(new_data)
    # In class I forgot the sqrt(n) factor!
    y_sd = np.sqrt(sum((new_data - y_avg)**2) / (n-1))
    y_se = y_sd / np.sqrt(n)
    stat = abs(y_avg / y_se)
    outcome.append(stat >= 1.96)

np.mean(outcome)
# Notice this is a t-distribution with n-1 degrees of freedom


# Exercise 2, is the median a better estimate than the avg for E(Y)
# When Y~Normal(0, 5^2)

def bad_est(x):
    if random.choice([True, False]):
        out = np.percentile(x, 75)
    else:
        out = np.percentile(x, 25)
    return out


n = 100
num_sim = 1000
outcome = np.empty((num_sim, 3))
true_mean = 0
for i in range(num_sim):
    new_data = np.random.normal(true_mean, 5, n)
    outcome[i, 0] = np.mean(new_data)
    outcome[i, 1] = np.percentile(new_data, 50)
    outcome[i, 2] = bad_est(new_data)

fig, axes = plt.subplots(1, 3)
for i in range(outcome.shape[1]):
    axes[i].hist(outcome[:, i])
    axes[i].set_xlim(np.min(outcome), np.max(outcome))
plt.show()

# Not recommended
np.abs(np.apply_along_axis(np.mean, 0, outcome) - true_mean)
# Better
np.apply_along_axis(lambda x: np.mean(np.power(x - true_mean, 2)), 0, outcome)
np.apply_along_axis(lambda x: np.mean(np.abs(x - true_mean)), 0, outcome)
