# --------------------------------------------------------------------------
# -----------------------  Podstawy nauki o danych  ------------------------
# --------------------------------------------------------------------------
#  Zadanie 1: Regresja liniowa
#  autorzy: A. Gonczarek, J. Kaczmar, S. Zareba, P. Dąbrowski, M Zięba
#  2018
# --------------------------------------------------------------------------

import numpy as np
from numpy.linalg import inv as inv

from utils import polynomial


def mean_squared_error(x, y, w):
    """
    :param x: ciag wejsciowy Nx1
    :param y: ciag wyjsciowy Nx1
    :param w: parametry modelu (M+1)x1
    :return: blad sredniokwadratowy pomiedzy wyjsciami y
    oraz wyjsciami uzyskanymi z wielowamiu o parametrach w dla wejsc x
    """
    return np.mean(np.power(polynomial(x, w) - y, 2))


def design_matrix(x_train, M):
    """
    :param x_train: ciag treningowy Nx1
    :param M: stopien wielomianu 0,1,2,...
    :return: funkcja wylicza Design Matrix Nx(M+1) dla wielomianu rzedu M
    """

    des_mat = np.zeros((len(x_train), M + 1))
    # x^0 x^1 x^2 x^3 ... x^M+1
    for row in range(len(x_train)):
        for col in range(M + 1):
            des_mat[row][col] = x_train[row] ** col

    # Φ
    return des_mat


def least_squares(x_train, y_train, M):
    """
    :param x_train: ciag treningowy wejscia Nx1
    :param y_train: ciag treningowy wyjscia Nx1
    :param M: rzad wielomianu
    :return: funkcja zwraca krotke (w,err), gdzie w sa parametrami dopasowanego wielomianu, a err blad sredniokwadratowy
    dopasowania
    """
    matrix = design_matrix(x_train, M)
    ls = inv(matrix.transpose() @ matrix) @ matrix.transpose() @ y_train
    ms_err = mean_squared_error(x_train, y_train, ls)
    return ls, ms_err


def regularized_least_squares(x_train, y_train, M, regularization_lambda):
    """
    :param x_train: ciag treningowy wejscia Nx1
    :param y_train: ciag treningowy wyjscia Nx1
    :param M: rzad wielomianu
    :param regularization_lambda: parametr regularyzacji
    :return: funkcja zwraca krotke (w,err), gdzie w sa parametrami dopasowanego wielomianu zgodnie z kryterium z regularyzacja l2,
    a err blad sredniokwadratowy dopasowania
    """

    matrix_des = design_matrix(x_train, M)
    matrix_des_trans = matrix_des.transpose()

    regularization_matrix = np.zeros((matrix_des.shape[1], matrix_des.shape[1]))
    for i in range(regularization_matrix.shape[0]):
        for j in range(regularization_matrix.shape[0]):
            if i == j:
                regularization_matrix[i][j] = regularization_lambda

    rls = inv(matrix_des_trans @ matrix_des + regularization_matrix) @ matrix_des_trans @ y_train
    err = mean_squared_error(x_train, y_train, rls)
    return rls, err


def model_selection(x_train, y_train, x_val, y_val, M_values):
    """
    :param x_train: ciag treningowy wejscia Nx1
    :param y_train: ciag treningowy wyjscia Nx1
    :param x_val: ciag walidacyjny wejscia Nx1
    :param y_val: ciag walidacyjny wyjscia Nx1
    :param M_values: tablica stopni wielomianu, ktore maja byc sprawdzone
    :return: funkcja zwraca krotke (w,train_err,val_err), gdzie w sa parametrami modelu, ktory najlepiej generalizuje dane,
    tj. daje najmniejszy blad na ciagu walidacyjnym, train_err i val_err to bledy na sredniokwadratowe na ciagach treningowym
    i walidacyjnym
    """

    M_val = M_values[0]
    ls_min, ls_err_min = least_squares(x_train, y_train, M_val)
    ms_err_min = mean_squared_error(x_val, y_val, ls_min)
    for M in M_values:
        ls, ls_err = least_squares(x_train, y_train, M)
        ms_err = mean_squared_error(x_val, y_val, ls)
        if ms_err < ms_err_min:
            ls_min = ls
            ls_err_min = ls_err
            ms_err_min = ms_err

    return ls_min, ls_err_min, ms_err_min


def regularized_model_selection(x_train, y_train, x_val, y_val, M, lambda_values):
    """
    :param x_train: ciag treningowy wejscia Nx1
    :param y_train: ciag treningowy wyjscia Nx1
    :param x_val: ciag walidacyjny wejscia Nx1
    :param y_val: ciag walidacyjny wyjscia Nx1
    :param M: stopien wielomianu
    :param lambda_values: lista ze wartosciami roznych parametrow regularyzacji
    :return: funkcja zwraca krotke (w,train_err,val_err,regularization_lambda), gdzie w sa parametrami modelu, ktory najlepiej generalizuje dane,
    tj. daje najmniejszy blad na ciagu walidacyjnym. Wielomian dopasowany jest wg kryterium z regularyzacja. train_err i val_err to
    bledy na sredniokwadratowe na ciagach treningowym i walidacyjnym. regularization_lambda to najlepsza wartosc parametru regularyzacji
    """
    reg_param_min = lambda_values[0]
    rls_min, rls_err_min = regularized_least_squares(x_train, y_train, M, reg_param_min)
    ms_err_min = mean_squared_error(x_val, y_val, rls_min)
    for reg_param in lambda_values:
        rls, rls_err = regularized_least_squares(x_train, y_train, M, reg_param)
        ms_err = mean_squared_error(x_val, y_val, rls)
        if ms_err < ms_err_min:
            rls_min = rls
            rls_err_min = rls_err
            ms_err_min = ms_err
            reg_param_min = reg_param
    return rls_min, rls_err_min, ms_err_min, reg_param_min
