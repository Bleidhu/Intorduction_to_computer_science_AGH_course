for i in range(1, 1000000):
    print(i)
    tmp = i
    digitsum = 0
    while tmp > 0:
        digitsum += tmp%10
        tmp //= 10
    tmp = i
    sum = 0
    n = 2
    while tmp > 1:
        if(tmp%n == 0):
            sum += n
            tmp //= n
        else:
            n += 1
    if(digitsum == sum):
        print(i)