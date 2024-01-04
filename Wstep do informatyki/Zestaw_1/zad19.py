prec = 0

suma = 0
siln = 1
liczba = 1
while 1/siln > prec:
    print(1/siln, suma)
    suma += 1/siln
    siln *= liczba
    liczba += 1
print(suma)