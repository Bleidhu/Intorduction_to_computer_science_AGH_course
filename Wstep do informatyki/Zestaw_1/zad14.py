x = float(input())

currentFactorial = 1
n = 1
s = 0
last = 1

s += 1

while abs(last) > 0.0001:
    currentFactorial *= 2*n * (2*n - 1)

    last = (((-1)**n)/currentFactorial) * x**(2*n)

    s += last

    n += 1

    print(last, s)

print(s)

