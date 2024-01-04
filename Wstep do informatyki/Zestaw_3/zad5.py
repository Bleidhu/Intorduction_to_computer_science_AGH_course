seq = []

inpt = input()

while(inpt != "0" ):
    seq.append(inpt)
    inpt = input()


tab = [0 for i in range(10)]

for i in seq:
    index = 0
    while(index < len(tab) and tab[index] < int(i)):
        index += 1
    index -= 1

    if(index != -1):
        for j in range(0, index):
            tab[j] = tab[j + 1]
    tab[index] = int(i)

print(tab[0])


