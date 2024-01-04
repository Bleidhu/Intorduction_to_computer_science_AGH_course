import random
n = int(input())
t = []

for i in range(1, n):
    t.append(random.randrange(1, 1001))

req = False
for i in t:
    i2 = i
    count = 0
    while(i2 > 0):
        digit = i2%10
        if(digit%2 == 0):
            break
        i2 //= 10
    else:
        req = True
        break

print(t)
print(req)