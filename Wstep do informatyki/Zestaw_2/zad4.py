from math import *
n = int(input())

def czy_liczba_jest_dtp(n):
    for i in range(4,n):
        if(n%i == 0 and i != 5):
            return False
    return True

s = 1

for i in range(2, n + 1):
    if(czy_liczba_jest_dtp(i)):
        s += 1
print(s)
