def zad19(T):
    n = len(T)
    maxi=0
    for i in range(n-1):
        suma=T[i]
        cnt=1
        suma_ind=i
        if T[i] < T[i+1]:
            for j in range(i + 1, n):
                if not T[j - 1]<T[j]:
                    break
                else:
                    suma+=T[j]
                    suma_ind+=j
                    cnt+=1
                    if suma==suma_ind:
                        maxi=max(maxi,cnt)
    return maxi

print(zad19([1, 2, 1, 5, 6, 7, 7, 8, 4]))