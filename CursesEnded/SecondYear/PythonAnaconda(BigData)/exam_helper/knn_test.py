from math import sqrt

import numpy as np
from sklearn.model_selection import train_test_split

from generate_data_test import generate_data

def euclidean_distance(row1, row2):
    distance = 0.0
    for i in range(len(row1) - 1):
        distance += (row1[i] - row2[i]) ** 2
    return sqrt(distance)


def get_neighbors(train, test_row, num_neighbors):
    distances = list()
    for train_row in train:
        dist = euclidean_distance(test_row, train_row)
        distances.append((train_row, dist))
    distances.sort(key=lambda tup: tup[1])
    neighbors = list()
    for i in range(num_neighbors):
        neighbors.append(distances[i][0])
    return neighbors


def predict_classification(train, test_row, num_neighbors):
    neighbors = get_neighbors(train, test_row, num_neighbors)
    output_values = [row[-1] for row in neighbors]
    prediction = max(set(output_values), key=output_values.count)
    return prediction


def k_nearest_neighbors(train, test, num_neighbors):
    predictions = list()
    for row in test:
        output = predict_classification(train, row, num_neighbors)
        predictions.append(output)
    return predictions


data, classes = generate_data(500, 2, 5)
# plot_generated_data(data, classes)

train_data, test_data, train_class, test_class = train_test_split(data, classes, test_size=0.3)

for i in range(len(train_data)):
    train_data[i] = np.append(train_data[i], train_class[i])

predictions = k_nearest_neighbors(train_data, test_data, 5)
success = 0
for i in range(len(predictions)):
    if predictions[i] == test_class[i]:
        success += 1

print(success / len(predictions))
