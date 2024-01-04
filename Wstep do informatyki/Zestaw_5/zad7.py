def zadanie(T, x):
    # x - mass we are trying to measure
    # T - weights we have avaliable
    def rek(T, x, p=0, a=0):
        n = len(T)
        if a == x:
            return True
        if p == n:
            return False
        else:
            return rek(T, x, p + 1, a) or rek(T, x, p + 1, a + T[p])

    return rek(T, x)


print(zadanie([1, 2, 3], 3))
