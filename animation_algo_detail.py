import numpy as np

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from tools.class_distribution_function import DistributionFunction
from tools.step_functions import RecFunction
from tools.function_plot import update_dot_dash_plots


# sample size
size = 5

# distribution function & interval
# interval = [-3.5, 3.5]
# distribution = DistributionFunction(
#     func=lambda u: (2*np.pi) ** (-1/2) * np.exp(-u ** 2 / 2) * RecFunction(*interval)(u),
#     interval=interval
# )

interval = [-1, 2]
distribution = DistributionFunction(
    func=lambda u: (1 + 2 / np.pi) ** (-1) * (-u * RecFunction(-1, 0)(u) + np.sin(np.pi * u) * RecFunction(0, 1)(u) + (u - 1) * RecFunction(1, 2)(u)),
    interval=interval
)


# sample from uniform
probabilities = np.random.rand(size)

# construct mappings
Y = []

for p0 in probabilities:
    y = distribution.map_dist_uniform(p0)

    print(p0)
    Y.append(y)


# animation
# init
fig, axs = plt.subplots(1, 2)

# plot dist functions
interval_unif = [-0.5, 1.5]
nb_points = 1000
t_unif = np.linspace(*interval, nb_points)
axs[0].plot(t_unif, RecFunction(0, 1)(t_unif), color="#1f77b4")

t_dist = np.linspace(*interval, nb_points)
axs[1].plot(t_dist, distribution(t_dist))


# area plots
# unif = axs[0].fill_between([], [], color="#1f77b4")
dist = axs[1].fill_between([], [], color="#1f77b4")

# dot and dash
unif_dot, = axs[0].plot([], [], "o", color='#d62728')
dist_dot, = axs[1].plot([], [], "o", color='#d62728')

unif_dash, = axs[0].plot([], [], "|", linewidth=5, color='#7f7f7f')
dist_dash, = axs[1].plot([], [], "|", linewidth=5, color='#7f7f7f')


def anim(index_frame):
    global unif_dot, unif_dash, dist_dot, dist_dash

    index = index_frame

    unif_dot, unif_dash = update_dot_dash_plots(unif_dot, unif_dash, new_x=probabilities[index], new_y=1)
    dist_dot, dist_dash = update_dot_dash_plots(dist_dot, dist_dash, new_x=Y[index], new_y=distribution(Y[index]))

    t_unif = np.linspace(0, probabilities[index], 1000)
    t_dist = np.linspace(-3.5, Y[index], 1000)

    unif = axs[0].fill_between(t_unif, RecFunction(0, 1)(t_unif), color="#1f77b4", alpha=0.5)
    dist = axs[1].fill_between(t_dist, distribution(t_dist), color="#1f77b4", alpha=0.5)

    return unif_dot, unif_dash, dist_dot, dist_dash, unif, dist


animation = FuncAnimation(fig, anim, frames=range(0, size), interval=500, repeat=True, blit=True)

# setting up fig
# x limits
index = 0
for inter in [interval_unif, interval]:
    axs[index].set_xlim(*inter)

    index += 1

# y limits
axs[0].set_ylim(0, 1.5)
axs[1].set_ylim(0, 1.5)

# titles
count = 0
for title in ["Uniform", "Normal"]:
    axs[count].set_title(title)

    count += 1

# x label y label
for i in range(2):
    axs[i].set_xlabel("$X$")
    axs[i].set_ylabel("$Fraction$")


axs[1].set_xlabel("$Y$")


plt.tight_layout()

fig.set_size_inches(6, 3.2)
plt.show()

animation.save('screenshots/anim-algo-custom-2.gif', writer='Pillow', fps=60)
