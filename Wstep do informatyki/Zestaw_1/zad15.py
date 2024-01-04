from math import *
last_val = sqrt(0.5)
s = last_val

for i in range(1, 1000):
    last_val = sqrt(0.5*last_val + 0.5)
    s *= last_val
    #print(last_val, s)
print(2/s)