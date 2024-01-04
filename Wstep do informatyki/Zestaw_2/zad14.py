n = input()
m = input()

counter = 0
def is_prime(n):
    while n > 0:


def dfs(get_from, current, i, j):
    a = i
    b = j
    if(i == len(n) and j == len(m)):
        print(current)
        if(int(current)%7 == )
        return
        pass
    elif get_from == 1:
        current += n[i]
        a += 1
    elif get_from == 2:
        current += m[j]
        b += 1
    if a != len(n):
        dfs(1, current,a,b)
    if b != len(m):
        dfs(2, current,a,b)
    
dfs(1, '', 0, 0)
dfs(2, '', 0, 0)