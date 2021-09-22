import time

import numpy as np
import pandas as pd
import sklearn
from matplotlib import pyplot as plt
from sklearn import tree
from sklearn.decomposition import PCA
from sklearn.neural_network import MLPClassifier
from sklearn.naive_bayes import GaussianNB

CLASS_TO_NAME = {1: "WALKING", 2: "WALKING_UPSTAIRS", 3: "WALKING_DOWNSTAIRS", 4: "SITTING", 5: "STANDING", 6: "LAYING"}


def get_data(location, type):
    data = pd.read_csv(f'{location}X_{type}.txt', header=None, delimiter=r"\s+").transpose()
    classes = pd.read_csv(f'{location}y_{type}.txt', header=None, delimiter=r"\s+")
    return data, np.array([i[0] for i in classes.values.tolist()]).tolist()


def sort_classes(features, classes):
    walking = []
    walking_upstairs = []
    walking_downstairs = []
    sitting = []
    standing = []
    laying = []
    values = features
    for i in range(len(values)):
        if int(classes[i]) == 1:
            walking.append(values[i])
        elif int(classes[i]) == 2:
            walking_upstairs.append(values[i])
        elif int(classes[i]) == 3:
            walking_downstairs.append(values[i])
        elif int(classes[i]) == 4:
            sitting.append(values[i])
        elif int(classes[i]) == 5:
            standing.append(values[i])
        elif int(classes[i]) == 6:
            laying.append(values[i])
    return walking, walking_upstairs, walking_downstairs, sitting, standing, laying


def transform_features_pca(pca, data):
    compressed_features = pca.transform(data)
    ratio = pca.explained_variance_ratio_
    return compressed_features.transpose().tolist(), ratio


def visualise(features, classes):
    walking, walking_upstairs, walking_downstairs, sitting, standing, laying = sort_classes(features, classes)

    fig = plt.figure()
    fig.add_subplot(111, projection='3d')

    def plot_figure(data, color, label):
        plt.plot([i[0] for i in data], [i[1] for i in data], [i[2] for i in data], color, label=label)

    plot_figure(walking, 'r+', CLASS_TO_NAME[1])
    plot_figure(walking_upstairs, 'b+', CLASS_TO_NAME[2])
    plot_figure(walking_downstairs, 'm+', CLASS_TO_NAME[3])
    plot_figure(sitting, 'y+', CLASS_TO_NAME[4])
    plot_figure(standing, 'c+', CLASS_TO_NAME[5])
    plot_figure(laying, 'g+', CLASS_TO_NAME[6])
    plt.legend()
    plt.show()


def svc_prediction(train_features, train_classes, test_features, test_classes):
    start = time.time()
    # Build model
    clf = sklearn.svm.SVC()
    clf.fit(train_features, train_classes)

    # Prediction
    predicted = clf.predict(test_features)

    # Benchmark
    success = 0
    success_stay = 0
    for i in range(len(predicted)):
        if predicted[i] in [1, 2, 3] and test_classes[i] in [1, 2, 3]:
            success_stay += 1
        if predicted[i] in [4, 5, 6] and test_classes[i] in [4, 5, 6]:
            success_stay += 1
        if predicted[i] == test_classes[i]:
            success += 1
    print(f'SVM success ratio: {success / len(predicted)}')
    print(f'SVM success ratio stand/move: {success_stay / len(predicted)}')
    end = time.time()
    print(end - start)
    return success / len(predicted)


def gaussianNB_prediction(train_features, train_classes, test_features, test_classes):
    start = time.time()
    # Build model
    clf = GaussianNB()
    clf.fit(train_features, train_classes)

    # Prediction
    predicted = clf.predict(test_features)

    # Benchmark
    success = 0
    success_stay = 0
    for i in range(len(predicted)):
        if predicted[i] in [1, 2, 3] and test_classes[i] in [1, 2, 3]:
            success_stay += 1
        if predicted[i] in [4, 5, 6] and test_classes[i] in [4, 5, 6]:
            success_stay += 1
        if predicted[i] == test_classes[i]:
            success += 1
    print(f'Gaussian NB success ratio: {success / len(predicted)}')
    print(f'Gaussian NB ratio stand/move: {success_stay / len(predicted)}')
    end = time.time()
    print(end - start)
    return success / len(predicted)


def decision_trees_prediction(train_features, train_classes, test_features, test_classes):
    start = time.time()

    # Build model
    clf = tree.DecisionTreeClassifier()
    clf.fit(train_features, train_classes)

    # Prediction
    predicted = clf.predict(test_features)

    # Benchmark
    success = 0
    success_stay = 0
    for i in range(len(predicted)):
        if predicted[i] in [1, 2, 3] and test_classes[i] in [1, 2, 3]:
            success_stay += 1
        if predicted[i] in [4, 5, 6] and test_classes[i] in [4, 5, 6]:
            success_stay += 1
        if predicted[i] == test_classes[i]:
            success += 1
    print(f'Decision trees success ratio: {success / len(predicted)}')
    print(f'Decision trees success ratio stand/move: {success_stay / len(predicted)}')
    end = time.time()
    print(end - start)
    return success / len(predicted)


def MLP_prediction(train_features, train_classes, test_features, test_classes):
    start = time.time()
    # Build model
    clf = MLPClassifier()
    clf.fit(train_features, train_classes)

    # Prediction
    predicted = clf.predict(test_features)

    # Benchmark
    success = 0
    success_stay = 0
    for i in range(len(predicted)):
        if predicted[i] in [1, 2, 3] and test_classes[i] in [1, 2, 3]:
            success_stay += 1
        if predicted[i] in [4, 5, 6] and test_classes[i] in [4, 5, 6]:
            success_stay += 1
        if predicted[i] == test_classes[i]:
            success += 1
    print(f'MLP success ratio: {success / len(predicted)}')
    print(f'MLP success ratio stand/move: {success_stay / len(predicted)}')
    end = time.time()
    print(end - start)
    return success / len(predicted)


pca = PCA(n_components=3)

# Train data
train_data, train_classes = get_data('dataset/train/', 'train')
train_compressed_features = pca.fit_transform(train_data.transpose())
train_features_ratio = pca.explained_variance_ratio_
print(train_features_ratio)

# Test data
test_data, test_classes = get_data('dataset/test/', 'test')
test_compressed_features = pca.transform(test_data.transpose())

visualise(train_compressed_features, train_classes)

x = [3, 75, 100, 150, 200, 250, 300, 350, 400]
svc = []
tree_p = []
MLP = []
NB = []

for i in x:
    pca = PCA(n_components=i)
    train_compressed_features = pca.fit_transform(train_data.transpose())
    test_compressed_features = pca.transform(test_data.transpose())
    svc.append(svc_prediction(train_compressed_features, train_classes, test_compressed_features, test_classes))
    tree_p.append(decision_trees_prediction(train_compressed_features, train_classes, test_compressed_features, test_classes))
    MLP.append(MLP_prediction(train_compressed_features, train_classes, test_compressed_features, test_classes))
    NB.append(gaussianNB_prediction(train_compressed_features, train_classes, test_compressed_features, test_classes))

fig = plt.figure()
fig.add_subplot(111)
plt.plot(x, svc, label='svc')
plt.plot(x, tree_p, label='tree')
plt.plot(x, MLP, label='mlp')
plt.plot(x, NB, label='nb')
plt.legend()
plt.show()