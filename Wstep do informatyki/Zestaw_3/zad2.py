a = int(input())
b = int(input())

aDigits = [0 for _ in range(10)]
bDigits = [0 for _ in range(10)]

while a > 0:
    aDigits[a%10] += 1
    a//= 10

while b > 0:
    bDigits[b%10] += 1
    b //= 10

if(aDigits == bDigits):
    print("TAK")
else:
    print("NIE")
