import numpy as np
import time



def aeuc(x, y):
    if (y == 0):
        return x
    return aeuc(y, x % y)


time_aeuc = []
time_time_secondaeuc = []
x = np.array([2, 5, 4, 3, 3, 1]) * np.array([2, 4, 6, 8, 2, 7])
y_max = 10

for i in range(y_max):

    start = time.time()
    for index in range(len(x) // 2):
        aeuc(index*2, index*2 + 1)
    end = time.time()
    time_aeuc.append(end - start)

    start = time.time()
    for index in range(len(x) // 2):
        secondaeuc(index * 2, index*2 + 1)
    end = time.time()
    time_secondaeuc.append(end - start)


fig, ax = plt.subplots(1)
ax.plot(x, time_aeuc, x, time_secondaeuc)
plt.show()

