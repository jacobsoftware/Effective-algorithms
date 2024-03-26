def ppl_in_rooms(rooms,n):
    list_of_ppl = [1]*n
    non_empty_rooms = 0
    for _ in range(n):        
        for j in range(n):
            if list_of_ppl[j] > 0:
                list_of_ppl[j] -= 1
                list_of_ppl[rooms[j]-1] += 1

    for i in range(n):
        if list_of_ppl[i] > 0: non_empty_rooms += 1
    return non_empty_rooms


def main():

    data_sets = int(input())
    results = []
    for _ in range(data_sets):
        n = int(input())
        rooms = input()
        rooms = rooms.split(' ')
        rooms = list(map(int, rooms))
        results.append(ppl_in_rooms(rooms,n))

    for result in results:
        print(result)

main()
