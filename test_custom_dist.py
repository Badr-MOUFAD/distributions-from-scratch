import numpy as np
from scipy.stats import expon, norm

import matplotlib.pyplot as plt

from class_distribution_function import DistributionFunction
from step_functions import Heaviside, RecFunction


interval = [0, np.pi]
dist_func = lambda u: (1 / 2) * np.sin(u) * RecFunction(*interval)(u)

# interval = [0, np.inf]
# dist_func = lambda u: np.exp(-u) * Heaviside()(u)

dist = DistributionFunction(func=dist_func, interval=interval)

x = np.linspace(-0.5, np.pi * (1 + 0.1), 200)
# x = np.linspace(-0.5, 10, 200)

plt.plot(x, dist(x))
plt.show()

cumul_dist = []
for val in x:
    cumul_dist.append(dist.cumulative_dist_function(val))

plt.plot(x, cumul_dist)
plt.show()
