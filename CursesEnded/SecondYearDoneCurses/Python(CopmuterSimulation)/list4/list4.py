import numpy as np
import matplotlib.pyplot as plt
from random import uniform

x_inside = []
y_inside = []
x_outside = []
y_outside = []

points_inside = 0
points_outside = 0
total_points = 10 ** 4


def is_in_fig(x, y):
    # First left down circle
    if not ((x - 1) ** 2 + (y - 2) ** 2 <= 1 or y > 2 or x > 1):
        return False
    # First triangle down
    if (np.absolute(-x + 2) > y) and 1 < x < 3:
        return False
    # First straight line
    if 3 < x < 5 and y < 1:
        return False
    # Second right down circle
    if not ((x - 5) ** 2 + (y - 2) ** 2 <= 1 or y > 2 or x < 5):
        return False
    # Third right up circle
    if not ((x - 1) ** 2 + (y - 4) ** 2 <= 1 or y < 4 or x > 1):
        return False
    # Fourth right down circle
    if not ((x - 5) ** 2 + (y - 4) ** 2 <= 1 or y < 4 or x < 5):
        return False
    # Second triangle up
    if (-np.absolute(-x + 3) + 7 < y) and 1 < x < 5:
        return False
    return True


for _ in range(total_points):
    x = uniform(0, 6)
    y = uniform(0, 7)
    if is_in_fig(x, y):
        points_inside += 1
        x_inside.append(x)
        y_inside.append(y)
    else:
        points_outside += 1
        x_outside.append(x)
        y_outside.append(y)

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.scatter(x_inside, y_inside, color='g', s=1)
ax.scatter(x_outside, y_outside, color='r', s=1, linewidth=2.0)
fig.show()

surface_area = 6*7
surface_fig = surface_area*(points_inside/(points_inside+points_outside))
print("Surface fig: " + str(surface_fig))
