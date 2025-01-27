# --------------------------------------------------------------------------
# -----------------------  Rozpoznawanie Obrazow  --------------------------
# --------------------------------------------------------------------------
#  Zadanie 2: k-NN i Naive Bayes
#  autorzy: A. Gonczarek, J. Kaczmar, S. Zareba, P. Dąbrowski
#  2018
# --------------------------------------------------------------------------

from __future__ import division

import numpy as np


def hamming_distance(X, X_train):
    """
    :param X: zbior porownwanych obiektow N1xD
    :param X_train: zbior obiektow do ktorych porownujemy N2xD
    Funkcja wyznacza odleglosci Hamminga obiektow ze zbioru X od
    obiektow X_train. Odleglosci obiektow z jednego i drugiego
    zbioru zwrocone zostana w postaci macierzy
    :return: macierz odleglosci pomiedzy obiektami z X i X_train N1xN2
    """
    x_array = X.toarray()
    x_train_array = X_train.toarray()
    x_inv = np.invert(x_array).astype(int)
    x_train_inv = np.invert(x_train_array).astype(int)

    return x_inv @ x_train_array.transpose() + x_array @ x_train_inv.transpose()


def sort_train_labels_knn(Dist, y):
    """
    Funkcja sortujaca etykiety klas danych treningowych y
    wzgledem prawdopodobienstw zawartych w macierzy Dist.
    Funkcja zwraca macierz o wymiarach N1xN2. W kazdym
    wierszu maja byc posortowane etykiety klas z y wzgledem
    wartosci podobienstw odpowiadajacego wiersza macierzy
    Dist
    :param Dist: macierz odleglosci pomiedzy obiektami z X
    i X_train N1xN2
    :param y: wektor etykiet o dlugosci N2
    :return: macierz etykiet klas posortowana wzgledem
    wartosci podobienstw odpowiadajacego wiersza macierzy
    Dist. Uzyc algorytmu mergesort.
    """
    return y[Dist.argsort(kind='mergesort')]


def p_y_x_knn(y, k):
    """
    Funkcja wyznacza rozklad prawdopodobienstwa p(y|x) dla
    kazdej z klas dla obiektow ze zbioru testowego wykorzystujac
    klasfikator KNN wyuczony na danych trenningowych
    :param y: macierz posortowanych etykiet dla danych treningowych N1xN2
    :param k: liczba najblizszuch sasiadow dla KNN
    :return: macierz prawdopodobienstw dla obiektow z X
    """
    result = np.zeros((len(y), 4))
    for i in range(len(y)):
        for j in range(k):
            result[i, y[i, j]] = result[i, y[i, j]] + 1
    return 1 / k * result


def classification_error(p_y_x, y_true):
    """
    Wyznacz blad klasyfikacji.
    :param p_y_x: macierz przewidywanych prawdopodobienstw
    :param y_true: zbior rzeczywistych etykiet klas 1xN.
    Kazdy wiersz macierzy reprezentuje rozklad p(y|x)
    :return: blad klasyfikacji
    """
    sum_ = 0
    for i in range(y_true.shape[0]):
        max_index = -1
        for j in range(p_y_x[:][i].shape[0]):
            if max(p_y_x[:][i]) == p_y_x[i][j]:
                max_index = j
        if max_index != y_true[i]:
            sum_ += 1
    return 1 / y_true.shape[0] * sum_


def model_selection_knn(Xval, Xtrain, yval, ytrain, k_values):
    """
    :param Xval: zbior danych walidacyjnych N1xD
    :param Xtrain: zbior danych treningowych N2xD
    :param yval: etykiety klas dla danych walidacyjnych 1xN1
    :param ytrain: etykiety klas dla danych treningowych 1xN2
    :param k_values: wartosci parametru k, ktore maja zostac sprawdzone
    :return: funkcja wykonuje selekcje modelu knn i zwraca krotke (best_error,best_k,errors), gdzie best_error to najnizszy
    osiagniety blad, best_k - k dla ktorego blad byl najnizszy, errors - lista wartosci bledow dla kolejnych k z k_values
    """
    y_dys_sorted = sort_train_labels_knn(hamming_distance(Xval, Xtrain), ytrain)
    best_k = -1
    best_error = classification_error(p_y_x_knn(y_dys_sorted, k_values[0]), yval)
    error_list = []
    for k in k_values:
        error = classification_error(p_y_x_knn(y_dys_sorted, k), yval)
        if error < best_error:
            best_k = k
            best_error = error
        error_list.append(error)
    return best_error, best_k, error_list


