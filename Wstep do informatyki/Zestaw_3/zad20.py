MAX_NUMBER_VALUE = 1000

def zad20(T):
    n = len(T)

    factors = [0]*MAX_NUMBER_VALUE

    left, right = 0, 0
    max_len = 0

    while right < n:
        #jesli max. ilosc kazdego czynnika <= 1 to moge dodac nowy element
        if max(factors) <= 1:
            copy_num = T[right]

            d = 2
            while copy_num != 1:
                while copy_num % d == 0:
                    factors[d] += 1
                    copy_num //= d
                d += 1
            right += 1
        else:
            copy_num = T[left]

            d = 2
            while copy_num != 1:
                while copy_num % d == 0:
                    factors[d] -= 1
                    copy_num //= d
                d += 1
            left += 1

        if max(factors) <= 1:
            max_len = max(max_len, right - left)
    return max_len

print(zad20([5, 3, 2, 9]))