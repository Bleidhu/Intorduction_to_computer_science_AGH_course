from math import *
def divisors_sum(number):
    sum = 1
    for i in range(2, isqrt(number)):
        if(number%i == 0):
            sum += i + number//i
    
    if(isqrt(number)**2 == number):
        sum += isqrt(number)
    return sum

for i in range(2, 10**6):
    j = divisors_sum(i)
    if(divisors_sum(j) == i and i != j and i < j):
        print(i, j)

