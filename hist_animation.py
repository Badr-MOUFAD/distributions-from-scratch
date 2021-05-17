import numpy as np

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from tools.class_distribution_function import DistributionFunction
from tools.step_functions import RecFunction


# sample size
size = 1000

# nb bins chosen using Sturge’s Rule
nb_bins = int(1 + 3.322 * np.log(size))

# interval and hist ticks
interval = [-5, 5]
hist_ticks = np.linspace(*interval, nb_bins)
dx = hist_ticks[1] - hist_ticks[0]

# create prob dist function
distribution = DistributionFunction(
    func=lambda u: (2*np.pi) ** (-1 / 2) * np.exp(-u ** 2 / 2) * RecFunction(*interval)(u),
    interval=interval
)

# sample from a uniform [0, 1]
probs = np.random.rand(size)

# evolution of samples
evolution_samples = [[]]

for i in range(size):
    prob = probs[i]
    y = distribution.map_dist_uniform(p0=prob)

    print(i)

    new_hist = list(evolution_samples[-1])
    new_hist.append(y)

    evolution_samples.append(new_hist)

# instantiate graph
fig, ax = plt.subplots(1, 1)

# histogram
_, _, bar_container = ax.hist([], hist_ticks, density=False, lw=1, ec="yellow", alpha=0.5, label="sampled")

# dis function
t = np.linspace(*interval, 100)
dist_func, = ax.plot(t, distribution(t), label="ideal")

# text
# to display elapsed time
text_template = 'nb samples = %.0f'
nb_sample_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)


# function to create anim function
def prepare_animation(bar_container):

    def animate(frame_number):
        # actual stage
        actual_stage = evolution_samples[frame_number]

        # update length of bars
        n, _ = np.histogram(actual_stage, hist_ticks)

        for count, rect in zip(n, bar_container.patches):
            rect.set_height(count / (frame_number * dx))

        # update dist
        # dist_func.set_data(t, distribution(t))

        # update nb samples
        nb_sample_text.set_text(text_template % frame_number)

        return bar_container.patches, dist_func

    return animate


anim = FuncAnimation(fig, prepare_animation(bar_container), frames=range(1, size, 10), interval=1, repeat=True)

ax.set_xlim(*interval)
ax.set_ylim(-0.1, 1)

# axis
ax.set_xlabel("$X$")
ax.set_ylabel("Frequency")

#
ax.set_title("Normal distribution (ideal vs. sampled)")
ax.legend()
plt.show()

# anim.save('test_screenshots/test_normal_7.gif', writer='Pillow', fps=60)
