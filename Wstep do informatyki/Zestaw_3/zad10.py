
n = int(input())
t = []

for _ in range(n):
    tmp = int(input())
    t.append(tmp)


max_len = 2
curr = 2
r = t[1] - t[0]
for i in range(2, len(t)):
    if(t[i] - t[i - 1] == r):
        curr += 1
    else:
        max_len = max(max_len, curr)
        curr = 2
        r = t[i] - t[i - 1]
max_len = max(max_len, curr)
print(max_len)