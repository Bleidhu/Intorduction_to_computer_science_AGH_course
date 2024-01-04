def waga(n):
    i = 2
    cnt = 0
    while n > 1:
        if(n%i == 0):
            cnt += 1
            while n%i == 0:
                n//=i
        i+=1
    return cnt

def zad(T):
    n = len(T)
    for i in range(n):
        T[i] = waga(T[i])

    def rek(T, s1=0, s2=0, s3=0, p=0):
        if(p == n):
            return s1==s2==s3
        else:
            return(rek(T, s1+T[p], s2, s3, p+1) or rek(T, s1, s2+T[p], s3, p+1) or rek(T, s1, s2, s3 + T[p], p+1))
        
    return(rek(T))

print(zad([6, 3, 5]))