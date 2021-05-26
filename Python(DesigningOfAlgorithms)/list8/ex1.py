import numpy as np
import pandas as pd


def lvk(V, G, is_directed):
    print('Lista wierzchołków i krawędzi')
    Vlist = []
    for v in range(V):
        Vlist.append(v)
    return Vlist, G


# Macierz sąsiedztwa
def adjacency_matrix(V, G, is_directed):
    print('Macierz sąsiedztwa')
    nm = np.zeros((V, V))
    for k in G:
        nm[k[0]][k[1]] = 1
        if not is_directed:
            nm[k[1]][k[0]] = 1
    df = pd.DataFrame(nm)
    return df


# Macierz incydencji
def incidence_matrix(V, G, is_directed):
    print('Macierz incydencji')
    if not is_directed:
        return "Macierz incydencji działa tylko dla grafów skierowanych"
    else:
        moi = np.zeros((V, len(G)))
        for r in range(len(G)):
            moi[G[r][0]][r] = 1
            moi[G[r][1]][r] = -1
    df = pd.DataFrame(moi)
    return df


def shortest_path(V, G, is_directed, start, end):
    matrix = adjacency_matrix(V, G, is_directed)
    for i in range(1, V):
        m = np.linalg.matrix_power(matrix, i)
        if m[start][end] != 0:
            return i
    return "Droga nie istnieje"


def connectivity(V, G):
    matrix = adjacency_matrix(V, G, False)
    c = [0] * V
    for v1 in range(V):
        for v2 in range(V):
            if matrix[v1][v2] != 0:
                c[v2] = 1
    for i in c:
        if i == 0:
            return "Graf nie spójny"
    return "Graf spójny"


def print_methods(V, G, is_directed, method):
    if method == 1:
        return lvk(V, G, is_directed)
    elif method == 2:
        return adjacency_matrix(V, G, is_directed)
    else:
        return incidence_matrix(V, G, is_directed)


V = 6
G = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 0), (0, 1)]

choose = str(input('Graf skierowany? [t/f]: '))
if choose == 't':
    is_directed = True
else:
    is_directed = False

for method in range(1, 4):
    print(print_methods(V, G, is_directed, method))
print('Najszybsza droga: ' + str(shortest_path(V, G, is_directed, 2, 1)))
print(connectivity(V, G))
