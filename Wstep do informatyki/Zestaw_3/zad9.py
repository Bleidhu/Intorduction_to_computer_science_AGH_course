
n = int(input())
t = []

for _ in range(n):
    tmp = int(input())
    t.append(tmp)


max_len = 1
curr = 1
for i in range(1, len(t)):
    if(t[i] > t[i - 1]):
        curr += 1
    else:
        max_len = max(max_len, curr)
        curr = 1
max_len = max(max_len, curr)
print(max_len)