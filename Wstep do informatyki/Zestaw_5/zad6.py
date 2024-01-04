def zadanie(T):
    mincnt = len(T)
    suma = 0

    def rek(T, sel=0, si=0, p=0, cnt=0):
        n = len(T)
        nonlocal mincnt
        nonlocal suma
        if sel == si and 0 < cnt < mincnt:
            suma = sel
            mincnt = cnt
        if p == n:
            return
        else:
            rek(T, sel, si, p + 1, cnt)
            rek(T, sel + T[p], si + p, p + 1, cnt + 1)

    rek(T)
    print(suma, mincnt)


zadanie([1, 0, 7, 8, 5, 11, 2])
