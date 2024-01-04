
import random
def min_max_count(t):
    min_el = t[0]
    max_el = t[0]
    for i in t:
        if(i < min_el):
            min_el = i
        if(i > max_el):
            max_el = i
    min_count = 0
    max_count = 0

    for i in t:
        if(i == min_el):
            min_count += 1
        if(i == max_el):
            max_count += 1

    if( min_count == 1 and max_count == 1):
        return True
    else: 
        return False
    

t = [random.randrange(1, 5000) for _ in range(500)]

print(min_max_count(t))