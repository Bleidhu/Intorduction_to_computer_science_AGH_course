a,b,c = [int(i) for i in input().split(' ')]



#a,b = min(a,b), max(a,b)

while b > 0:
    a,b = b, a%b

nwdab = a



c, nwdab = min(c, nwdab), max(c, nwdab)

while nwdab > 0:
    c, nwdab = nwdab, c%nwdab



print(c)

