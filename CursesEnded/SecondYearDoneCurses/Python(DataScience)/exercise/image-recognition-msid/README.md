# image-recognition-msid

## Introduction
Detection image presentation of 10 categories: T-shirt/top, Trouser, Pullover, Dress, Coat, Sandal, Shirt, Sneaker, Bag, Ankle boot

## Methods

The main method is [Gaussian Naive Bayes](https://machinelearningmastery.com/naive-bayes-for-machine-learning/)

## Results

| Creator | Accurancy (mean) | Training time | Reapets | Job started | Job Done
| --- | --- | --- | --- | --- | --- |
| Zalando benchmark  | 0.564 | 0:00:10 | 2 | 3 years ago | 3 years ago |
| Me | 0.279  | 0:00:4 | 3 | 08.01.2020 | 08.01.2020 |

## Usage

Liblary must have: pylab, gzip, numpy, scipy, json


How to run:
```bash
python3 mnist_recognition.py
```

Model is located in file [model.json](https://github.com/Kamil-IT/image-recognition-msid/blob/main/model.json)

Tested on:

Python 3.8.5

Ubuntu 20.04.1
