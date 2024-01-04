n = int(input())

war = True

while n > 0:
    if n%10 <= (n//10)%10:
        war = False
        break
    else:
        n //= 10

print(war)