import numpy as np
import pandas as pd
import networkx as nx
V = 6
G = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 0), (0, 1)]


def lvk(V, G, is_directed):
    print('== Lista wierzchołków i krawędzi ==')
    Vlist = []
    for v in range(V):
        Vlist.append(v)
    return Vlist, G


def nm(V, G, is_directed):
    print('== Macierz sąsiedztwa ==')
    nm = np.zeros((V, V))
    for k in G:
        nm[k[0]][k[1]] = 1
        if not is_directed:
            nm[k[1]][k[0]] = 1
    df = pd.DataFrame(nm)
    return df


def moi(V, G, is_directed):
    print('== Macierz incydencji ==')
    if not is_directed:
        return "Ta metoda działa tylko dla grafów skierowanych"
    else:
        moi = np.zeros((V, len(G)))
        for r in range(len(G)):
            moi[G[r][0]][r] = 1
            moi[G[r][1]][r] = -1
    df = pd.DataFrame(moi)
    return df


def shortestpath(V, G, is_directed, start, end):
    matrix = nm(V, G, is_directed)
    for i in range(1, V):
        m = np.linalg.matrix_power(matrix, i)
        if m[start][end] != 0:
            return i
    return "Droga nie istnieje"


def connectivity(V, G):
    matrix = nm(V, G, False)
    c = [0] * V
    for v1 in range(V):
        for v2 in range(V):
            if matrix[v1][v2] != 0:
                c[v2] = 1
    for i in c:
        if i == 0:
            return "Graf nie jest spójny"
    return "Graf jest spójny"


def print_methods(V, G, is_directed, method):
    if method == 1:
        return lvk(V, G, is_directed)
    elif method == 2:
        return nm(V, G, is_directed)
    elif method == 3:
        return moi(V, G, is_directed)
    else:
        exit()


if __name__ == '__main__':
    print('Czy graf ma być skierowany? (True/False): ', end='')
    choose = str(input())
    if choose == 'True':
        is_directed = True
    elif choose == 'False':
        is_directed = False
    else:
        exit()

    for method in range(1, 4):
        print(print_methods(V, G, is_directed, method))
    print(shortestpath(V, G, is_directed, 2, 1))
    print(connectivity(V, G))
