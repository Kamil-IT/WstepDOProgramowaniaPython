from pylab import *

import fashion_mnist.utils.mnist_reader as mnist_reader
from naive_bayes import GaussianNaiveBayes


def load_mnist_dataset():
    dir_loc = '/home/kamil/PycharmProjects/image-recognition-msid/fashion_mnist/data/fashion'
    train_set = mnist_reader.load_mnist(dir_loc, kind='train')
    test_set = mnist_reader.load_mnist(dir_loc, kind='t10k')

    return train_set, test_set


def mnist_digit_recognition():
    train_set, test_set = load_mnist_dataset()
    n_labels = 10  # 1,2,3,4,5,6,7,9,0
    n_features = 28 * 28

    draw_ex_images(5, 4, train_set[0].shape[0], train_set[0])

    mnist_model = GaussianNaiveBayes(n_labels, n_features)
    start = time.time()
    mnist_model.train(train_set[0], train_set[1])
    end = time.time()
    print(end - start)
    mnist_model.save_model()
    mean, var, pi = mnist_model.get_parameters()
    print(f"Model parameters: mean {mean}, var {var}, pi {pi}")

    test_data, labels = test_set
    limit = 150
    test_data, labels = test_data[:limit], labels[:limit]
    results = np.arange(limit, dtype=np.int)
    for n in range(limit):
        results[n] = mnist_model.classify(test_data[n])
        print(f"{n} : predicted {results[n]}, correct {labels[n]}")

    print("recognition rate: ", (results == labels).mean())


def draw_ex_images(n_cols, n_rows, n_images, train_set):
    for i in range(1, n_rows * n_cols + 1):
        im_idx = randint(0, n_images - 1)
        pixels = train_set[im_idx]
        plt.subplot(n_rows, n_cols, i)
        pixels.resize(28, 28)
        plt.imshow(pixels, cmap='gray')
        plt.axis('off')
    plt.show()


if __name__ == "__main__":
    mnist_digit_recognition()
