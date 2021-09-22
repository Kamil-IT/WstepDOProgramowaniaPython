import numpy as np
from matplotlib import pyplot as plt
from numpy import random
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC


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



def dist(row1, row2):
    distance = 0.0
    for i in range(len(row1)-1):
        distance += abs((row1[i] - row2[i]))
    return distance




def select_best_cand(val, cands):
    best = 0
    best_dist = np.inf
    for el in cands:
        c_dist = dist(val, el)
        if c_dist < best_dist:
            best = el
            best_dist = c_dist
    return best


def gen_candidates(z, L, K):
    return [sum([z[j] for j in range(K[l])]) / K[l] for l in range(L)]


def classify(new_z, L, K, z):
    return select_best_cand(new_z, gen_candidates(z, L, K))
