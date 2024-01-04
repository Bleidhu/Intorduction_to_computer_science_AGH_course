def zadanie(T, x):
    cnt = 0
    n = len(T)
    def rek(T, x, ilo=1, p=0):
        n = len(T)
        #print(p, ilo,  brane)
        nonlocal cnt

        if ilo == x:
            cnt += 1    
        if p == n:
            return
        else:
            rek(T, x , ilo, p + 1)
            rek(T, x , ilo * T[p], p + 1,)
    rek(
        T,
        x,
    )
    print(cnt)


zadanie([1, 3, 6], 18)
