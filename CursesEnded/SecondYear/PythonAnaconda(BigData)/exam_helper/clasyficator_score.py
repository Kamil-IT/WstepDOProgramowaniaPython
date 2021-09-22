from matplotlib import pyplot as plt
from sklearn.metrics import roc_curve, plot_roc_curve
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

from generate_data_test import generate_data


# Binary
# https://pl.wikipedia.org/wiki/Tablica_pomy%C5%82ek
# TP - prawdziwie pozytywna (prawda dobrze rozpoznana (1))
# FP - fałszywie pozytywna (prawda zle rozpoznana (1))
# FN - fałszywie negatywne (fałsz zle rozpoznany (0))
# TN - prawdziwie negatywna (fałsz dobrze rozpoznany (0))


def tp(prediction, classes):
    score = 0
    for i in range(len(prediction)):
        if prediction[i] == 1 and classes[i] == 1:
            score += 1
    return score


def fp(prediction, classes):
    score = 0
    for i in range(len(prediction)):
        if prediction[i] == 1 and classes[i] == 0:
            score += 1
    return score


def fn(prediction, classes):
    score = 0
    for i in range(len(prediction)):
        if prediction[i] == 0 and classes[i] == 1:
            score += 1
    return score


def tn(prediction, classes):
    score = 0
    for i in range(len(prediction)):
        if prediction[i] == 0 and classes[i] == 0:
            score += 1
    return score


# krzywa roc

data, classes = generate_data(10000, 2, 2)

train_data, test_data, train_class, test_class = train_test_split(data, classes, test_size=0.3)

clf = SVC()
clf.fit(train_data, train_class)

# Prediction
predicted = clf.predict(test_data)

curve = plot_roc_curve(clf, test_data, test_class)
plt.show()