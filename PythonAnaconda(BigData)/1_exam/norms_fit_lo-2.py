import numpy as np


def l2_fit(x0, x, y):
    return np.sum(np.power(x0[0] * x + x0[1] - y, 2))


def l1_fit(x0, x, y):
    return np.sum(np.abs(x0[0] * x + x0[1] - y))


def l0_fit(x0, x, y):
    sum_ = 0
    for i in y:
        if i != 0:
            sum_ += 1
    return sum_
