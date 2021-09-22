import numpy as np
from math import cos
from scipy.optimize import fmin



def func(x):
    return (cos(3*np.pi * x))/x



x = np.sort(np.random.uniform(0.1, 1.1, 10))
minimum = fmin(func, 1)
print(minimum[0])