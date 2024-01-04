def konwersja_i_liczenie_cyf_w_sys_n_kowym(liczba, podstawa):
    cyfry = [False for _ in range(podstawa)]

    while liczba > 0:
        print(liczba%podstawa)
        cyfry[liczba%podstawa] == True
        liczba //= podstawa
    returned = 0
    for i in range(len(cyfry) - 1, -1, -1):
        if(cyfry[i]):
            returned *= 10
            returned += i
    return returned

print(konwersja_i_liczenie_cyf_w_sys_n_kowym(13, 4))
    