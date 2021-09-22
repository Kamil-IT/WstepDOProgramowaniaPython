import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack as fft
import cvxpy as cvx

N = 5000
t = np.linspace(0, 1 / 8, N)
y = np.sin(100 * np.pi * t) + np.sin(333 * np.pi * t)

plt.figure(figsize=(10, 15))
plt.subplot(311)
plt.plot(t, y)

m = 500  # 10% sample

pr = np.random.choice(N, m, replace=False)
# losowanie probek
pr.sort()
# sortowanie do wyswietlania
t2 = t[pr]
b = y[pr]

plt.subplot(312)
plt.plot(t2, b)
plt.plot(t2, b, 'r*')

A = fft.idct(np.identity(N), norm='ortho', axis=0)
A = A[pr]

vx = cvx.Variable(N)

objective = cvx.Minimize(cvx.norm(vx, 1))
constraints = [A * vx == b]
prob = cvx.Problem(objective, constraints)
result = prob.solve(verbose=True)
x = np.array(vx.value)
x = np.squeeze(x)
f = fft.idct(x, norm='ortho', axis=0)
plt.subplot(313)
plt.plot(f)

objective2 = cvx.Minimize(cvx.norm(vx, 2))
prob2 = cvx.Problem(objective2, constraints)
result2 = prob2.solve(verbose=True)
x = np.array(vx.value)
x = np.squeeze(x)
f = fft.idct(x, norm='ortho', axis=0)
plt.plot(f, 'g')

plt.show()
