from math import sqrt

import numpy


def matrix_determinant(matrix):
    return numpy.linalg.det(matrix)


matrix = numpy.array([[1, 1, 1, 1], [2, 4, 6, 6], [2, 1, 9, 6], [2, 1, 9, 2]])
print(matrix_determinant(matrix))


