import unittest
from math import sqrt

import numpy
import scipy
from scipy import linalg


class test(unittest.TestCase):
    matrix_array = [[1, 2, 3], [3, 6, 7], [9, 9, 9]]
    matrix = scipy.array(matrix_array)

    def testMatrixHaveNumbers(self):
        for row in self.matrix_array:
            for column in row:
                self.assertIsInstance(column, (int, float))

    def testMatrixIsSquare(self):
        count_shape = self.matrix.shape.count(sqrt(self.matrix.size))
        self.assertEqual(count_shape, 2)

    # Do poprawy
    def testLUMatrixDeterminant(self):
        I, L, U = linalg.lu(self.matrix)
        detI = linalg.det(I)
        detL = linalg.det(L)
        detU = linalg.det(U)
        det_all = linalg.det(self.matrix)
        self.assertEqual(det_all, detI * detU * detL)

    def testDeterminant(self):
        self.assertEqual(numpy.linalg.det(self.matrix_array), -18.000000000000014)


if __name__ == "__main__":
    unittest.main()
