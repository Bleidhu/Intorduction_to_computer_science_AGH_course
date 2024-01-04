liczba = int(input())
a = 1
b = 1
is_in_fib = False
while a < liczba:
    an = 1
    bn = 1
    while an < liczba:
        if a*an == liczba:
            print('TAK', an, a)
            is_in_fib = True
            break
        an, bn = bn, an + bn
    if(is_in_fib):
        break
    a, b = b, a + b
if(not is_in_fib):
   print('NIE')
        