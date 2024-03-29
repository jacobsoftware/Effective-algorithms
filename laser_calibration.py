def number_of_reflections(a, b):
    n = 0    
    if b > (180.0-a)/2: return n
    else:
        while True:
            if b > (180.0-n*a-b): break
            else: n = n +1                
        return n-1

def main():
    data_sets = int(input())
    results = [0]*data_sets
    for i in range(data_sets):
        angle_a, angle_b = map(float,input().split())
        results[i] = number_of_reflections(angle_a, angle_b)

    for result in results:
        print(result)

main()