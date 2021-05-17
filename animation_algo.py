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
interval = [-3.5, 3.5]
hist_ticks_dist = np.linspace(*interval, nb_bins)
dx = hist_ticks_dist[1] - hist_ticks_dist[0]

interval_unif = [0, 1]
hist_ticks_unif = np.linspace(*interval_unif, nb_bins)
dx_unif = hist_ticks_unif[1] - hist_ticks_unif[0]

# create prob dist function
distribution = DistributionFunction(
    func=lambda u: (2*np.pi) ** (-1 / 2) * np.exp(-u ** 2 / 2) * RecFunction(*interval)(u),
    interval=interval
)

# sample from a uniform [0, 1]
probs = np.random.rand(size)

# evolution of samples
evolution_samples_dist = [[]]
evolution_samples_unif = [[]]

for i in range(size):
    prob = probs[i]
    y = distribution.map_dist_uniform(p0=prob)

    print(i)

    new_hist = list(evolution_samples_dist[-1])
    new_hist_unif = list(evolution_samples_unif[-1])

    new_hist.append(y)
    new_hist_unif.append(prob)

    evolution_samples_dist.append(new_hist)
    evolution_samples_unif.append(new_hist_unif)

# instantiate graph
fig, axs = plt.subplots(1, 2)

# histogram
_, _, bar_container_unif = axs[0].hist([], hist_ticks_unif, lw=1, ec="yellow", alpha=0.5, label="sampled")
_, _, bar_container_dist = axs[1].hist([], hist_ticks_dist, lw=1, ec="yellow", alpha=0.5, label="sampled")


# dis function
t_unif = np.linspace(-0.5, 1.5, 100)
unif_dist = axs[0].plot(t_unif, RecFunction(0, 1)(t_unif), label="ideal")

t_dist = np.linspace(*interval, 100)
dist_func, = axs[1].plot(t_dist, distribution(t_dist), label="ideal")

# text
# to display elapsed time
text_template = 'nb samples = %.0f'
nb_sample_text = axs[0].text(0.45, 0.79, '', transform=axs[0].transAxes)
nb_sample_text_unif = axs[1].text(0.45, 0.79, '', transform=axs[1].transAxes)


# function to create anim function
def prepare_animation(*args):
    bar_container_unif, bar_container_dist = args

    def animate(frame_number):
        # dist
        # actual stage
        actual_stage = evolution_samples_dist[frame_number]

        # update length of bars dist
        n, _ = np.histogram(actual_stage, hist_ticks_dist)

        for count, rect in zip(n, bar_container_dist.patches):
            rect.set_height(count / (frame_number * dx))

        # unif
        # actual stage
        actual_stage = evolution_samples_unif[frame_number]

        # update length of bars dist
        n, _ = np.histogram(actual_stage, hist_ticks_unif)

        for count, rect in zip(n, bar_container_unif.patches):
            rect.set_height(count / (frame_number * dx_unif))

        # update nb samples
        nb_sample_text.set_text(text_template % frame_number)
        nb_sample_text_unif.set_text(text_template % frame_number)

        return bar_container_unif.patches, bar_container_dist.patches

    return animate


anim = FuncAnimation(fig, prepare_animation(bar_container_unif, bar_container_dist), frames=range(1, size, 10), interval=1, repeat=True)

for i in range(2):
    # axis
    axs[i].set_xlabel("$X$")
    axs[i].set_ylabel("Frequency")

    axs[i].legend()


axs[0].set_ylim(-0.1, 2)
axs[1].set_ylim(-0.1, 1)

#
axs[0].set_xlim(-0.5, 1.5)
axs[1].set_xlim(*interval)

axs[0].set_title("Uniform")
axs[1].set_title("Normal distribution")

plt.tight_layout()
plt.show()

anim.save('test_screenshots/anim_algo.gif', writer='Pillow', fps=60)
