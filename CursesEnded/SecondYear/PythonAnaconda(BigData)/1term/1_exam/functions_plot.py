import numpy as np
from matplotlib import pyplot as plt
from scipy import signal

"""
    Generating signals (sampling)
"""

N = 1000
# sampling(losowanie próbek) N times
t = np.sort(np.random.uniform(0, 10, N))
# sampling(losowanie próbek) N times on same distance
t_same_distance = np.linspace(0, 10, N)
# random sampling and indexing
indexes = np.random.choice(N, 100, replace=False)
indexes.quick_sort()
t_different_distance = t[indexes]
y_sin_different_distance = np.sin(np.pi * t)[indexes]

# Sin from samples
sin = np.sin(5 * np.pi * t)

# Sawtooth(Piłokształtny) form samples
sawtooth = signal.sawtooth(np.pi * 5 * t)

# Square-wave(prostokątna fala lub przebiek prostokątny)
square = signal.square(np.pi * 5 * t)


"""
    Plotting signals
"""

# plt.subplot(number_plots 1 current_plot)
# Normal plots
plt.subplot(611)
plt.plot(t, sin, 'y-')

plt.subplot(612)
plt.plot(t, sawtooth, 'y-')

plt.subplot(613)
plt.plot(t, square, 'y-')

# Multiple plots on same chart
plt.subplot(614)
plt.plot(t, sin, 'y-')
plt.plot(t, sawtooth, 'y-')
plt.plot(t, square, 'y-')


# Plot semilogy(logarytmiczny)
plt.subplot(615)
plt.semilogy(t, sin, 'y-')

# Plot points
plt.subplot(616)
plt.plot(t, sin, '*')

plt.show()
