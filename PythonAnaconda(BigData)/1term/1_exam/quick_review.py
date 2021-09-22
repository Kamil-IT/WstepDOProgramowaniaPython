import numpy as np
import scipy.optimize as opt
from matplotlib import pyplot as plt

N = 100

# Zamiast generować próbki w równych odległościach, proszę wygenerować próbki na zadanym odcinku w sposób losowy i na ich podstawie spróbować wygenerować sygnał sinusa.
t = np.sort(np.random.uniform(0, 10, N))
y = np.sin(t)

plt.subplot(111)
plt.plot(t, y, 'y-')
plt.plot(t, y, '*')

plt.show()

opt.fmin()

# W tym zadaniu będziemy estymować parametry pewnej prostej więc żeby zasymulować, że nie znamy dokładnie tej prostej to dodamy sobie do niej trochę liczb losowych

