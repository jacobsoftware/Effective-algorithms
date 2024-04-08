def main():
    loop = True
    sum_values = 0
    while loop:
        str_in = input()
        value = int(str_in)
        if  value == 0:
            loop = False
        else:
            sum_values += value
    print(sum_values)

main()
