import numpy as np


def l1_fit(x0, x, y):
    return np.sum(np.abs(x0[0] * x + x0[1] - y))


def l2_fit(x0, x, y):
    return np.sum(np.power(x0[0] * x + x0[1] - y, 2))


def l0_fit(x0, x, y):
    return np.sum((np.abs(x0[0] * x + x0[1] - y)) > 0)


def l0_fit_norm(x0, x, y):
    return np.linalg.norm((x0[0] * x + x0[1] - y), ord=0)


def l1_fit_norm(x0, x, y):
    return np.linalg.norm((x0[0] * x + x0[1] - y), ord=1)


def l2_fit_norm(x0, x, y):
    return np.linalg.norm((x0[0] * x + x0[1] - y), ord=2)