def estimate_a_priori_nb(ytrain):
    """
    :param ytrain: etykiety dla dla danych treningowych 1xN
    :return: funkcja wyznacza rozklad a priori p(y) i zwraca p_y - wektor prawdopodobienstw a priori 1xM
    """
    a_priori_nb = []
    for i in range(len(np.unique(ytrain))):
        a_priori_nb.append(np.count_nonzero(ytrain == i))
    return 1 / ytrain.shape[0] * np.array(a_priori_nb)


def estimate_p_x_y_nb(Xtrain, ytrain, a, b):
    """
    :param Xtrain: dane treningowe NxD
    :param ytrain: etykiety klas dla danych treningowych 1xN
    :param a: parametr a rozkladu Beta
    :param b: parametr b rozkladu Beta
    :return: funkcja wyznacza rozklad prawdopodobienstwa p(x|y) zakladajac, ze x przyjmuje wartosci binarne i ze elementy
    x sa niezalezne od siebie. Funkcja zwraca macierz p_x_y o wymiarach MxD.
    """
    Xtrain_array = Xtrain.toarray()
    M = len(np.unique(ytrain))
    D = Xtrain_array.shape[1]
    sum_up = np.zeros((M, D))
    sum_down = np.zeros((M, D))
    for i in range(ytrain.shape[0]):
        sum_down[ytrain[i]] += 1
        sum_up[ytrain[i]] += Xtrain_array[i]
    return (sum_up + a - 1) / (sum_down + a + b - 2)


def p_y_x_nb(p_y, p_x_1_y, X):
    """
    :param p_y: wektor prawdopodobienstw a priori o wymiarach 1xM
    :param p_x_1_y: rozklad prawdopodobienstw p(x=1|y) - macierz MxD
    :param X: dane dla ktorych beda wyznaczone prawdopodobienstwa, macierz NxD
    :return: funkcja wyznacza rozklad prawdopodobienstwa p(y|x) dla kazdej z klas z wykorzystaniem klasyfikatora Naiwnego
    Bayesa. Funkcja zwraca macierz p_y_x o wymiarach NxM.
    """
    X_array = X.toarray()
    M = p_y.shape[0]
    N = X_array.shape[0]
    result = np.zeros((N, M))

    for i in range(N):
        Xarray_i = X_array[i]
        Xarray_i_rev = 1 - Xarray_i
        for j in range(M):
            up = (np.power(p_x_1_y[j], Xarray_i) * np.power(1 - p_x_1_y[j], Xarray_i_rev)).prod() * p_y[j]
            down = 0
            for k_prim in range(M):
                down += (np.power(p_x_1_y[k_prim], Xarray_i) * np.power(1 - p_x_1_y[k_prim], Xarray_i_rev)).prod() * p_y[k_prim]
            result[i][j] = up / down
    return result


def model_selection_nb(Xtrain, Xval, ytrain, yval, a_values, b_values):
    """
    :param Xtrain: zbior danych treningowych N2xD
    :param Xval: zbior danych walidacyjnych N1xD
    :param ytrain: etykiety klas dla danych treningowych 1xN2
    :param yval: etykiety klas dla danych walidacyjnych 1xN1
    :param a_values: lista parametrow a do sprawdzenia
    :param b_values: lista parametrow b do sprawdzenia
    :return: funkcja wykonuje selekcje modelu Naive Bayes - wybiera najlepsze wartosci parametrow a i b. Funkcja zwraca
    krotke (error_best, best_a, best_b, errors) gdzie best_error to najnizszy
    osiagniety blad, best_a - a dla ktorego blad byl najnizszy, best_b - b dla ktorego blad byl najnizszy,
    errors - macierz wartosci bledow dla wszystkich par (a,b)
    """
    estimate_a_priori = estimate_a_priori_nb(ytrain)
    errors = np.zeros((a_values.shape[0], b_values.shape[0]))
    error_best = 100000
    best_a = 0
    best_b = 0
    for i in range(a_values.shape[0]):
        for j in range(b_values.shape[0]):
            p_x_y_es = estimate_p_x_y_nb(Xtrain, ytrain, a_values[i], b_values[j])
            p_x_y = p_y_x_nb(estimate_a_priori, p_x_y_es, Xval)
            errors[i][j] = classification_error(p_x_y, yval)
            if error_best > errors[i][j]:
                error_best = errors[i][j]
                best_a = a_values[i]
                best_b = b_values[j]
    return error_best, best_a, best_b, errors
