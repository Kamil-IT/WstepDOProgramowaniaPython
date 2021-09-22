import numpy as np
from matplotlib import pyplot as plt

N = 100
x = np.linspace(0, 1 / 8, N)
y = 3 * x * np.sin(x)

# a
tkeo = []
for i in range(1, N - 1):
    tkeo.append(y[i] ** 2 - y[i + 1] * y[i - 1])

print(tkeo)

# b
s = 0

sum_mian = 0
for e in range(N):
    sum_mian += (y[e] - sum(y) / len(y)) ** 3
mianownik = 1/N * sum_mian

sum_licz = 1/N
for e in range(N):
    sum_licz += (y[e] - sum(y) / len(y))


s = 1/(N-1) * sum_licz ** (3/2)
print(s)

# c


plt.subplot(211)
plt.plot(x[1:-1], tkeo, 'y-')

plt.subplot(212)
plt.plot(x, y, 'y-')

plt.show()