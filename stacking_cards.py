def min_steps_to_sort_cards(cards, n):
    list_of_max = [1] * n

    for i in range(1, n):
        for j in range(i):
            if cards[i] > cards[j]:
                list_of_max[i] = max(list_of_max[i], list_of_max[j] + 1)

    min_steps = n - max(list_of_max)
    
    return min_steps

def main():

    data_sets = int(input())
    results = [0]*data_sets
    for i in range(data_sets):
        n = int(input())
        cards = list(map(int, input().split()))
        results[i] = min_steps_to_sort_cards(cards, n)

    for result in results: print(result)

main()