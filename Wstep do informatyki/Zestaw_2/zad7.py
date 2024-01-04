from math import *
x = int(input())

def is_part_of_seq(x):
    if ( 4*x - 3 >= 0 and isqrt(4*x - 3)*isqrt(4*x - 3) == 4*x - 3 and isqrt(4*x - 3)%2 == 1):
        return True
    else:
        return False
#an = n*n + n + 1
#n^2 + n + 1
#x = n^2 + n + 1
#delta = n^2 +n + 1 - x
# jezeli 1 + 1 + x >=  0 and sqrt(1 + 1 + x) in Z to wtedy jezeli (-1 +- isqrt(x + 2))//2 in Z to mamy rozwo

for i in range(2, isqrt(x)+1):
    if(is_part_of_seq(i) or is_part_of_seq(x//i)):
        print("TAK")
        break
