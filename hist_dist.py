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

dist_func = lambda u: (1 / 2) * np.sin(u) * RecFunction(0, np.pi)(u)
interval = [0, np.pi]

dist = DistributionFunction(func=dist_func, interval=interval)

x = np.linspace(-0.5, np.pi + 0.5, 200)

# plot dist function
plt.plot(x, dist(x))
plt.plot(x, dist.F(x))

# plot histogram of dist
size = 1000
# nb bins chosen using Sturge’s Rule
nb_bins = int(1 + 3.322 * np.log(size))

plt.hist(dist.generate_samples(size=1000), density=True, bins=nb_bins)

plt.title("Uniform distribution")
plt.xlabel("X")
plt.ylabel("frequency")

plt.xlim(-0.5, np.pi + 0.5)
plt.show()
