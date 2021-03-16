def recurrent_algorithm_1(n):
    if n == 0:
        return 0
    return 3 ^ n + recurrent_algorithm_1(n - 1)


def recurrent_algorithm_2(n):
    if n == -1 or n == 0:
        return 0
    return n + recurrent_algorithm_2(n - 2)


def recurrent_algorithm_3(n):
    if n == 1 or n == 0:
        return n
    return recurrent_algorithm_3(n - 1) + recurrent_algorithm_3(n - 2)


print(recurrent_algorithm_1(10))
print(recurrent_algorithm_2(10))
print(recurrent_algorithm_3(10))
