def zadanie(T, x):
    cnt = 0
    n = len(T)
    def rek(T, x, brane, ilo=1, p=0):
        n = len(T)
        #print(p, ilo,  brane)
        nonlocal cnt

        if ilo == x:
            cnt += 1
            for i in range(n):
                if(brane[i]):
                    print(T[i], end=' ')
            print()
        if p == n:
            return
        else:
            rek(T, x, brane , ilo, p + 1)
            brane[p] = True
            rek(T, x, brane, ilo * T[p], p + 1,)
            brane[p] = False
    brane = [False for _ in range(n)]
    rek(
        T,
        x,
        brane
    )
    print(cnt)


zadanie([1, 3, 6], 18)
