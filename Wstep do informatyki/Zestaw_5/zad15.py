w = [True for _ in range(8)]
c = [True for _ in range(8)]

cnt_comb = 0
def hetmani(w, c, cnt=0):
    if(cnt==8):
        global cnt_comb
        cnt_comb += 1
        return
    else:
        for i in range(8):
            if(not w[i]):
                continue
            for j in range(8):
                if(not c[j]):
                    continue
                wn = [x for x in w]
                cn = [x for x in c]
                wn[i] = False
                cn[j] = False
                print(i, j, cnt_comb, cnt)
                hetmani(wn, cn, cnt+1)
hetmani(w, c)