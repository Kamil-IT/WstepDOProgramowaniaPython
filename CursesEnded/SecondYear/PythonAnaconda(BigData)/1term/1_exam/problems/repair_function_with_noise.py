import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as opt

N = 15
x = np.sort(np.random.uniform(0, 10, N))
y = x ** 2
y_dump = x ** 2 + 10 * np.random.randn(len(x))


# Repair dump function
def l1_fit(x0, x, y):
    return np.sum(np.abs(x0[0] * np.array(x) + x0[1] - y))


def l2_fit(x0, x, y):
    return np.sum(np.power(x0[0] * np.array(x) + x0[1] - y, 2))


def l0_fit(x0, x, y):
    return np.sum((np.abs(x0[0] * np.array(x) + x0[1] - y)) > 0)


def get_sqrt_val(x):
    result = []
    for x_val in x:
        if x_val >= 0:
            result.append(np.sqrt(x_val))
        else:
            result.append(-1 * np.sqrt(-1 * x_val))
    return np.array(result)


# Estimation function parameters

y_dump = get_sqrt_val(y_dump)

# L0
y_opti_l0 = opt.fmin(l0_fit, [1, 1], (x, y_dump))
y_rapair_l0 = (y_opti_l0[1] + np.array(x) * y_opti_l0[0]) ** 2
# L1
y_opti_l1 = opt.fmin(l1_fit, [1, 1], (x, y_dump))
y_rapair_l1 = (y_opti_l1[1] + np.array(x) * y_opti_l1[0]) ** 2
# L2
y_opti_l2 = opt.fmin(l2_fit, [1, 1], (x, y_dump))
y_rapair_l2 = (y_opti_l2[1] + np.array(x) * y_opti_l2[0]) ** 2

plt.subplot(311)
plt.plot(x, y, 'b')
plt.plot(x, y_dump ** 2, '*')
plt.plot(x, y_rapair_l0, 'g')

plt.subplot(312)
plt.plot(x, y, 'b')
plt.plot(x, y_dump ** 2, '*')
plt.plot(x, y_rapair_l1, 'g')

plt.subplot(313)
plt.plot(x, y, 'b')
plt.plot(x, y_dump ** 2, '*')
plt.plot(x, y_rapair_l2, 'g')
plt.show()
