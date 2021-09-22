import pandas as pd

vector = pd.Series([1, 2, 3, 4, 200, 400, 10, 25])


# Replace outliers with None
def find_outliers(vector):
    result = []
    for i in range(len(vector)):
        if vector.median() - vector.std() < vector[i] < vector.median() + vector.std():
            result.append(vector[i])
        else:
            result.append(None)
    return pd.Series(result)


vector = find_outliers(vector)

print(vector)
# Replace None with good values
print(vector.interpolate())
