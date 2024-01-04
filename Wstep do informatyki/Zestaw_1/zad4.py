n = int(input())

a = 1
sum_num = 0
count = 0
while sum_num + a <= n:
    sum_num += a
    count += 1
    a += 2

print(count)