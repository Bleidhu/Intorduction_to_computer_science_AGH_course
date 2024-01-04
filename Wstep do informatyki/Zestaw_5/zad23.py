def rek(T, s, p, war, cnt=0):
    n = len(T)
    if(s == war and cnt == 3):
        return True
    if(p == n or cnt == 3):
        return False
    else:
        return rek(T, s, p+1, war, cnt) or rek(T, (s*T[p])/(s+T[p]), p+1, war, cnt + 1)
    
