a = int(input())
b = int(input())
n = int(input())

print(a//b, end=".")
a = a%b

for i in range(1 ,n+1):
    a*= 10
    print(a//b, end="")
    a = a%b