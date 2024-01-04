import random 

def szukaj_ciagu(t, n):
    i = 0
    while i < n - 2:
        j = 2
        while i + 2*j + 1 < n:
            multip = t[i]/t[i + j + 1]
            flag = True
            for k in range(i + 1, i + j + 1):
                if(t[k]/t[k + j + 1] != multip):
                    flag = False
            if(flag):
                return (i, i + j)
            j += 1
        i += 1
    return (-1, -1)

def main():
    t =  [2,5,7,3,2,3,5,7,6,9,15,21,17,19,23,2,6,4,8,3,5,7,1,3,2]
    n = len(t)

    print(szukaj_ciagu(t, n))

if __name__ == '__main__':
    main()