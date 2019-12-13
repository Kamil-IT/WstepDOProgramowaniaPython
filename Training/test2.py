"""
Żeby  to gówno działało trzeba pobrać najpierw:
https://go.microsoft.com/fwlink/?LinkId=691126
Potem na Windowsie trzeba wpierdolić w cmd:
python -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose
Jak się to wykona, to zajebiście
Potem w PyCharmie klikacie File->Settings->Project Interpreter->rozwijacie liste->show all-> + -> zmieniacie na 'System Interpreter'
Z listy wybieracie ściężkę do pythona zainstalowanego na waszym kompie i git wszystko powinno już działać
"""

from scipy import linalg
import numpy as np
import unittest


def methodLU(A):
    P, L, U = linalg.lu(A)
    return P, L, U


def findDet(A):
    return np.linalg.det(A)


class Tests(unittest.TestCase):
    new_matrix = [[1, -1, 2], [3, 0, -4], [2, 3, 5]]
    A = np.array(new_matrix)

    def testIsNumber(self):
        for row in self.new_matrix:
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
        for row in self.new_matrix:
            for col in row:
                col_counter += 1
            row_counter += 1
        self.assertEqual(col_counter/row_counter, row_counter)

    def testDet(self):
        normal_det = findDet(self.A)
        self.assertAlmostEqual(normal_det, 53)  # wedlug kalkulatora macierzy powinno by 53

    def testDetsLU(self):
        P, L, U = methodLU(self.A)
        print('Macierze P, L i U: ')
        print('-------------------------------')
        print(P)
        print('-------------------------------')
        print(L)
        print('-------------------------------')
        print(U)
        print('-------------------------------')
        normal_det = findDet(self.A)
        # det(A) = det(P * L * U) = det(P) * det(L) * det(U)
        LU_det = findDet(P) * findDet(L) * findDet(U)
        print(f'det(A) = {normal_det}')
        print(f'det(A) = det(P * L * U) = det(P) * det(L) * det(U)')
        print(f'{findDet(P)} * {findDet(L)} * {findDet(U)} = {LU_det}')
        self.assertAlmostEqual(normal_det, LU_det)