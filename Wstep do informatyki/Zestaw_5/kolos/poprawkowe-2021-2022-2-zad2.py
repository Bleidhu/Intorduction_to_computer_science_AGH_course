from math import *
def is_prime(a):
    if a == 2 or a == 3:
        return True
    if a % 2 == 0 or a % 3 == 0 or a == 1:
        return False
    
    i = 6
    while i <= sqrt(a):
        if a % (i-1) == 0 or a % (i+1) == 0:
            return False
        i += 6

    return True


def zad2(T):
    def rek(T, i, szt):
        n = len(T)
        if( i == n and szt == 0):
            return n
        elif(i==n):
            return -1
        else:
            cnt = szt - 6

            for j in range(cnt, szt+1, 1):
                print(i, j, T[i] + j, szt - j)
                if(100 >= T[i]+j >= 0 and szt - j >= 0 and is_prime(T[i] + j) and rek(T, i + 1, szt - j) == n):
                    return n
            return i
    print(rek(T, 0, 0) == len(T))

zad2([10, 20, 30])