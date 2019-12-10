import pprint
import scipy
import scipy.linalg

A = scipy.array([[7, 3, -1, 2], [3, 8, 1, -4], [-1, 1, 4, -1], [2, -4, -1, 6]])
I, L, U = scipy.linalg.lu(A)

print(L)
print()
print(U)



# 4 ZAŁOŻENIA
