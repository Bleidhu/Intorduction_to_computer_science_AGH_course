# ile dni w roku 366 (przestepne)

import random


n = int(input())
allExp = 0
succesExp = 0
for _ in range(100000):
    allExp += 1
    var = False
    t = [ random.randrange(1, 365) if random.randrange(1, 4) != 4 else random.randrange(1, 365) for _ in range(n)]

    dates = [0 for _ in range(367)]


    for i in t:
        dates[i] += 1
        if(dates[i] >= 2):
            var = True
    
    if(var):
        succesExp += 1

print((succesExp / allExp) * 100, "%", sep="")