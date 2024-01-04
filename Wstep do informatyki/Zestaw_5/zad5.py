import math


def prime_seq(T, a, b):
    n = len(T)
    power = 1
    sum_i = 0
    while b >= a:
        sum_i += T[b] * power
        power *= 2
        b -= 1

    if sum_i == 0 or sum_i == 1:
        return False
    for i in range(2, math.isqrt(sum_i) + 1):
        if sum_i % i == 0:
            return False
    return True


def rekursja(T, a, b):
    if b - a + 1 > 30:
        return False
    else:
        for i in range(a + 1, b):
            if a + 1 < b:
                if rekursja(T, a, i) and rekursja(T, i, b):
                    return True
        return False


print(prime_seq([1, 1, 0, 1, 0, 0], 0, 6 - 1))
