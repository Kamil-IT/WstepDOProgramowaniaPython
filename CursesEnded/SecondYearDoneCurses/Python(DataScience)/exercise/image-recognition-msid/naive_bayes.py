import json

import numpy as np
import scipy
import scipy.stats


class GaussianNaiveBayes:

    def __init__(self, n_labels, n_features):
        self.n_labels = int(n_labels)
        self.n_features = int(n_features)
        self.mean = np.zeros((n_labels, n_features), dtype=np.float)
        self.var = np.zeros((n_labels, n_features), dtype=np.float)
        self.pi = np.zeros(n_labels, dtype=np.float)

    def classify(self, data):
        results = [self.negative_log_likelihood(data, y) for y in range(self.n_labels)]
        return np.argmin(results)

    def train(self, data, labels):
        N = data.shape[0]  # the number of training data
        N_l = np.array([(labels == y).sum() for y in range(self.n_labels)], dtype=np.float)  # count for each label

        # update Gaussian mean
        for y in range(self.n_labels):
            sum = np.sum(data[n] if labels[n] == y else 0.0 for n in range(N))
            self.mean[y] = sum / N_l[y]

        # update Gaussian variance
        for y in range(self.n_labels):
            sum = np.sum((data[n] - self.mean[y]) ** 2 if labels[n] == y else 0.0 for n in range(N))
            self.var[y] = sum / N_l[y]

        # update prior of labels
        self.pi = N_l / N

    def negative_log_likelihood(self, data, labels):
        log_prior_y = -np.log(self.pi[labels])
        log_posterior_x_given_y = -np.sum([
            self.log_gaussian_wrap(
                data[d],
                self.mean[labels][d],
                self.var[labels][d]) for d in range(self.n_features)])
        return log_prior_y + log_posterior_x_given_y

    def save_model(self):
        f = open("model.json", "w")
        json_model = str(
            json.dumps(
                {"mean": str(list(self.mean)),
                 "var": str(list(self.var)),
                 "pi": str(list(self.pi))})
        ).replace("\\n", "\n")
        f.write(json_model.__str__())
        f.close()

    def log_gaussian_wrap(self, x, mean, var):
        epsilon = 0.0000001
        if var < epsilon:
            return 0.0
        return scipy.stats.norm(mean, var).logpdf(x)

    def get_parameters(self):
        return self.mean, self.var, self.pi
