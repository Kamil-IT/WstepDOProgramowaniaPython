import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

N = 1000
t = np.sort(np.random.uniform(0, 10, N))
sin = np.sin(5 * np.pi * t)
sawtooth = signal.sawtooth(np.pi * 5 * t)
square = signal.square(np.pi * 5 * t)

sin_frequencies, sin_power = signal.periodogram(sin)
sawtooth_frequencies, sawtooth_power = signal.periodogram(sawtooth)
square_frequencies, square_power = signal.periodogram(square)

sin_frequencies_welch, sin_power_welch = signal.welch(sin)
sawtooth_frequencies_welch, sawtooth_power_welch = signal.welch(sawtooth)
square_frequencies_welch, square_power_welch = signal.welch(square)


# plt.subplot(311)
# plt.semilogy(t, sin, 'y-')
#
# plt.subplot(312)
# plt.semilogy(t, sawtooth, 'y-')
#
# plt.subplot(313)
# plt.semilogy(t, square, 'y-')


plt.subplot(611)
plt.semilogy(sin_frequencies, sin_power, 'y-')

plt.subplot(612)
plt.semilogy(sawtooth_frequencies, sawtooth_power, 'y-')

plt.subplot(613)
plt.semilogy(square_frequencies, square_power, 'y-')


plt.subplot(614)
plt.semilogy(sin_frequencies_welch, sin_power_welch, 'y-')

plt.subplot(615)
plt.semilogy(sawtooth_frequencies_welch, sawtooth_power_welch, 'y-')

plt.subplot(616)
plt.semilogy(square_frequencies_welch, square_power_welch, 'y-')

plt.show()
