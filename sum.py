def main():
    n = int(input())
    sum_of_values = 0
    if n<1:
        while n<=1:
            sum_of_values = sum_of_values + n
            n = n + 1
        print(sum_of_values)
    else:
        x = 1
        while x<=n:
            sum_of_values = sum_of_values + x
            x = x + 1
        print(sum_of_values)
main()
