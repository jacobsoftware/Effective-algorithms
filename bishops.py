def bishops():
    i = 0
    while i < 1024:
        n = int(input())
        if n == 1:
            print(1)
        else:
            print(2*(n - 1))
        i += 1
bishops()
