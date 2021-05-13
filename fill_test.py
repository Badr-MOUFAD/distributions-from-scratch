import numpy as np
import matplotlib.pyplot as plt

from step_functions import Heaviside, RecFunction
from class_distribution_function import DistributionFunction


x_uniform = np.linspace(-1, 2)
x_exp = np.linspace(-1, 10)

fig, ax = plt.subplots(1, 3)

p0 = 0.5
ax[0].plot(x_uniform, RecFunction(0, 1)(x_uniform))
ax[0].plot([p0 for i in range(10)], np.linspace(0, 1, 10), "|", color="r")
ax[0].plot([p0], [1], "o", color="r")

ax[1].plot(x_exp, (lambda u: np.exp(-u) * Heaviside()(u))(x_exp))
ax[0].plot([p0 for i in range(10)], np.linspace(0, 1, 10), "|", color="r")
ax[0].plot([p0], [1], "o", color="r")

ax[2].hist(x=[], density=True)
# ax.plot([5 for i in range(10)], np.linspace(0, 5 ** 2, 10), "|", color="r")
# ax.plot([5], [5 ** 2], "o", color="r")

plt.tight_layout()
plt.show()
