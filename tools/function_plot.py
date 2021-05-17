
def update_dot_dash_plots(dot_plot, dash_plot, new_x, new_y):
    length = 50

    x_dash = [new_x for i in range(length)]
    y_dash = [new_y / length * i for i in range(length)]

    dot_plot.set_data([new_x], [new_y])
    dash_plot.set_data(x_dash, y_dash)

    return dot_plot, dash_plot

