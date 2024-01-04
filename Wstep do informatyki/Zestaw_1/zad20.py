from math import *
a = int(input())
b = int(input())

while abs(a - b) > 0.0001:
    a, b = sqrt(a * b), (a + b)/2


print((a+b)/2)