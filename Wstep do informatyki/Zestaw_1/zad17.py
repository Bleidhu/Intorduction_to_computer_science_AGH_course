a = 4
b = 7
iloraz = 1
lastIloraz = -1
while abs(iloraz - lastIloraz) > 0.1**9:
    a,b = b, a + b
    lastIloraz, iloraz = iloraz, a / b
print(iloraz)