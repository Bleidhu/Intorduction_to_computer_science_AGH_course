k = int(input())
a = 1
b = k
n = 100
x = (b-a)/n
#1 i x ograniczają obszar
mid = a + (b - a)/(2*n)

P = 0

for i in range(0, n):
    P += 1/mid
    mid += x
print(P*x)