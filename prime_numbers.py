def if_prime(value):
    if value == 2 or value == 1: return False
    if value % 2 == 0: return False

    max_divider = int(value**0.5)+1
    for divider in range(3,max_divider,2):
        if value % divider == 0: return False
        
    return True

def main():
    n = int(input())
    values = []
    for i in range(n):
        values.append(int(input()))
    for value in values:
        output = if_prime(value)
        if output: print('TAK')
        else: print('NIE')

main()