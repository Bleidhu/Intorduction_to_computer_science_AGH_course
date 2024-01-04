def minor(A, i, j):
    n = len(A)
    n_new = n - 1
    a,b = 0, 0
    minor = [[0 for _ in range(n_new)] for _ in range(n_new)]
    for w in range(n):
        if(w == i):
            continue
        b = 0
        for k in range(n):
            if k == j:
                continue
            minor[a][b] = A[w][k]
            b+=1
        a+=1
    return minor

print(minor([[1,2,3],
             [4,5,6],
             [7, 8, 9]], 1, 1))

def wyznacznik(A):
    print(A)
    n = len(A)
    if n == 1:
        return A[0][0]
    else:
        det = 0
        for i in range(n):
            det += ((-1)**(i))*wyznacznik(minor(A, 0, i))*A[0][i]
        return det
    
print(wyznacznik([[11, 12, 14, 0],
                  [15, 17, 19, 1],
                  [10, 11, 12, 8],
                  [13, 11, 9, 14]]))