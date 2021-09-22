import matplotlib.pyplot as plt
import numpy as np


def fft(x):
    x_complex = [np.complex(val, 0) for val in x]
    fft_rec(x_complex)
    return x_complex


def fft_rec(x):
    elements = len(x)

    if elements <= 1:
        return

    even = np.array(x[0:elements:2])
    odd = np.array(x[1:elements:2])

    fft_rec(even)
    fft_rec(odd)

    for k in range(0, int(elements / 2)):
        t = np.exp(np.complex(0, -2 * np.pi * k / elements)) * odd[k]
        x[k] = even[k] + t
        x[int(elements / 2 + k)] = even[k] - t


# Check fft
N = 128
T = 1.0 / 800.0

x = np.linspace(0.0, N * T, N)
y = np.sin(50.0 * 2.0 * np.pi * x) + 0.5 * np.sin(80.0 * 2.0 * np.pi * x)

yf = fft(y)
xf = np.linspace(0.0, 1.0 / (2.0 * T), int(N / 2))

fig, ax = plt.subplots()
ax.plot(xf, 2.0 / N * np.abs(yf[:N // 2]))
plt.show()

# Check for y(t) = 5sin(t) + 3sin(2t) + 5sin(5t)
t = np.arange(0, 4 * np.pi, 0.1)
function = 5 * np.sin(t) + 3 * np.sin(2 * t) + 5 * np.sin(5 * t)

fft_my = fft(function)
print(fft_my)

# fft_np = np.fft.fft(function)
# print(fft_np)
