import numpy as np

import matplotlib.pyplot as plt

from tools.class_distribution_function import DistributionFunction
from tools.step_functions import RecFunction


# interval and distribution function
interval = [-5, 5]
dist_func = lambda u: (2 * np.pi) ** (-1/2) * np.exp(-u ** 2 / 2) * RecFunction(*interval)(u)

# construct distribution
dist = DistributionFunction(func=dist_func, interval=interval)

actulisation = (1 + 0.1)
x = np.linspace(interval[0] * actulisation, interval[1] *actulisation , 200)

# plot dist function
plt.plot(x, dist(x))

# plot histogram of dist
size = 1000
# nb bins chosen using Sturge’s Rule
nb_bins = int(1 + 3.322 * np.log(size))

# plot histogram
plt.hist(dist.generate_samples(size=1000), density=True, bins=nb_bins)

# layout
plt.title(r"Distribution: $\frac{2}{\pi} cos(u)^2 \mathbb{1}_{[0, \pi]}$")
plt.xlabel("X")
plt.ylabel("frequency")

plt.xlim(interval[0] * actulisation, interval[1] * actulisation)

plt.show()
