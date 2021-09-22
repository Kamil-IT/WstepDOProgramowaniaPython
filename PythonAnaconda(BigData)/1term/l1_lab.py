from numpy import linspace, cos, pi, ceil, floor, arange, sin, sinc
from pylab import plot, show, axis, subplot, errorbar

f = 1.0
fs = 5.0

t = linspace(-1, 1, 100)
ts = arange(-1, 1 + 1 / fs, 1 / fs)
num_coeffs = len(ts)
sm = 0

# reconstruct

for k in range(-num_coeffs, num_coeffs):
    sm += sin(2 * pi * (k / fs)) * sinc(k - fs * t)

# plot
plot(t, sm, '--', t, sin(2 * pi * t), ts, sin(ts), 'o')
# plot(t, (sm - sin(2 * pi * t)))
show()