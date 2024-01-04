import random

n = int(input())

t = []

for _ in range(n):
    t.append(2*random.randint(0, 49) + 1)


curr = 2
max_len_plus = 2
max_len_minus = 2
r = t[1] - t[0]
for i in range(2, n):
    if(t[i] - t[i - 1] == r):
        curr+=1
    else:
        if(r > 0):
            max_len_plus = max(max_len_plus, curr)
            curr = 2
            r = t[i] - t[i - 1]
        else:
            max_len_minus = max(max_len_minus, curr)
            curr = 2
            r = t[i] - t[i - 1]

if(r > 0):
    max_len_plus = max(max_len_plus, curr)
else:
    max_len_minus = max(max_len_minus, curr)

print(t, max_len_minus, max_len_plus)