from math import *
n = int(input())

diff = n - 1
divis = (1, n)
for i in range(2, isqrt(n) + 1):
    if(n%i == 0 and abs(i - n//i) < diff):
        diff = abs(i - n//i)
        divis = (i, n//i)

print(divis)