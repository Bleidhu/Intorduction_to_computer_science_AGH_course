n = int(input())
a = 1
b = 1
curr = 0
while curr < n:
    curr += a
    a,b = b, a + b

if(curr == n):
    print("TAK")
else:
    an = 1
    bn = 1
    
    while curr > n:
        curr -= an
        an, bn = bn, an + bn
    
    if(curr == n):
        print("TAK")
    else:
        print("NIE")