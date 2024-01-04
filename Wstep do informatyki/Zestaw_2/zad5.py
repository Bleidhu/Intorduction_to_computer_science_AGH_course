from itertools import combinations
def rozbijanie(x):
    licznik = 1
    wynik = 0
    while licznik < len(x)+1:
        comb = combinations(x, licznik)
        for i in list(comb):
            num = "".join(i)
            if int(num) % 7 == 0:
                wynik += 1
        licznik += 1
    return wynik
    

def main():
    print(rozbijanie(input()))

if __name__ =="__main__":
    main()