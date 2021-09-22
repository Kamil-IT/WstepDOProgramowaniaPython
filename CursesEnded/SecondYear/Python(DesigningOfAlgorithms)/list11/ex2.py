import matplotlib.pyplot as plt
import numpy as np
import scipy
from numpy import dot

x = [1, 2, 3]
y = [1, 2.5, 1]
point = [-1, -1]

pi = scipy.pi
dot = scipy.dot
sin = scipy.sin
cos = scipy.cos
ar = scipy.array


def rotate(pts, cnt, ang=pi / 4):
    return dot(pts - cnt, ar([[cos(ang), sin(ang)], [-sin(ang), cos(ang)]])) + cnt


def area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1)
                + x3 * (y1 - y2)) / 2.0)


def is_inside(x1, y1, x2, y2, x3, y3, x, y):
    A = area(x1, y1, x2, y2, x3, y3)
    A1 = area(x, y, x2, y2, x3, y3)
    A2 = area(x1, y1, x, y, x3, y3)
    A3 = area(x1, y1, x2, y2, x, y)
    if (A == A1 + A2 + A3):
        return True
    else:
        return False


while True:
    rotated = rotate(ar([[x[i], y[i]] for i in range(len(x))]), ar([-1, -1]), 0.5)
    x = [i[0] for i in rotated]
    y = [i[1] for i in rotated]

    plt.cla()
    plt.plot(point[0], point[1], 'ro')
    if is_inside(x[0], y[0], x[1], y[1], x[2], y[2], 0, 2):
        plt.plot(0, 2, 'ro', color='g')
    else:
        plt.plot(0, 2, 'ro')
    plt.xlim([-6, 5])
    plt.ylim([-7, 7])
    plt.tripcolor(x, y, facecolors=np.asarray([10]))
    plt.draw()
    plt.pause(1)
