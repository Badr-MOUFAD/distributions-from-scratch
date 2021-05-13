# computation
import numpy as np
from scipy.integrate import quad
from scipy.optimize import fsolve

from step_functions import Heaviside

# graph
import matplotlib.pyplot as plt
from plotly import graph_objects as go
import plotly.io as pio

pio.templates.default = "plotly_white"


class ExpoDistribution:
    def __init__(self, lam):
        self.lam = lam
        return

    def __call__(self, x):
        lam = self.lam

        return lam * np.exp(-lam * x) * Heaviside(x0=0)(x)

    def cumulative_distribution(self, x):
        # take val and ignore error
        return quad(lambda u: self(u), 0, x)[0]




lam = 1
t = np.linspace(-2, 10)
exp_dis = ExpoDistribution(lam=lam)

# y = []
#
# for val in t:
#     y.append(exp_dis.cumulative_distribution(val))
#
# plt.plot(t, y)
# plt.show()


# exclude borders
probabilities = np.linspace(0, 1, 50)[1:-1]
constructed_exp_dist = []

for p0 in probabilities:
    equation_function = lambda x: exp_dis.cumulative_distribution(x) - p0

    y0, = fsolve(func=equation_function, x0=np.array([0]))

    constructed_exp_dist.append(y0)

plt.plot(probabilities, constructed_exp_dist)
plt.show()
