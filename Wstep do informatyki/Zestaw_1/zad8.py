from math import sqrt
n = int(input())

x = 2

while x <= sqrt(n):
    if(n%x == 0):
        print("NIE")
        break
    x += 1
else:
    print("TAK")