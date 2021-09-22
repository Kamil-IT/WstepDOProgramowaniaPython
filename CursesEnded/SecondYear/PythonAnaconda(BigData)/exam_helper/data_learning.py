from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

from generate_data_test import generate_data, plot_generated_data


def good_prediction_give_point(predicted, test_classes):
    success = 0
    for i in range(len(predicted)):
        if predicted[i] == test_classes[i]:
            success += 1
    return success / len(predicted)


def learn_and_test_data(method_obj, ratting_method, train_features, train_classes, test_features, test_classes):
    # Build model
    clf = method_obj
    clf.fit(train_features, train_classes)

    # Prediction
    predicted = clf.predict(test_features)

    return ratting_method(predicted, test_classes)


data, classes = generate_data(500, 3, 5)
plot_generated_data(data, classes)

train_data, test_data, train_class, test_class = train_test_split(data, classes, test_size=0.3)

for i in [KNeighborsClassifier(), MLPClassifier(), DecisionTreeClassifier(), SVC()]:
    print(i.__str__() + str(
        learn_and_test_data(i, good_prediction_give_point, train_data, train_class, test_data, test_class)))
