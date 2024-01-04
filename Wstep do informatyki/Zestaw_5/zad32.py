def zadanie(T, k):
    def rek(T, k, sum1=0, sum2=0, p=0, cnt1=0, cnt2=0):
        n = len(T)

        if(k == cnt1 == cnt2 and sum1==sum2):
            return True
        if(p == n or cnt1 > k or cnt2 > k):
            return False
        else:
            return (rek(T, k, sum1, sum2, p + 1, cnt1, cnt2) or
            rek(T, k, sum1 + T[p], sum2, p+1, cnt1+1, cnt2)
            or rek(T, k, sum1, sum2+T[p], p+1, cnt1, cnt2+1))
        
    print(rek(T, k))

zadanie([1, 1, 1, 1], 2)