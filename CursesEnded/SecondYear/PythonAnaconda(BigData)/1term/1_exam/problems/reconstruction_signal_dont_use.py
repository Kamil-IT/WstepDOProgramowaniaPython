import numpy as np
from matplotlib import pyplot as plt
from scipy import signal, fft
import cvxpy as cvx

"""
    lab 3 working
"""

N = 1000
t = np.linspace(0, 10, N)
y = np.sin(t)

y_to_reconstruction = y[::int(N * 0.01)]

A = fft.idct(np.identity(N), norm='ortho', axis=0)
A = A[::int(N * 0.01)]

vx = cvx.Variable(N)
objective = cvx.Minimize(cvx.norm(vx, 1))
constraints = [A*vx == y_to_reconstruction]
prob = cvx.Problem(objective, constraints)
result = prob.solve(verbose=True)

x = np.array(vx.value)
x = np.squeeze(x)
f = fft.idct(x, norm='ortho', axis=0)







plt.subplot(111)
plt.plot(t, y, 'b-')
plt.plot(t, f, 'y-')
plt.show()