from math import sqrt
import numpy as np
from matplotlib import pyplot as plt
from numpy import random
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import numpy as np
from sklearn.model_selection import train_test_split

def disttance_1(row1, row2):
    distance = 0.0
    for i in range(len(row1)-1):
        distance += abs((row1[i] - row2[i]))
    return distance


def get_neighbors(train, test_row, num_neighbors):
    distances = list()
    for train_row in train:
        dist = disttance_1(test_row, train_row)
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


def generate_data(quantity, cech_quantity, class_quantity):
    result_to_learn = []
    class_to_learn = []

    for j in range(class_quantity):
        for i in range(quantity // class_quantity):
            row = random.rand(cech_quantity) + j - 0.5 * j
            result_to_learn.append(row)
            class_to_learn.append(j)
    return result_to_learn, class_to_learn


def generate_data_to_plot_data(generate_data, generated_class):
    result = [[] for i in set(generated_class)]
    for i in range(len(generate_data)):
        result[generated_class[i]].append(generate_data[i])
    return result


def plot_generated_data(generate_data, generated_class):
    colors = ['r+', 'b+', 'm+', 'y+', 'c+', 'g+']
    unique_class = set(generated_class)
    colors = [colors[i] for i in range(len(unique_class))]
    data_to_plot = generate_data_to_plot_data(generate_data, generated_class)
    if len(generate_data[0]) == 2:
        fig = plt.figure()
        fig.add_subplot(111)

        def plot_figure(data, color, label):
            plt.plot([i[0] for i in data], [i[1] for i in data], color, label=label)

        for i in range(len(colors)):
            plot_figure(data_to_plot[i], colors[i], f'class {i}')

        plt.legend()
        plt.show()
    else:
        fig = plt.figure()
        fig.add_subplot(111, projection='3d')

        def plot_figure(data, color, label):
            plt.plot([i[0] for i in data], [i[1] for i in data], [i[2] for i in data], color, label=label)

        for i in range(len(colors)):
            plot_figure(data_to_plot[i], colors[i], f'class {i}')

        plt.legend()
        plt.show(block=False)


data, classes = generate_data(100, 2, 2)

plot_generated_data(data, classes)


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
