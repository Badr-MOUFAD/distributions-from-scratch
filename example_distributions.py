import numpy as np
import matplotlib.pyplot as plt

from tools.step_functions import RecFunction


arr_figures = [
    [
        {
            "dist": lambda x: RecFunction(0, 1.)(x),
            "x_interval": [-0.25, 1.25],
            "title": "Uniform",
            "y_interval": [0., 1.4]
        },
        {
            "dist": lambda x: (2 * np.pi) ** (-1/2) * np.exp(-x ** 2 / 2) * RecFunction(-5., 5.)(x),
            "x_interval": [-5, 5],
            "title": "Normal",
            "y_interval": [0, 0.65]
        },
        {
            "dist": lambda x: np.exp(-x) * RecFunction(0., 7.)(x),
            "x_interval": [-0.5, 7.],
            "title": "Exponential",
            "y_interval": [0, 1.5]
        }
    ],
    [
        {
            "dist": lambda x: 3 * x ** 2 * RecFunction(0., 1.)(x),
            "x_interval": [-0.25, 1.25],
            "title": "$3 u^2 \mathbb{1}_{[0, 1]}$",
            "y_interval": [0, 4]
        },
{
            "dist": lambda x: 1 / 2 * np.sin(x) * RecFunction(0, np.pi)(x),
            "x_interval": [-0.5, np.pi*(1 + 0.1)],
            "title": r"$\frac{1}{2} sin(u) \mathbb{1}_{[0, \pi]}$",
            "y_interval": [0, 0.8]
        },
        {
            "dist": lambda x: 2 / np.pi * np.cos(x) ** 2 * RecFunction(0, np.pi)(x),
            "x_interval": [-0.5, np.pi*(1 + 0.1)],
            "title": r"$\frac{2}{\pi} cos(u)^2 \mathbb{1}_{[0, \pi]}$",
            "y_interval": [0, 0.8]
        },
    ]
]


#
nb_rows = 2
nb_cols = 3
nb_points = 1000

fig, axs = plt.subplots(2, 3)

# plot
for i in range(nb_rows):
    for j in range(nb_cols):
        ax = axs[i][j]
        current_figure = arr_figures[i][j]

        x = np.linspace(*current_figure["x_interval"], nb_points)
        ax.plot(x, current_figure["dist"](x))

        # layout
        ax.set_xlim(*current_figure["x_interval"])
        ax.set_ylim(*current_figure["y_interval"])

        ax.set_xlabel("$X$")
        ax.set_title(current_figure["title"])


plt.tight_layout()
plt.show()


# plt.savefig("screenshots/example_dist.png")
