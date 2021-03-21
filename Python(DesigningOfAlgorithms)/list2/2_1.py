def recurrent_algorithm_1(n):
    if n == 0:
        return 0
    return 3 ** n + recurrent_algorithm_1(n - 1)


def recurrent_algorithm_2(n):
    if n == -1 or n == 0:
        return 0
    return n + recurrent_algorithm_2(n - 2)


def recurrent_algorithm_3(n):
    if n == 1 or n == 0:
        return n
    return recurrent_algorithm_3(n - 1) + recurrent_algorithm_3(n - 2)


def analytical_algorithm_1(n):
    return sum([3 ** i for i in range(1, n + 1)])


def analytical_algorithm_2(n):
    if n % 2 == 0:
        range_ = (int(n / 2) + 1)
    else:
        range_ = int((n + 1) / 2) + 1
    return sum([n - 2 * (i - 1) for i in range(1, range_)])


def analytical_algorithm_3(n):
    a = (1 + 5 ** 0.5) / 2
    b = (1 - 5 ** 0.5) / 2
    return int(1 / (5 ** (1 / 2)) * (a ** n - b ** n))


N = 11
for n in range(N):
    print(str(n) + " Test for algorithm 1 go correctly: " + str(analytical_algorithm_1(n) == recurrent_algorithm_1(n)))
    print(str(n) + " Test for algorithm 2 go correctly: " + str(analytical_algorithm_2(n) == recurrent_algorithm_2(n)))
    print(str(n) + " Test for algorithm 3 go correctly: " + str(analytical_algorithm_3(n) == recurrent_algorithm_3(n)))
