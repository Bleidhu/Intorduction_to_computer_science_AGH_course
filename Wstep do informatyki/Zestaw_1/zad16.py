def ile_operacji(n):
    op = 0
    a = n
    while a != 1:
        a = (a % 2)*(3*a + 1) + (1 - a %2)* a/2
        op += 1
    
    return op

maxNum = 2
ops = ile_operacji(2) 
for i in range(3, 10001):
    a = ile_operacji(i)
    if(a > ops):
        ops = a;
        maxNUm = i

print(maxNum)