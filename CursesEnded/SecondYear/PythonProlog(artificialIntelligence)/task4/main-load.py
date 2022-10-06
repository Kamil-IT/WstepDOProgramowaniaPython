import numpy as np
import pandas as pd
import tensorflow as tf


def predict(model, x):
    return model.predict(np.array([x]))


if __name__ == '__main__':
    # 2159
    X = pd.read_csv('radio_train/input_data.csv').to_numpy()
    Y = pd.read_csv('radio_train/target_data.csv').to_numpy() + 0.2

    X_train = X[::2]
    Y_train = Y[::2]

    X_valid = X[1::2]
    Y_valid = Y[1::2]

    n = X_train.shape[0]
    dim_no = X_train.shape[1]
    class_no = Y_train.shape[1]

    model = tf.keras.models.load_model("model/", compile=True)
    model.summary()
    good = 0
    bad = 0
    error_interval = 0
    for i in range(len(X_valid)):
        x = X_valid[i]
        y = Y_valid[i]
        y_predict = predict(model, x)
        if any((y_predict + error_interval > y)[0]) and any((y_predict - error_interval < y)[0]):
            good += 1
        else:
            bad += 1
            print(f'pred: {y_predict} real: {y}')
    print(f'good {good}')
    print(f'bad {bad}')
    current_accuracy = good / (bad + good)
    print(f'{current_accuracy}')
