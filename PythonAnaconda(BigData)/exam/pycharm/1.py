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


data, classes = generate_data(200, 2, 2)

train_data, test_data, train_class, test_class = train_test_split(data, classes, test_size=0.3)

plot_generated_data(train_data, train_class)
plot_generated_data(test_data, test_class)

clf = SVC()
clf.fit(train_data, train_class)

# Prediction
predicted = clf.predict(test_data)

tn_val = tn(predicted, test_class)
tp_val = tp(predicted, test_class)
fp_val = fp(predicted, test_class)
fn_val = fn(predicted, test_class)

dokladnosc = (tp_val / tn_val) / (tp_val + tn_val + fp_val + fn_val)
precyzja = tp_val / (tp_val + fp_val)
specyficznosc = tn_val / (tn_val + fp_val)

print("Bazowałem na klasyfikatorze SVC")
print("Dokładność " + str(dokladnosc))
print("precyzja " + str(precyzja))
print("specyficznosc " + str(specyficznosc))

fig = plt.figure()
fig.add_subplot(111)
plt.bar(['Dokładność', 'precyzja', 'specyficznosc'], [dokladnosc, precyzja, specyficznosc])
plt.show()