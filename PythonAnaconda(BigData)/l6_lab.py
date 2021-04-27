import pandas as pd

vector = pd.Series([1, 2, 3, 4, 200, 400, 10, 25])

for i in range(len(vector)):
    if not (vector.median() - vector.std() < vector[i] < vector.median() + vector.std()):
        vector[i] = None

print(vector)
print(vector.interpolate())
