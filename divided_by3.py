def div3():
    n = int(input())
    string = ''
    div_counter = 0
    for i in range(1,n+1):
        string += str(i)
        if int(string) % 3 == 0: div_counter += 1
    print(div_counter)

div3()
    