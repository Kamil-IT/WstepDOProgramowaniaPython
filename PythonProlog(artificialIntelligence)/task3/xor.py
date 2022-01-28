import numpy as np
from matplotlib import pyplot as plt

x = np.array([[0, 0, 1, 1],
              [0, 1, 0, 1],
              [0, 1, 0, 1]])
y = np.array([[0, 1, 1, 0]])

neuron_output = 1
neuron_hidden = 2

momentum = 0.9
learning_rate = 0.9

np.random.seed(5)
w1 = np.random.rand(neuron_hidden, x.shape[0])
w2 = np.random.rand(neuron_output, neuron_hidden)


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def forward_propagation(w1, w2, input=x):
    a_1 = sigmoid(np.dot(w1, input))
    a_2 = sigmoid(np.dot(w2, a_1))
    return a_1, a_2


def back_propagation(w_1, w_2, a_1, a_2):
    dz2 = a_2 - y

    dw1 = np.dot(
        np.dot(w_2.T, dz2) * a_1 * (1 - a_1),
        x.T) / training_size
    dw1 = np.reshape(dw1, w_1.shape)

    dw2 = np.reshape(
        np.dot(dz2, a_1.T) / training_size,
        w_2.shape)

    return dw2, dw1


def predict_number(w1, w2, input):
    _, a_2 = forward_propagation(w1, w2, input)
    a_2 = np.squeeze(a_2)
    if a_2 >= 0.5:
        return 1
    else:
        return 0


def calculate_predict_rate(w1, w2):
    good_calculation = np.array([
        predict_number(w1, w2, [[0], [0]]) == 0,
        predict_number(w1, w2, [[0], [1]]) == 1,
        predict_number(w1, w2, [[1], [0]]) == 1,
        predict_number(w1, w2, [[1], [1]]) == 0
    ])
    return good_calculation.sum() / 4


def calculate_metrics(w_1, w_2):
    predict_rate = calculate_predict_rate(w_1, w_2)
    predict_rates.append(predict_rate)

w1_copy = w1.copy()
w2_copy = w2.copy()
training_size = x.shape[1]
predict_rates = []
epochs = 200
# for e in range(10):
for c in range(10):
    last_d2 = 0
    last_d1 = 0
    learning_rate = 8
    momentum = 1 - c / 10
    for i in range(epochs):
        a1, a2 = forward_propagation(w1, w2)
        d_w2, d_w1 = back_propagation(w1, w2, a1, a2)

        d_1 = 1 * learning_rate * d_w1
        d_2 = 1 * learning_rate * d_w2
        # w1 = w1 - d_1 + momentum * last_d1
        # w2 = w2 - d_2 + momentum * last_d2

        # w2 = w2 - learning_rate * d_w2 - last_w2 * momentum
        # w1 = w1 - learning_rate * d_w1 - last_w1 * momentum
        # calculate_metrics(w1, w2)

        last_d2 = d_2.copy()
        last_d1 = d_1.copy()

    plt.plot(predict_rates,
             label='momentum: ' + str(round(momentum, 4)) + ', learning_rate: ' + str(round(learning_rate, 2)))

    predict_rates = []
    loss = []
    w1 = w1_copy.copy()
    w2 = w2_copy.copy()

plt.xlabel("Epochs")
plt.ylabel("Predict rate (%)")
plt.legend()
plt.show()
