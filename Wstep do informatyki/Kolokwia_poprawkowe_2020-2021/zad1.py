def nwd(a, b):
    if a == 0 or b == 0:
        return(1)
    while b > 0:
        a, b = b, a%b
    return a

def podziel(a, b):
    x, y = a[0]*b[1], a[1]*b[0]

    if(y < 0 and x < 0):
        x*=-1
        y*=-1
    elif y < 0 and x >= 0:
        y*= -1
        x*=-1

    nwd_xy = nwd(x, y)

    return (x//nwd_xy, y//nwd_xy)

def longest(T):
    n = len(T)

    if T[0][0] == 0:
        q = (0, 0)
    else:
        q = podziel(T[1], T[0])
        print(q)
    max_len = 2
    curr_len = 2

    i = 2

    while i < n:
        if T[i - 1][0] == 0:
            if T[i][0] == 0  and q == (0, 0):
                curr_len += 1
                print("0", i, curr_len, max_len, q)
                max_len = max(curr_len, max_len)
            else:
                curr_len = 2
                q = (0, 0)
        else:
            tmp = podziel(T[i], T[i - 1])
            if(tmp ==  q):
                curr_len += 1
                print("1", i, curr_len, max_len, q)
                max_len = max(curr_len, max_len)
            else:
                q = tmp
                curr_len = 2
        i += 1
    
    return max_len

print(longest(  [(1,2),(2,3),(3,4),(4,5),(5,6)] ))