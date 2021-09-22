import numpy.random as rnd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# SVM lub SvN, drzewa decyzyjen DT

n = 500
x1 = 4 * rnd.rand(n) - 3
y1 = 4 * rnd.rand(n) - 3
z1 = 4 * rnd.rand(n) - 3

x2 = 4 * rnd.rand(n) + 10
y2 = 4 * rnd.rand(n)
z2 = 4 * rnd.rand(n)

x3 = 0
y3 = 0
z3 = 5

# Bierzemy 3 sąsiadów
fig = plt.figure()
ax = plt.axes(projection='3d')

ax.scatter(x1, y1, z1)
ax.scatter(x2, y2, z2)
ax.scatter(x3, y3, z3, 'y')

plt.show()



