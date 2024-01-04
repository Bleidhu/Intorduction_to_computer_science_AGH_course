import math
def czy_pierwsza(n):
    i = 2
    if(n == 1 or n == 0):
        return False
    while i <= math.sqrt(n):
        if(n%i == 0):
            return False
        i += 1
        #end if
    #end while

    return True

def liczba_roznocyfrowa_z_a(a, i, j, n):
    dziel = 10**(n - j) # daje nam j=tą cyfrę od końca przy dzieleniu modulo

    wyst_cyfry = [0 for _ in range(10)]

    liczba = 0

    pow10 = 1
    a //= dziel
    while pow10 < 10**i:
        cyfra = a%10
        a //= 10

        wyst_cyfry[cyfra] += 1

        if(wyst_cyfry[cyfra] > 1):
            return (False, -1)
        
        liczba += cyfra*pow10
        pow10 *= 10
    
    return (True, liczba)

def main():
    a = int(input())

    n = math.floor(math.log10(a)) + 1

    max_roznocyfr_pierw = 0

    for i in range(1, n):
        if((a//10**i)%10 == 0):
            continue
        for j in range(min(i + 9, n), i - 1, -1):
            #f zwracająca liczbę wynikającą z obcięcia a do i tej pozycji z przodu i j z tyłu
            czy_roznocyfr, liczba = liczba_roznocyfrowa_z_a(a, i, j, n)

            if(not czy_roznocyfr):
                continue

            if(czy_pierwsza(liczba)):
                max_roznocyfr_pierw = max(liczba, max_roznocyfr_pierw)

    print(max_roznocyfr_pierw)

if __name__ == '__main__':
    main()