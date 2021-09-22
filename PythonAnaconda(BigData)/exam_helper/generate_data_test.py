import numpy as np
import numpy.random as random
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split


def generate_data(quantity, cech_quantity, class_quantity):
    # result_to_learn = [[cech1, cech2, cech3], [cech1, cech2, cech3]...]
    result_to_learn = []
    # class_to_learn = [class1, class2, class5...]
    class_to_learn = []

    for j in range(class_quantity):
        for i in range(quantity // class_quantity):
            row = random.rand(cech_quantity) + j - 0.5 * j
            result_to_learn.append(row)
            class_to_learn.append(j)
    return result_to_learn, class_to_learn


def generate_data_to_plot_data(generate_data, generated_class):
    # result =             class 1                       class 2
    # result = [[[x1, y1, z1], [x2, y2, z2]], [[x1, y1, z1], [x2, y2, z2]]...]
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


data, classes = generate_data(500, 3, 5)
plot_generated_data(data, classes)

train_data, test_data, train_class, test_class = train_test_split(data, classes, test_size=0.3)