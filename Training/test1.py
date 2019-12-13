import unittest
import numpy


def findDet(a):
    return int(numpy.linalg.det(a))


class Tests(unittest.TestCase):
    new_array = [[1, 2, 3], [3, 6, 7], [9, 9, 9]]

    def testIsNumber(self):
        for row in self.new_array:
            for col in row:
                """
                try:
                    assert isinstance(col, (int, float)), 'Zły typ danych w macierzy'
                except AssertionError as message:
                    print(message)
                """
                self.assertIsInstance(col, (int, float))

    def testSize(self):
        col_counter = 0
        row_counter = 0
        for row in self.new_array:
            for col in row:
                col_counter += 1
            row_counter += 1

        self.assertEqual(col_counter/row_counter, row_counter)

    def testReturnCorrect(self):
        self.a = numpy.array(self.new_array)
        self.assertAlmostEqual(findDet(self.a), -18)


if __name__ == '__main__':
    unittest.main()