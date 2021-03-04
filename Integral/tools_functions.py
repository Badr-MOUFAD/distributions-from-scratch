import numpy as np

from plotly import graph_objects as go
import plotly.io as pio

pio.templates.default = "plotly_white"


def derivative(function, epsilon=10 ** -5):

    def df(x):
        return (function(x + epsilon) - function(x)) / epsilon

    return df


def linear_approximation(function, x0):

    def lin_approx(x):
        return derivative(function)(x0) * (x - x0) + function(x0)

    return lin_approx


def generate_steps(function, x_start, x_end, epsilon=10**-2):
    second_derivative = derivative(derivative(function))

    result = [x_start]
    x0 = result[0]
    x = result[0]

    while x <= x_end:
        # d_square = abs(second_derivative(x0))
        #
        # # this bound was chosen to insure a step
        # # of at most 10 ** -1
        # if d_square > 2 * 10**-5:
        #     x = x0 + np.sqrt(2 * epsilon / (abs(second_derivative(x0))))
        # else:
        #     x = x0 + np.sqrt(2 * epsilon)

        s = abs(derivative(function)(x0)) + abs(second_derivative(x0))
        if s > 2 * epsilon:
            x = x0 + np.sqrt(2 * epsilon / s)
        else:
            x = x0 + 1

        result.append(x)

        # to move forward,
        # in the next iteration x0 will play the role of x
        x0 = x

    # replace the last element with x_end
    return np.array(result[:len(result) - 1] + [x_end])


def intergral(a, b, function, epsilon=10**-3):
    x = generate_steps(function=function, x_start=a, x_end=b, epsilon=epsilon)
    sum_integral = 0

    for i in range(len(x) - 1):
        sum_integral += (function(x[i+1]) + function(x[i])) * (x[i+1] - x[i]) / 2

    return sum_integral


def generate_trapezoids(function, a, b, epsilon=10**-2):
    x = generate_steps(function=function, x_start=a, x_end=b, epsilon=epsilon)
    arr_graphs = []

    for i in range(len(x) - 1):
        arr_graphs.append(
            go.Scatter(x=[x[i], x[i], x[i+1], x[i+1]], y=[0, function(x[i]), function(x[i+1]), 0],
                       fill='tozeroy',
                       marker=dict(color="#636EFA"),
                       showlegend=False)
        )

    return arr_graphs


def map_element(distribution_function, a, b, probability, precision=10**-2):
    x = generate_steps(function=distribution_function, x_start=a, x_end=b, epsilon=precision)
    sum_integral = 0

    for i in range(len(x) - 1):
        sum_integral += (distribution_function(x[i + 1]) + distribution_function(x[i])) * (x[i + 1] - x[i]) / 2

        if sum_integral > probability:
            return (x[i+1] + x[i]) / 2

    return b


b = 5
a = 0
# t = np.linspace(a, b, 200)
# # f = lambda u: np.exp(-u**2 / 2) / np.sqrt(2 * np.pi)
# f = lambda u: np.exp(-u)
#
# #
# fig = go.Figure(data=[
#     go.Scatter(x=t, y=f(t), mode="lines", marker=dict(color="#EF553B")),
#     *generate_trapezoids(function=lambda u: f(u), a=a, b=b)
# ])
#
# fig.update_layout(
#     font=dict(size=10),
#     height=800,
#     width=800
# )
#
# fig.show()

prob = 0.5
print(map_element(distribution_function=lambda u: np.exp(-u), a=0, b=20, probability=prob))

lam = 1
print(- np.log(1 - prob) / lam)
