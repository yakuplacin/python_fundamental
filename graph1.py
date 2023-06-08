
# importing the required module
import matplotlib.pyplot as plt
import numpy as np
# x axis values


def f(x):
    return 1 / (100-x)


x = np.linspace(1, 100, 100)
y = f(x)
# plotting the points
plt.plot(x, y)

# naming the x axis
plt.xlabel('Parallelization')
# naming the y axis
plt.ylabel('Speed-up %')

# giving a title to my graph
plt.title('The speed-up graph')

# function to show the plot
plt.show()
