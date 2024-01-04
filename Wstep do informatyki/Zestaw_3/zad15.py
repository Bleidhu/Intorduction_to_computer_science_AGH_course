import math
def is_prime(a):
    d = 2
    while d <= math.sqrt(a):
        if(a%d == 0):
            return(False)
    return(True)

def check_var(t):
    a = 1
    b = 1
    while a < len(t):
        if(is_prime(t[a])):
            return False
        a, b = b, a + b
    counter = 0

    for i in t:
        if(is_prime(i)):
            counter += 1
    if(counter != 0):
        return True
    else:
        return False