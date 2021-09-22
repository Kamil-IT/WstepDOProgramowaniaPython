import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as opt

x = np.sort(np.random.uniform(0, 20, 30))
y_noised = x ** 2 + 0.1 * np.random.randn(len(x))
y_true = x ** 2


def model(params, x):
    a, b, c = params
    return a * x ** 2 + b * x + c


def l1_fit(x0, x, y):
    y_pred = model(x0, x)
    return np.sum(np.abs(y - y_pred))


def l2_fit(x0, x, y):
    y_pred = model(x0, x)
    return np.sum(np.abs((y - y_pred) ** 2))


xopt1 = opt.fmin(func=l1_fit, x0=[1, 1, 1], args=(x, y_noised))
xopt2 = opt.fmin(func=l2_fit, x0=[1, 1, 1], args=(x, y_noised))

y_est1 = xopt1[2] + xopt1[1] * x + xopt1[0] * x ** 2
y_est2 = xopt2[2] + xopt2[1] * x + xopt2[0] * x ** 2


err_l1 = np.abs(y_true - y_est1)
err_l2 = np.abs(y_true - y_est2)


fig, ax = plt.subplots(4, 1, figsize=(10, 8), constrained_layout=True)
ax[0].plot(x, y_noised, '*')
ax[1].plot(x, y_noised, '*')
ax[2].plot(x, y_noised, '*')
ax[0].plot(x, y_true, 'k', label='oryginal')
ax[0].set_title('original')
ax[1].plot(x, y_est1, 'g-', label='l1 norm')
ax[1].set_title('norm l1')
ax[2].plot(x, y_est2, 'r-', label='l2 norm')
ax[2].set_title('norm l2')
ax[3].plot(x, err_l1, label='error l1')
ax[3].plot(x, err_l2, label='error l2')
ax[3].set_title('error')
plt.legend()

plt.show()