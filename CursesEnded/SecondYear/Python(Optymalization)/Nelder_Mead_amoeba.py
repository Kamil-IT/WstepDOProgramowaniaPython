from scipy.optimize import rosen
import random as rd
import numpy as np
import sys


def func(A):
    s = 0
    for i in range(n * n):
        if (i >= n):  # top boundary
            s = s - np.cos(abs(A[i] - A[i - n])) + 1
        if (i < n * n - n):  # bottom boundary
            s = s - np.cos(abs(A[i] - A[i + n])) + 1
        if (i % n != 0):  # left boundary
            s = s - np.cos(abs(A[i] - A[i - 1])) + 1
        if (i % n != (n - 1)):  # right boundary
            s = s - np.cos(abs(A[i] - A[i + 1])) + 1
    return s


def create_random_table(n):
    '''
    creating a starting point of the system:
    n*n-dimentional table with random values
    values range: [0, 2*pi)
    '''
    tab = []
    for i in range(n * n):
        tab.append(rd.uniform(0, 2 * np.pi))
    return tab


def create_ordered_table(n):
    '''
    creating a starting point of the system:
    n*n-dimentional table with ordered values
    values range: [0, 2*pi)
    '''
    tab = []
    for i in range(n * n):
        tab.append(0 + i % (2 * np.pi))
    return tab


def get_psum(p, ndim, mpts):
    '''
    counting partial sum
    '''
    psum = []
    for j in range(ndim):
        sum = 0.0
        for i in range(mpts):
            sum += p[i][j]
        psum.append(sum)
    return psum


def amotry(p, y, psum, ihi, ndim, fac):
    '''
    extrapolation by a factor fac through the face of the simplex across from the high point
    replacing the high point if the new point is better
    '''
    ptry = []
    fac1 = (1.0 - fac) / ndim
    fac2 = fac1 - fac
    for j in range(ndim):
        ptry.append(psum[j] * fac1 - p[ihi][j] * fac2)
    ytry = func(ptry)
    if (ytry < y[ihi]):
        y[ihi] = ytry
        for j in range(ndim):
            psum[j] += ptry[j] - p[ihi][j]
            p[ihi][j] = ptry[j]
    return ytry


n = 10  # dimention of side of pseudo-square table
delta = 1  # displacement
ftol = 1e-6  # fractional convergence tolerance
nmax = 10000000  # maximum allowed number of function evaluations
tiny = 1e-7  # tiny value preventing from dividing by 0

# creating point table as starting point in the system
point = create_random_table(n)
ndim = len(point)

# creating delta values table
delta_tab = []
for i in range(ndim):
    delta_tab.append(delta)

# adding delta values to the point table with extended dimention as p simplex
p = []
for i in range(ndim + 1):
    k = []
    for j in range(ndim):
        k.append(point[j])
    p.append(k)
    if (i != 0):
        p[i][i - 1] += delta_tab[i - 1]

# getting y table of solutions
y = []
mpts = len(p)  # number of rows
for i in range(mpts):
    x = []
    for j in range(ndim):
        x.append(p[i][j])
    y.append(func(x))

# parameters for iterating
nfunc = 0
psum = get_psum(p, ndim, mpts)
it = 0

# algorithm working in the iterative mode
while True:
    it += 1

    ilo = 0
    if y[0] > y[1]:
        inhi = 1
        ihi = 0
    else:
        inhi = 0
        ihi = 1

    for i in range(mpts):
        if y[i] <= y[ilo]:
            ilo = i
        if y[i] > y[ihi]:
            inhi = ihi
            ihi = i
        elif y[i] > y[inhi] and i != ihi:
            inhi = i

    rtol = 2.0 * abs(y[ihi] - y[ilo]) / (abs(y[ihi]) + abs(y[ilo]) + tiny)

    if (rtol < ftol):
        print("Optimisation succeeded")
        return y, p, ndim, ilo

    nfunc += 2

    ytry = amotry(p, y, psum, ihi, ndim, -1.0)  # simplex
    if ytry <= y[ilo]:
        ytry = amotry(p, y, psum, ihi, ndim, 2.0)  # simplex extrapolation
    elif ytry >= y[inhi]:
        ysave = y[ihi]
        ytry = amotry(p, y, psum, ihi, ndim, 0.5)  # simplex contraction
        if ytry >= ysave:
            for i in range(mpts):
                if i != ilo:
                    for j in range(ndim):
                        p[i][j] = psum[j] = 0.5 * (p[i][j] + p[ilo][j])
                    y[i] = func(psum)
            nfunc += ndim;
            psum = get_psum(p, ndim, mpts)
    else:
        nfunc = nfunc - 1
