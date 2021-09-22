import pandas as pd
import random

vector = pd.Series([1, 2, 3, 4, 200, 400, 10, 25])

print("max" + str(vector.min()))
print("min" + str(vector.max()))
print("avg" + str(pd.Series.mean(vector)))
print("std" + str(pd.Series.std(vector)))

x = []

for i in vector:
    if vector.median() - vector.std() < i < vector.median() + vector.std():
        x.append(i)

print(x)