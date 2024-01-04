import math
def zlozona(x):
    a = 2
    while a < math.isqrt(x):
        if x%a == 0 and x!=a:
            return True
        a+=1
    return False
def zadanie(A, B):
    cnt = 0
    def rekurencja(x, A, B):
        if(A == 0 and B == 0):
            if(zlozona(x)):
                nonlocal cnt
                cnt += 1
                print(format(x, 'b'))
            return
        else:
            if(A>0):
                rekurencja(x*2 + 1, A - 1, B)
            if(B>0):
                rekurencja(x*2, A, B - 1)
            return
    rekurencja(1, A-1, B)
    return(cnt)

print(zadanie(2, 3))