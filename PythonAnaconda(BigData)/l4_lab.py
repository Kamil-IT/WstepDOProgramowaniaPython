import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

N = 1000
t = np.sort(np.random.uniform(0, 10, N))
x = np.sin(5 * np.pi * t)

xx = signal.sawtooth(np.pi * 5 * t)

xxx = signal.square(np.pi * 5 * t)

m = 100

sumaxx = []
suma2 = []
suma3 = []
for r in range(m - 1):
    cc = 0
    ccx = 0
    ccs = 0
    for i in range(N - r):
        cc += (1 / (N - r)) * x[i] * x[i - r]
        ccx += (1 / (N - r)) * xx[i] * xx[i - r]
        ccs += (1 / (N - r)) * xxx[i] * xxx[i - r]
    suma2.append(cc)
    suma3.append(ccs)
    sumaxx.append(ccx)

z = []

for i in range(m - 1):
    z.append(i + 1)


def corelate(array):
    a = []
    aa = signal.correlate(array, array)
    for i in range(m - 2, 2 * (m - 1) - 1):
        a.append(aa[i])
    return a


plt.subplot(911)
plt.plot(t, x, 'y-')

plt.subplot(912)
plt.plot(z, suma2, 'g-')

plt.subplot(913)
plt.plot(z, corelate(suma2), 'r-')

plt.subplot(914)
plt.plot(t, xx, 'y-')

plt.subplot(915)
plt.plot(z, sumaxx, 'g-')

plt.subplot(916)
plt.plot(z, corelate(sumaxx), 'r-')

plt.subplot(917)
plt.plot(t, xxx, 'y-')

plt.subplot(918)
plt.plot(z, suma3, 'g-')

plt.subplot(919)
plt.plot(z, corelate(suma3), 'r-')

plt.show()