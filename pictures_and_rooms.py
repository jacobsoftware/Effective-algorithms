def ppl_in_rooms(rooms,n):
    list_of_ppl = [1]*n
    non_empty_rooms = 0
    # prev_list = [0]*n
    how_many_options = set(rooms)
    m = n
    if len(how_many_options) != n: m = len(how_many_options)+1
    for _ in range(m):        
        for j in range(n):
            if list_of_ppl[j] > 0:
                list_of_ppl[j] -= 1
                list_of_ppl[rooms[j]-1] += 1
        # if prev_list == list_of_ppl: break
        # else: prev_list = list_of_ppl[:]

    for i in range(n): 
        if list_of_ppl[i] > 0: non_empty_rooms += 1
    return non_empty_rooms

def main():

    data_sets = int(input())
    results = [0]*data_sets
    for i in range(data_sets):
        n = int(input())
        rooms = list(map(int,input().split()))
        results[i] = ppl_in_rooms(rooms,n)
    for result in results:
        print(result)

main()

