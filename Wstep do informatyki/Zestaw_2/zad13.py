n = int(input())

dig = n%10

n //= 10

war = True

while n > 0:
    if(n%10 == dig):
        war = False
        break
    n//=10

print(war)
