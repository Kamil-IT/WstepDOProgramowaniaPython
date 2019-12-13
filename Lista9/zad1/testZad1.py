import unittest
from math import sqrt

import numpy

from github.WstepDOProgramowaniaPython.Lista9.zad1.zad1 import matrix_determinant


class TestMatrix(unittest.TestCase):
    # Wprowadzany macierz
    matrix_example = [[1, 2, 3], [3, 6, 7], [9, 9, 9]]

    def testMatrixHaveNumbers(self):
        for row in self.matrix_example:
            for column in row:
                self.assertIsInstance(column, (int, float))

    def testMatrixIsSquare(self):
        matrix = numpy.array(self.matrix_example)
        self.assertEqual(matrix.shape.count(sqrt(matrix.size)), 2)

    def testCorrectResults(self):
        self.assertEqual(matrix_determinant(self.matrix_example), -18.000000000000014)


if __name__ == "__main__":
    unittest.main()
