n = int(input())

t = []

def prime_divisors(n):
    i = 2
    divisors = []
    n2 = n
    while n2 > 0:
        if(n%i == 0):
            n2//=i
            divisors.append(i)
        else:
            i += 1
    return divisors


for _ in range(n):
    tmp = int(input())
    t.append(tmp)

vis = [0 for _ in range(n)]

vis[0] = 1

for i in range(n - 1):
    if(vis[i] == 1):
        for j in prime_divisors(t[i]):
            if(i + j < n):
                vis[i + j] = 1

print(vis[n-1])

        