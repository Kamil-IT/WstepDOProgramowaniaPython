import numpy as np


def normalize(to_normalized):
    normalized = np.linalg.norm(to_normalized)
    if normalized == 0:
        return to_normalized
    return to_normalized / normalized


float_array = [2.2, 5.6, 4.3, 3.0, 0.5]

for number in normalize(float_array):
    print(round(number, 3))
