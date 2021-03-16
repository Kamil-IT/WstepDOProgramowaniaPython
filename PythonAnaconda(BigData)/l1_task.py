from numpy import linspace, cos, pi, ceil, floor, arange, sin, sinc, array
from pylab import plot, show, axis, subplot, errorbar
from random import randint, uniform

f = 1.0
fs = 3

t = linspace(-1, 1, randint(10, 1200))
y = sin(t)
ts = array([uniform(-1, 1) for i in range(fs + fs + 1)])
ts.sort()
num_coeffs = len(ts)
sm = 0

# reconstruct

for k in range(-num_coeffs, num_coeffs):
    sm += sin(2 * pi * (k / fs)) * sinc(k - fs * t)

# plot
plot(t, sm, '--', t, sin(2 * pi * t), ts, sin(2 * pi * ts), 'o')
# plot(t, abs(sm - sin(2 * pi * t)))
# plot(t, sm, '--')
show()
