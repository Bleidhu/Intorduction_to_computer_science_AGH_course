n = int(input())

a = 2
is_part_of_seq = False
while a < n:
    if(n%a == 0):
        is_part_of_seq = True
        break
    a = 3*a + 1

if(is_part_of_seq):
    print('Tak')
else:
    print('Nie')