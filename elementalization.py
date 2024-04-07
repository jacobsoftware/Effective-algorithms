# https://www.spoj.com/problems/MPPZC/

def elementalization(n):         
    return int(n**0.5)
        

def main():
    data_sets = int(input())
    results = [0]*data_sets
    for i in range(data_sets):
        n = int(input())
        results[i] = elementalization(n)
    for result in results:
        print(result)

main()