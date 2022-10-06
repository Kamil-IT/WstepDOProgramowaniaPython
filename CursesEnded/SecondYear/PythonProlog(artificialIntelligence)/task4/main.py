import numpy as np
import pandas as pd
import tensorflow as tf
from keras.losses import MeanSquaredError
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential


def predict(model, x):
    return model.predict(np.array([x]))


max_accuracy = 0

# Choose learning rate
# lr = 0
# for i in range(10):
#     lr = i / 1000

for i in range(1):
    # 2159
    X = pd.read_csv('radio_train/input_data.csv').to_numpy()
    Y = pd.read_csv('radio_train/target_data.csv').to_numpy() + 0.2

    X_train = X[::2]
    Y_train = Y[::2]

    X_valid = X[1::2]
    Y_valid = Y[1::2]

    # Random choice train and valid
    # np.random.seed(1)
    # rand_id = np.random.choice(range(X.shape[0]), size=(1727,), replace=False)
    # X_train = X[rand_id]
    # Y_train = Y[rand_id]
    # X_valid = []
    # Y_valid = []
    # for i in X:
    #     if i not in X_train:
    #         X_valid.append(i)
    # for i in Y:
    #     if i not in Y_train:
    #         Y_valid.append(i)

    # cross validation
    # X_split = list(np.array_split(X, 4))
    # Y_split = list(np.array_split(Y, 4))
    #
    # X_valid = X_split[i]
    # Y_valid = Y_split[i]
    # X_train = []
    # Y_train = []
    # for e in range(4):
    #     if e != i:
    #         X_train.extend(X_split[e])
    #         Y_train.extend(X_split[e])


    n = X_train.shape[0]
    dim_no = X_train.shape[1]
    class_no = Y_train.shape[1]

    model = Sequential()
    model.add(Dense(128 * 7, input_dim=dim_no, activation='relu', kernel_initializer='glorot_uniform'))
    model.add(Dense(64 * 7, input_dim=dim_no, activation='relu', kernel_initializer='glorot_uniform'))
    model.add(Dense(32 * 7, input_dim=dim_no, activation='relu', kernel_initializer='glorot_uniform'))
    model.add(Dense(class_no, input_dim=dim_no, activation='sigmoid', kernel_initializer='glorot_uniform'))
    model.compile(loss=MeanSquaredError(), optimizer=tf.keras.optimizers.Adam(), metrics=['accuracy'])

    # Choose learning rate
    # model.compile(loss=MeanSquaredError(), optimizer=tf.keras.optimizers.Adam(learning_rate=lr), metrics=['accuracy'])

    tensorboard_callback = tf.keras.callbacks.TensorBoard(
        log_dir='log',
        histogram_freq=1)

    model.fit(X_train, Y_train, epochs=100, batch_size=100, validation_data=(X_valid, Y_valid),
              callbacks=tensorboard_callback)

    good = 0
    bad = 0
    error_interval = 0.001

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

    if max_accuracy < current_accuracy:
        tf.keras.models.save_model(
            model,
            'model2',
            overwrite=True,
            include_optimizer=True,
            save_format="tf",
            signatures=None
        )
        max_accuracy = current_accuracy

print(f'Final: {max_accuracy}')
