def zadanie(T, x):
    # x - mass we are trying to measure
    # T - weights we have avaliable
    possible = [False for i in T]

    def rek(T, x, possible ,p=0, a=0):
        n = len(T)
        if a == x:
            return (True, possible)
        if p == n:
            return (False, possible)
        else:
            return (
                rek(T, x, possible,p + 1, a)
                or rek(T, x, possible[p] := True,p + 1, a + T[p])
                or rek(T, x + T[p], possible[p] := True, p + 1, a)
            )

    return rek(T, x)


print(zadanie([1, 5], 4))
