import numpy as np
import matplotlib.pyplot as plt

from tools.step_functions import RecFunction
from tools.class_distribution_function import DistributionFunction


arr_figures = [
    [
        {
            "dist": lambda x: RecFunction(0, 1.)(x),
            "x_interval": [-0.25, 1.25],
            "interval": [0, 1],
            "title": "Uniform",
            "y_interval": [0., 1.4]
        },
        {
            "dist": lambda x: (2 * np.pi) ** (-1/2) * np.exp(-x ** 2 / 2) * RecFunction(-3.5, 3.5)(x),
            "x_interval": [-3.5, 3.5],
            "interval": [-3.5, 3.5],
            "title": "Normal",
            "y_interval": [0, 0.65]
        },
        {
            "dist": lambda x: np.exp(-x) * RecFunction(0., 7.)(x),
            "x_interval": [-0.5, 7.],
            "interval": [0, 7],
            "title": "Exponential",
            "y_interval": [0, 1.5]
        }
    ],
    [
        {
            "dist": lambda x: 3 * x ** 2 * RecFunction(0., 1.)(x),
            "x_interval": [-0.25, 1.25],
            "interval": [0, 1],
            "title": "$3 u^2 \mathbb{1}_{[0, 1]}$",
            "y_interval": [0, 4]
        },
{
            "dist": lambda x: 1 / 2 * np.sin(x) * RecFunction(0, np.pi)(x),
            "x_interval": [-0.5, np.pi*(1 + 0.1)],
            "interval": [0, np.pi],
            "title": r"$\frac{1}{2} sin(u) \mathbb{1}_{[0, \pi]}$",
            "y_interval": [0, 0.8]
        },
        {
            "dist": lambda x: 2 / np.pi * np.cos(x) ** 2 * RecFunction(0, np.pi)(x),
            "x_interval": [-0.5, np.pi*(1 + 0.1)],
            "interval": [0, np.pi],
            "title": r"$\frac{2}{\pi} cos(u)^2 \mathbb{1}_{[0, \pi]}$",
            "y_interval": [0, 0.8]
        },
    ],
    [
        {
            "dist": lambda x: np.log(x) * RecFunction(1, 5)(x) / (5 * np.log(5) - 5 + 1) ,
            "x_interval": [0.9, 5.2],
            "interval": [1, 5],
            "title": r"$\frac{1}{5log(5)-4} log(u) \mathbb{1}_{[1, 5]}$",
            "y_interval": [0, 0.6]
        },
        {
            "dist": lambda x: (1 / 2) * ((1 - abs(x)) * RecFunction(-1, 1)(x) + (1 - abs(x - 2)) * RecFunction(1, 3)(x)),
            "x_interval": [-1.2, 3.2],
            "interval": [-1, 3],
            "title": r"$\frac{1}{2} ((1 - |x|) \mathbb{1}_{[-1, 1]} + (1 - |x - 2|) \mathbb{1}_{[1, 3]})$",
            "y_interval": [0, 0.6]
        },
        {
            "dist": lambda x: (x ** 2 + 1) / (2 / 3 + 2) * RecFunction(-1, 1)(x),# ((1 + np.sqrt((1 - x ** 2) * RecFunction(-1, 1)(x))) * RecFunction(-2, 2)(x)) / (2 + np.pi / 2),
            "x_interval": [-1.2, 1.2],
            "interval": [-1, 1],
            "title": r"$\frac{3}{8} (1 + x^2) \mathbb{1}_{[-1, 1]}$",
            "y_interval": [0, 0.8]
        },
    ]
]


# figure
nb_rows = 3
nb_cols = 3
nb_points = 1000

fig, axs = plt.subplots(nb_rows, nb_cols)

# histogram
size = 1000
# nb bins chosen using Sturge’s Rule
nb_bins = int(1 + 3.322 * np.log(size))


# plot
for i in range(nb_rows):
    for j in range(nb_cols):
        ax = axs[i][j]
        current_figure = arr_figures[i][j]

        # define dist
        dist = DistributionFunction(
            func=current_figure["dist"],
            interval=current_figure["interval"]
        )

        # plot dist
        x = np.linspace(*current_figure["x_interval"], nb_points)
        ax.plot(x, dist(x), color="#1f77b4", label="ideal")

        # plot histogram
        ax.hist(dist.generate_samples(size=size), density=True, lw=1, ec="#7f7f7f", alpha=0.5, bins=nb_bins, label="generated")

        # layout
        ax.set_xlim(*current_figure["x_interval"])
        ax.set_ylim(*current_figure["y_interval"])

        ax.set_xlabel("$X$")
        ax.set_title(current_figure["title"])


plt.tight_layout()
plt.show()


# plt.savefig("screenshots/example_dist.png")
