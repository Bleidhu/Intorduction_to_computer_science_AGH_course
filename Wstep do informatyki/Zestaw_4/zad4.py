import random

n = int(input())

t = [[random.randrange(1, 1000) for _ in range(n)] for _ in range(n)]

print(*t, sep="\n")


# iteracja po werszach
sum_of_columns = [0 for _ in range(n)]
sum_of_werses = [0 for _ in range(n)]

for i in range(n):
    for j in range(n):
        sum_of_columns[i] += t[j][i]
        sum_of_werses[i] += t[i][j]

max_div = sum_of_columns[0] / sum_of_werses[0]
werse = 0
column = 0

for i in range(n):
    for j in range(n):
        if sum_of_columns[i] / sum_of_werses[j] > max_div:
            max_div = sum_of_columns[i] / sum_of_werses[j]
            werse = j
            column = i

print(t[werse][column])
