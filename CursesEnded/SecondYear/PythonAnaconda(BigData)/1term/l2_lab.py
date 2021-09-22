import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

x = np.sort(np.random.uniform(0, 10, 15))
y = 3 + 0.25 * x + 0.5 * np.random.randn(len(x))
yy = 3 + 0.25 * x


def l2_fit(x0, x, y):
    return np.sum(np.power(x0[0] * x + x0[1] - y, 2))


def l1_fit(x0, x, y):
    return np.sum(np.abs(x0[0] * x + x0[1] - y))


def l0_fit(x0, x, y): #norma l 0
    sum_ = 0
    for i in y:
        if i != 0:
            sum_ += 1
    return sum_
    # or
    # np.linalg.normy(y, ord=0)


xopt2 = opt.fmin(func=l2_fit, x0=[1, 1], args=(x, y))
xopt1 = opt.fmin(func=l1_fit, x0=[1, 1], args=(x, y))

y_est1 = xopt1[1] + xopt1[0] * x
y_est2 = xopt2[1] + xopt2[0] * x

plt.subplot(211)
plt.plot(x, y, '*')
plt.plot(x, y_est1, 'g-', label='l1 norm')
plt.plot(x, y_est2, 'r-', label='l2 norm')
plt.plot(x, yy, 'b-', label='prosta')
plt.legend()

y2 = y.copy()
# y2[3] += 10
# y2[13] -= 5

xopt22 = opt.fmin(func=l2_fit, x0=[1, 1], args=(x, y2))
xopt11 = opt.fmin(func=l1_fit, x0=[1, 1], args=(x, y2))

y_est11 = xopt11[1] + xopt11[0] * x
y_est22 = xopt22[1] + xopt22[0] * x

plt.subplot(212)
plt.plot(x, yy, 'b--', label='prosta')
plt.plot(x, y_est11, 'g--', label='l1 norm')
plt.plot(x, y_est22, 'r--', label='l2 norm')
plt.ylim([-5, 16])
plt.legend()
plt.show()

y3 = y.copy()

xopt222 = opt.fmin(func=l2_fit, x0=[1, 1], args=(x, y2))
xopt111 = opt.fmin(func=l1_fit, x0=[1, 1], args=(x, y2))
xopt000 = opt.fmin(func=l0_fit, x0=[1, 1], args=(x, y2))

y_est111 = xopt111[1] + xopt111[0] * x
y_est222 = xopt222[1] + xopt222[0] * x
y_est000 = xopt000[1] + xopt000[0] * x

plt.subplot(212)
plt.plot(x, yy, 'y--', label='prosta')
plt.plot(x, y_est111, 'g--', label='l1 norm')
plt.plot(x, y_est222, 'r--', label='l2 norm')
plt.plot(x, y_est000, 'b--', label='l0 norm')

plt.plot(x, abs(yy - y_est000), 'b--', label='l0 error')
plt.plot(x, abs(yy - y_est111), 'g--', label='l1 error')
plt.plot(x, abs(yy - y_est222), 'r--', label='l2 error')

plt.ylim([-5, 16])
plt.legend()
plt.show()
