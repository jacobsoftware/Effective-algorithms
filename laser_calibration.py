def liczba_odbic(A, B):
    n = 1
    if B > (180.0*A)/A: return 0
    else:
        while True:
            if 180-2*A-B < 0: break
            else:
                A = 180 -2*A-B
                n = n +1
                
        return n



d = int(input())
wyniki = []
for _ in range(d):
    string_in = input()
    splitted = string_in.split(' ')
    A = float(splitted[0])
    B = float(splitted[1])
    wyniki.append(liczba_odbic(A, B))


for wynik in wyniki:
    print(wynik)
