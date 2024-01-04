a0 = 0
a1 = 1
b0 = 2

war = True
while war:
    if(int(input()) == a0):
        print(b0)
        b0 = b0 +  2 * a0
        a0, a1 = a1, a1 - b0*a0
    else:
        break