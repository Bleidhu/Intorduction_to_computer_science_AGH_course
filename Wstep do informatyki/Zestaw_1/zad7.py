n = int(input())

a = 1
b = 1

while a*b < n:
    a,b = b, b+a

if(a*b == n):
    print('TAK')
else:
    print('NIE')