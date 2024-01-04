def czynniki(n):
    i = 2
    ncp=n
    czynn = []
    while n > 1 and i < ncp:
        if(n%i == 0):
            czynn.append(i)
            while n%i == 0:
                n//=i
                print(n)
        i+=1
    return czynn

def rek(T, p=0, cnt=0):
    n=len(T)
    if(p == n-1):
        return cnt
    if(p > n-1):
        return -1
    else:
        czynn = czynniki(T[p])
        sk = -1
        for i in czynn:
            sk =  max(sk, rek(T, p+i, cnt+1))
        return sk
    
print(rek([6, 3, 2]))