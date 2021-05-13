import numpy as np
import matplotlib.pyplot as plt

from step_functions import Heaviside, RecFunction
from class_distribution_function import DistributionFunction


# init fig and axs
fig, axs = plt.subplots(1, 3)

uniform = axs[0].plot([], [])
dist_func = axs[1].plot([], [])
hist = axs[2].hist()