import numpy as np
from scipy.integrate import quad
from scipy.optimize import fsolve

import matplotlib.pyplot as plt

from step_functions import Heaviside, RecFunction


class DistributionFunction:
    # func with following props
    # continuous, defined on an interval of form
    # [a, b], (-inf, b], [a, +inf)
    # with integral == 1
    def __init__(self, func, interval):
        self.a, self.b = interval

        # vectorize dist function
        self.func = np.vectorize(func)
        return

    def __call__(self, x):
        return self.func(x)

    # cumulative distribution function F
    def cumulative_dist_function(self, x):
        a, b = self.a, self.b
        # case x lies on the left side of domain
        # of definition
        if x < a:
            return 0

        # case x lies on the left side of domain
        # of definition
        if x >= b:
            return 1

        # integrate from the right
        if a == -np.inf:
            return 1 - quad(lambda u: self(u), x, b)[0]

        return quad(lambda u: self(u), a, x)[0]

    # for a given prob p0 find corresponding y
    # for which F(y) = p0
    def map_dist_uniform(self, p0):
        # equation to solve
        equation_func = lambda x: self.cumulative_dist_function(x) - p0

        # starting point of solver
        # start from the finite border
        # a, b = self.a, self.b
        #
        # m = min(a, b)
        # M = max(a, b)
        #
        # x0 = m if m != -np.inf else M

        # solve and unpack
        y = fsolve(func=equation_func, x0=np.array([0]), full_output=True)

        return y[0][0]


# # example
# dis_func = lambda u: (1 / np.pi) * 1 / (1 + u ** 2) * RecFunction(-10, 10)(u)
#
# dist = DistributionFunction(func=dis_func, interval=[-10, 10])
#
# # plot of distribution
# x = np.linspace(-10, 10, 200)
# plt.plot(x, dist(x))
#
# plt.show()
#
# # plot of cumulative distribution function
# probs = []
#
# for val in x:
#     p = dist.cumulative_dist_function(val)
#
#     probs.append(p)
#
# plt.plot(x, probs)
# plt.show()
#
# # plot mapping uniform distribution
#
# # remove borders
# probs = np.linspace(0, 1, 100)[1:-1]
# y = []
#
# for p0 in probs:
#     y0 = dist.map_dist_uniform(p0)
#
#     y.append(y0)
#
# plt.plot(probs, y)
#
# plt.show()
