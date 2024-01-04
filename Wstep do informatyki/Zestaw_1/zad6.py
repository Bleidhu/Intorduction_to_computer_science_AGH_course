a = 1
b = 10
mid = (a + b)/2

eps = 0.0001

while abs(b - a) > eps:
    if(mid**mid < 2023):
        a = mid
    elif(mid**mid > 2023):
        b = mid
    else:
        print(mid)
        break
    mid = (a + b)/2

print(mid)