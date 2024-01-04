def square(T):
    n = len(T)
    for b in range(2, n):
        for i in range(n - b + 1):
            for j in range(n - b + 1):
                liczba = T[i][j] * T[i + b - 1][j] * T[i][j + b - 1] * T[i + b - 1][j + b - 1]

                if(ile_czynnikow(liczba) == 2):
                    return b
    return 0

def ile_czynnikow(a):
    cnt = 0

    d = 2

    while a!=1:
        if a%d == 0 : cnt+=1

        while a%d==0:
            a//=d
        
        d += 1
    return cnt


print(square([[2, 2, 3, 4],
              [2, 2, 3, 2],
              [2, 2, 2, 2],
              [2, 2, 2, 2]]))