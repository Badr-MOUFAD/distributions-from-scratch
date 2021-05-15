import numpy as np

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from tools.class_distribution_function import DistributionFunction
from tools.step_functions import RecFunction


# sample size
size = 123

# nb bins chosen using Sturge’s Rule
nb_bins = int(1 + 3.322 * np.log(size))

# interval and hist ticks
interval = [-7, 7]
hist_ticks = np.linspace(*interval, nb_bins)


# create prob dist function
distribution = DistributionFunction(
    func=lambda u: (2 * np.pi) ** (-1/2) * np.exp(-u ** 2 / 2) * RecFunction(*interval)(u),
    interval=interval
)

# sample from a uniform [0, 1]
probs = np.random.rand(size)

# evolution of samples
evolution_samples = [[]]
count = 0
for prob in probs:
    y = distribution.map_dist_uniform(p0=prob)

    print(count)

    new_hist = list(evolution_samples[-1])
    new_hist.append(y)

    evolution_samples.append(new_hist)
    count += 1


# instantiate graph
fig, ax = plt.subplots(1, 1)

# histogram
_, _, bar_container = ax.hist([], hist_ticks, density=False, lw=1, ec="yellow", alpha=0.5, label="sampled")

# dis function
t = np.linspace(*interval, 100)
dist_func, = ax.plot([], [], label="ideal")

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
            rect.set_height(count)

        # update dist
        dist_func.set_data(t, distribution(t) * frame_number)

        # update nb samples
        nb_sample_text.set_text(text_template % frame_number)

        return bar_container.patches, dist_func

    return animate


anim = FuncAnimation(fig, prepare_animation(bar_container), frames=size, interval=1, repeat=True)

ax.set_xlim(*interval)
ax.set_ylim(-0.5, 0.5 * size)

# axis
ax.set_xlabel("$X$")
ax.set_ylabel("Number")

#
ax.set_title("Normal distribution (ideal vs. sampled)")
ax.legend()
plt.show()

# anim.save('screenshots/test_normal_6.gif', writer='Pillow', fps=60)
