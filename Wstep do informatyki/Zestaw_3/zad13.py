import random
n = int(input())

t = [random.randrange(100, 1000) for _ in range(n)]
#t = [1,2,3,3,3,2,1]
#t = [2, 9, 3, 1, 7, 11, 9, 6, 7, 7, 1, 3, 9, 12, 15]
max_l = 1
n = len(t)
for i in range(n - 1):
    for j in range(n - 1, 0, -1):
        if(t[i] == t[j]):
            k = i + 1
            j -= 1
            l = 1
            while k < n and t[k] == t[j]:
                    l += 1
                    j -= 1
                    k += 1
            max_l = max(l, max_l)       

print(max_l)