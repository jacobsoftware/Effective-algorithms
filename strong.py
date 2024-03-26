def strong():
    n = int(input())
    strong_value = 1
    if n > 1:
        for i in range(1,n+1):
            strong_value =  strong_value * i
        strong_value = str(strong_value)
        print(strong_value[-1])
        
    else: print(strong_value)

strong()