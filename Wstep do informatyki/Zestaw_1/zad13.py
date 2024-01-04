a,b,c = [int(i) for i in input().split(' ')]

iloczynab = a*b
ckopia = c


a,b = min(a,b), max(a,b)

while b > 0:
    a,b = b, a%b


nwdab = a

nwwab = iloczynab//nwdab

iloczynab //= nwdab
 

c, iloczynab = min(c, iloczynab), max(c, iloczynab)

while iloczynab > 0:
    c, iloczynab = iloczynab, c%iloczynab



print((nwwab * ckopia)//c)

