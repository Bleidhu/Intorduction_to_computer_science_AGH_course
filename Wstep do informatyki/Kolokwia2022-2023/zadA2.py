def szukaj_w_ciagu(a, b):
    while a > 1:
        b, a = a, b - a + 1
    return a == 1, b == 0

def zadA2(T):
    n = len(T)
    for kol in range(n - 2):
        for i in range(n-2-kol):
            a=T[i][kol+i]
            b = T[1 + i][kol + i + 1]
            c = T[i + 2][kol + i + 2]

            if a+b == c + 1 and szukaj_w_ciagu(a, b):
                cnt = 3
                while a+b == c+1 and i < n-2-kol:
                    cnt += 1
                    i += 1
                return cnt

