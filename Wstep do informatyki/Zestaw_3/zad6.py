import random
n = int(input())
t = []

for i in range(1, n):
    t.append(random.randrange(1, 1001))

req = True
for i in t:
    i2 = i
    count = 0
    while(i2 > 0):
        digit = i2%10
        if(digit%2 == 1):
            count += 1
            break
        i2 //= 10
    if(count == 0):
        print(i)
        req = False
        break

print(t)
print(req)