from sys import maxsize
from itertools import permutations


def travelling_salesman_problem(matrix_route):
    vertex = [i for i in range(1, len(matrix_route))]

    min_ = maxsize
    for current_permut in permutations(vertex):
        current_cost = 0

        k = 0
        for j in current_permut:
            current_cost += matrix_route[k][j]
            k = j
        # We have to comeback
        current_cost += matrix_route[k][0]

        min_ = min(min_, current_cost)

    return min_


if __name__ == "__main__":
    matrix_route_symmetrical = [[0, 254, 331, 842, 2396],
                                [254, 0, 324, 1093, 2136],
                                [331, 324, 0, 1137, 2180],
                                [842, 1093, 1137, 0, 1616],
                                [2396, 2136, 2180, 1616, 0]]
    matrix_route_non_symmetrical = [[0, 25, 43, 31],
                                    [2, 0, 54, 33],
                                    [1, 25, 0, 43],
                                    [20, 25, 1, 0]]

    print(travelling_salesman_problem(matrix_route_symmetrical))
    print(travelling_salesman_problem(matrix_route_non_symmetrical))
