num = input()
n = len(num)

counter = 0
for s in range(1, 1 << n):
    tmp = ""
    for i in range(n):
        if((s & (1 << i)) > 0):
            tmp = tmp + num[i]

    if(tmp == ''):
        tmp = '0'
    if(int(tmp)%7 == 0):
        counter += 1

print(counter)