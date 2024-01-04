def zadanie31(n):
    podz = []

    i = 2
    while(n > 1):
        if(n%i == 0):
            podz.append(i)
            while n%i == 0 and n > 1:
                n//=i
        i += 1
    sum_p = 0
    def rek(podz, p, multip = 1, cnt = 0):
        n = len(podz)
        if(p==n):
            nonlocal sum_p
            if(cnt != 0):
                sum_p += multip
        else:
            rek(podz, p + 1, multip, cnt)
            rek(podz, p + 1, multip*podz[p], cnt + 1)
    rek(podz, 0)
    print(sum_p)

zadanie31(15)
