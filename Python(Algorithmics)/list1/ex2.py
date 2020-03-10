import numpy as np


def create_random_matrix_marks(stud_quantity, sub_quantity):
    return np.random.choice(np.arange(2., 6., 0.5), size=(stud_quantity, sub_quantity))


rows = 4
columns = 4

matrix1 = create_random_matrix_marks(rows, columns)
matrix2 = create_random_matrix_marks(rows, columns)

symmetric_length = 0
for row in range(0, rows):
    for col in range(0, columns):
        symmetric_length += abs(matrix1[row, col] - matrix2[row, col])

print(symmetric_length)