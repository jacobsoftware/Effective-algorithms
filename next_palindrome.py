def find_palindrom(value):
    n = int(len(value)/2)
    for i in range(n):
        value[-1-i]=value[i]


def main():
    n = int(input())
    results = [0]*n
    for i in range(n):
        value = input()
        results[i] = find_palindrom(value)
    
    for result in results: print(result)

main()