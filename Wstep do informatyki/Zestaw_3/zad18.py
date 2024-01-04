import random

n = 5

# t = [random.randrange(1, 10000) for _ in range(n)]

t = [2, 2, 4, 6, 8]
max_len = 0
for i in range(n):
    for j in range(n - 1, i - 1, -1):
        if t[j] % 2 == 1 and t[j] == t[i]:
            k = i + 1
            l = j - 1
            while k < l and t[k] % 2 == 1 and t[k] == t[l]:
                k += 1
                l -= 1
            if k == l or k == l + 1 or j == i:
                max_len = max(j - i + 1, max_len)
print(max_len)
