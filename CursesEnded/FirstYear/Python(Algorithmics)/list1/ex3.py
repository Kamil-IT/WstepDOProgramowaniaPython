import numpy as np


def create_random_matrix_marks(col, row):
    return np.random.randint(0, 100, size=(col, row))


def stepped_matrix(matrix):
    count_col, count_row = matrix.shape
    for row in range(count_row):
        for col in range(row + 1, count_col):
            if matrix[row, row] == 0:
                continue
            divisor = matrix[col, row] / matrix[row, row]
            for i in range(count_row):
                matrix[col, i] -= matrix[row, i] * divisor
    return matrix


matrix = create_random_matrix_marks(5, 15)
a, b = matrix.shape

print(stepped_matrix(matrix))
