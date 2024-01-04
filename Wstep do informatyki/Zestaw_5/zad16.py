
def waga(a):
        c_sum = 0
        sam = 0
        for i in range(len(a)):
            if(a[i] in ('a', 'e', 'y', 'u', 'i', 'o')):
                sam += 1
            c_sum += ord(a[i])
        return((c_sum, sam))

def zadanie(s1, s2):
    s1_c_sum, s1_sam = waga(s1)

    def rekurencja(s2, a=0, c_sum=0, sam=0):
         nonlocal s1_c_sum
         nonlocal s1_sam
         n = len(s2)
         if(a == n):
              if s1_c_sum == c_sum and s1_sam == sam:
                   return True
         else:
              modiff = 0
              if s2[a] in ('a', 'e', 'y', 'u', 'i', 'o'):
                   modiff = 1
              return rekurencja(s2, a+1, c_sum, sam) or rekurencja(s2, a+1, c_sum+ord(s2[a]), sam + modiff)
    print(rekurencja(s2))

zadanie('ula', 'exes')