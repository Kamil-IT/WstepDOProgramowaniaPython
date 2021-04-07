import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft, ifft


def hamming(matrix):
    N = len(matrix)
    for n in range(1, N + 1):
        x[n - 1] = 1 / 2 * (1 - np.cos((2 * np.pi * n) / (N - 1)))


# Quantity of sample points
N = 500
# Distance between
T = 1.0 / 800.0

# Creating signal
x = np.linspace(0.0, N * T, N)
y = np.sin(50.0 * 2.0 * np.pi * x) + 0.5 * np.sin(80.0 * 2.0 * np.pi * x)

# Window time hamming
hamming(y)

# fft
yf = fft(y)
xf = np.linspace(0.0, 1.0 / (2.0 * T), int(N / 2))

# Delete frequency
for i in range(len(yf)):
    if yf[i] > 0.6:
        yf[i] = 0

y = ifft(yf)














fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()
