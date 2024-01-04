def jedynki(n):
    cnt = 0
    while n > 0:
        cnt += n%2
        n//=2
    return cnt

def zadanie(T):
    n = len(T)
    for i in range(n):
        T[i] = jedynki(T[i])
    
    def rek(T, s1=0,s2=0,s3=0, p=0):
        if(p == n):
            return s1 == s2 == s3
        else:
            return rek(T, s1+T[p], s2, s3, p+1) or rek(T, s1, s2 + T[p], s3, p+1) or rek(T, s1, s2, s3+T[p], p+1)
    
    print(rek(T))

zadanie([5,7,15])