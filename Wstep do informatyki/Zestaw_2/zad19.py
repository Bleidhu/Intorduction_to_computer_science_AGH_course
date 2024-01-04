a = int(input())
b = int(input())

print(a//b, end=".")
a = a%b

digits = [0 for i in range(10)]

period = ''
full = ''

while True:
    a*= 10
    full += str(a//b)
    if(digits[a//b - 1] > 2):
        break
    elif(digits[a//b - 1] > 1):
        period += str(a//b)
        digits[a//b - 1] += 1
    else:
        digits[a//b - 1] += 1    
    a = a%b

for i in full:
    if(digits[int(i) - 1] == 1):
        print(i, end = "")
print("(" + period + ")")

