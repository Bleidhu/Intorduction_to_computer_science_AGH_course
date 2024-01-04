def pole(sq):
    return((sq[1]-sq[0])*(sq[3]-sq[2]))
def przec(T, w, p):
    for i in range(len(w)):
        if(w[i] and ((T[i][0]<=T[p][0]<=T[i][1] or T[i][0]<=T[p][1]<=T[i][1]) and 
                     (T[i][2]<=T[p][2]<=T[i][3] or T[i][2]<=T[p][3]<=T[i][3]))):
            return True
    return False
            
def rek(T, wziete, p=0, pl = 0,n = 0):
    if(n == 2):
        return pl == 8
    if(p == len(T)):
        return False
    else:
        a = rek(T, wziete, p+1, pl, n)
        
        if(not przec(T, wziete, p)):
            wziete[p] = True
            b = rek(T, wziete, p + 1, pl + pole(T[p]), n+1)
            wziete[p] = False
        return a or b
print(rek([(1, 3, 1, 3),(5, 7, 5, 7)], [False, False]))