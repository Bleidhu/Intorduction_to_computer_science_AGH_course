def hanoi(n, x, y, z):
    if n == 1:
        print(x + "=>" + y)
        return
    else:
        hanoi(n-1, x, z, y)
        print(x + '=>' + y)
        hanoi(n-1, z, y, x)

hanoi(5, "a", "b", "c")