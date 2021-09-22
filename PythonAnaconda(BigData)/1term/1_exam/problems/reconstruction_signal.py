# sin(3x)
import cvxpy as cvx
import numpy as np
from matplotlib import pyplot as plt
from scipy import fft

# Create function
N = 1000
t = np.linspace(0, 10, N)
y = np.sin(np.pi * t) * 3

# Get random indexes
indexes = np.random.choice(N, 100, replace=False)
indexes.quick_sort()
t_to_reconstruction = t[indexes]
y_to_reconstruction = y[indexes]

# Do fft transform
A = fft.idct(np.identity(N), norm='ortho', axis=0)
A = A[indexes]

# Solve problem
vx = cvx.Variable(N)
objective = cvx.Minimize(cvx.norm(vx, 1))
constraints = [A * vx == y_to_reconstruction]
prob = cvx.Problem(objective, constraints)
result = prob.solve(verbose=True)

# Clean up values and do fft transform
reconstructed_function_norm_1 = fft.idct(np.squeeze(np.array(vx.value)), norm='ortho', axis=0)


# Solve problem
vx = cvx.Variable(N)
objective = cvx.Minimize(cvx.norm(vx, 2))
constraints = [A * vx == y_to_reconstruction]
prob = cvx.Problem(objective, constraints)
result = prob.solve(verbose=True)

reconstructed_function_norm_2 = fft.idct(np.squeeze(np.array(vx.value)), norm='ortho', axis=0)


plt.subplot(211)
plt.plot(t, reconstructed_function_norm_1)
plt.plot(t, y, 'y')

plt.subplot(212)
plt.plot(t, reconstructed_function_norm_2)
plt.plot(t, y, 'y')

plt.show()
