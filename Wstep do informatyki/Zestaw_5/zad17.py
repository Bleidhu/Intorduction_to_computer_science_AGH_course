import math
def is_prime(x):
    a = 2
    if(x == 0 or x == 1):
        return False
    while a <= math.isqrt(x):
        if x%2 == 0:
            return False
        a += 1
    return True

def zadanie(x, y):
    n = math.floor(math.log10(x)) + 1
    m = math.floor(math.log10(y)) + 1

    cnt = 0

    def rekurencja(x, y, suma, a, b, n, m):
        nonlocal cnt
        if(is_prime(suma)):
            cnt += 1
            print(suma)
            return
        if(a==n and b == m):
            return
        else:
            if(a < n):
                cyfra_x = ((x%(10**(n - a)))//(10**(n - a - 1)))
                rekurencja(x, y, suma*10 + cyfra_x, a + 1, b, n, m)
            if(b < m):
                cyfra_y = ((y%(10**(m - b)))//(10**(m - b - 1)))
                rekurencja(x, y, suma*10 + cyfra_y, a, b+1, n, m)
    rekurencja(x, y, 0, 0, 0, n, m)
    return cnt

print(zadanie(123, 75))