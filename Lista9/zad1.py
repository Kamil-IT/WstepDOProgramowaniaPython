from cmath import sqrt

import numpy


def matrix_determinant(matrix):
    return numpy.linalg.det(matrix)


matrix = numpy.array([[1, 1, 1], [2, 4, 6], [2, 1, 9]])
print(matrix_determinant(matrix))
