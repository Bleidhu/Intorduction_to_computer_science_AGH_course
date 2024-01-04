n = int(input())

ncp = n

reversedn = 0

while ncp > 0:
    reversedn *= 10
    reversedn += ncp%10;
    ncp//=10
if(n == reversedn):
    print("Palindrom 10")

ncp = n
reversedn = 0
while ncp > 0:
    reversedn *= 2
    reversedn += ncp%2
    ncp//=2

if(n == reversedn):
    print("palindrom 2")

