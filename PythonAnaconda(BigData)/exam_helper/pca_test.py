from matplotlib import pyplot as plt
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split

from generate_data_test import generate_data, plot_generated_data

def plot_ratio_pca(ratio):
    fig = plt.figure()
    fig.add_subplot(111)
    plt.bar([i for i in range(len(ratio))], ratio)
    plt.show()


data, classes = generate_data(500, 3, 5)
plot_generated_data(data, classes)

train_data, test_data, train_class, test_class = train_test_split(data, classes, test_size=0.3)


pca = PCA(n_components=2)
transform_train = pca.fit_transform(train_data)
transform_test = pca.transform(test_data)

plot_generated_data(transform_train, train_class)
plot_ratio_pca(pca.explained_variance_ratio_)
