s = float(input())

a = 1
last = 0

while abs(a - last) > 1e-10:
    last = a
    a = (s/(last**2) + 2*last)/3
print(a)