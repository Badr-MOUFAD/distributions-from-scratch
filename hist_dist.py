import numpy as np
from scipy.stats import expon, norm

import matplotlib.pyplot as plt

from class_distribution_function import DistributionFunction
from step_functions import Heaviside, RecFunction


# samples = norm.rvs(size=10000)
# nb_bins = int(1 + 3.322 * np.log(len(samples)))
#
# plt.hist(samples, density=True, bins=nb_bins)
# plt.show()


# dist_func = lambda u: np.exp(-u) * Heaviside()(u)
# interval = [0, np.inf]
#
# dist = DistributionFunction(func=dist_func, interval=interval)

# dist_func = lambda u: (2 * np.pi) ** (-1 / 2) * np.exp(-u ** 2 / 2)
# interval = [-5, 5]
#
# dist = DistributionFunction(func=dist_func, interval=interval)

interval = [-5, 5]
dist_func = lambda u: (2 * np.pi) ** (-1/2) * np.exp(-u ** 2 / 2) * RecFunction(*interval)(u) # lambda u: 2 / np.pi * np.cos(u) ** 2 * RecFunction(*interval)(u) # lambda u: 3 * u ** 2 * RecFunction(*interval)(u) # lambda u: (1 / 2) * np.sin(u) * RecFunction(0, np.pi)(u)

dist = DistributionFunction(func=dist_func, interval=interval)

actulisation = (1 + 0.1)
x = np.linspace(interval[0] * actulisation, interval[1] *actulisation , 200)

# plot dist function
plt.plot(x, dist(x))

# plot histogram of dist
size = 1000
# nb bins chosen using Sturge’s Rule
nb_bins = int(1 + 3.322 * np.log(size))

plt.hist(dist.generate_samples(size=1000), density=True, bins=nb_bins)

plt.title(r"Distribution: $\frac{2}{\pi} cos(u)^2 \mathbb{1}_{[0, \pi]}$")
plt.xlabel("X")
plt.ylabel("frequency")

plt.xlim(interval[0] * actulisation, interval[1] * actulisation)
plt.show()
