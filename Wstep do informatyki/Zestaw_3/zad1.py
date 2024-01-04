x = int(input())
base = int(input())

a = []
while x > 0:
    a.append(str(x%base))
    x //= base
a.reverse()
for i in a:
    print(i, end="")
print()