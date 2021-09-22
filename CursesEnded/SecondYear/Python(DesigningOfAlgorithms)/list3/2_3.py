import random

import sympy


def is_prime_fermat_test(number, check_quantity):
    for i in range(check_quantity):
        q = sympy.randprime(2, number)
        if (q ** (number - 1) % number) != 1:
            return False
    return True


def is_prime_miller_rabin_test(p, k):

    # Find q and r
    r = 0
    q = p - 1
    while q % 2 == 0:
        r += 1
        q = q // 2

    for _ in range(k):
        a = random.randrange(2, p - 1)
        x = a ** q % p
        if x == 1 or x == p - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, p)
            if x == p - 1:
                break
        else:
            return False
        break
    return True


print(is_prime_fermat_test(23, 7))
print(is_prime_miller_rabin_test(23, 7))
