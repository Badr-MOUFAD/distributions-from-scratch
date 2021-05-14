import matplotlib.pyplot as plt

# init fig and axs
fig, axs = plt.subplots(1, 3)

uniform = axs[0].plot([], [])
dist_func = axs[1].plot([], [])
hist = axs[2].hist()