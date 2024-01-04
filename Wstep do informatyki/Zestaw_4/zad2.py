import random

n = int(input())

t = [[random.randrange(1, 1000) for _ in range(n)] for _ in range(n)]

print(t)


# iteracja po werszach
werse_with_onlyodddigited = 0
for i in t:
    counter = 0
    for j in i:
        toggle = True
        while j > 0:
            if j % 10 % 2 == 0:
                toggle = False
                break
            j //= 10
        if toggle:
            counter += 1
    if counter > 0:
        werse_with_onlyodddigited += 1
if werse_with_onlyodddigited == n:
    print("TAK")
else:
    print("NIE")
