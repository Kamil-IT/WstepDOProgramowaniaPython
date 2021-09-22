import numpy as np
import pandas as pd

vector = pd.Series([1, 2, 3, 4, 200, 400, 10, 25])
sin = pd.Series(np.sin(5 * np.pi))

print(vector.median())
print(vector.std())
print(vector.mean())
print(vector.min())
print(vector.max())
print(vector.interpolate())
