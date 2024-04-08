# https://www.spoj.com/problems/PAYING/

def how_many_coins(value):
    rest = value
    i = 0
    sum_value_of_coins = 0
    coins = 0
    while True:

        if rest == 0:
            return coins
        else:
            if rest >= 2**i:
                sum_value_of_coins += 2**i
                rest = value - sum_value_of_coins
                coins += 1
                i += 1
            else:
                i -=1
                if rest >= 2**i:
                    sum_value_of_coins += 2**i
                    rest = value - sum_value_of_coins
                    coins += 1
        


def main():
    data_sets = int(input())

    for _ in range(data_sets):
        str_in = input()
        value = int(str_in)
        print(how_many_coins(value))

main()
