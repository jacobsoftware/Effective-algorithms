import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def insert_key(self, key):
        heapq.heappush(self.heap, key)

    def extract_min(self):
        return heapq.heappop(self.heap)

    def top(self):
        if self.heap:
            return self.heap[0]
        else:
            return None


def main():

    n = int(input())
    for _ in range(n):
        max = 0
        items = [x for x in input().split()]
        coins_sum = {}
        heap = PriorityQueue()
        #result = ''
        for item in items:
            if item.isdecimal():
                # Wedlug polecenia zadania 0 nie jest ani moneta ani banknotem a wystepuje w przykladowym inpucie
                if int(item) in coins_sum.keys() and int(item) > 0:                    
                    value = coins_sum[int(item)]
                    coins_sum.update({int(item): value + 1})
                elif int(item) > 0:
                    heap.insert_key(int(item))
                    coins_sum.update({int(item): 1})

            elif item == 'w':
                if heap.top() is not None:
                    if coins_sum[heap.top()] > 1:
                        if (coins_sum[heap.top()] * heap.top() > max) and (coins_sum[heap.top()] * heap.top() > 10000):
                            max = coins_sum[heap.top()] * heap.top()
                            heap.extract_min()
                        else:
                            new_coin = coins_sum[heap.top()] * heap.top()
                            coins_sum.pop(heap.top())
                            heap.extract_min()                            
                            if new_coin in coins_sum.keys():
                                value = coins_sum[new_coin]
                                coins_sum.update({new_coin: value + 1})
                            else:
                                heap.insert_key(new_coin)
                                coins_sum.update({new_coin: 1})
                    else:
                        y = heap.extract_min()
                        if (heap.top() + y > max) and (heap.top() + y > 10000):
                            max = heap.top() + y
                            heap.extract_min()
                        else:
                            new_coin = heap.top() + y
                            coins_sum[heap.top()] -= 1
                            heap.extract_min()
                            if new_coin in coins_sum.keys():
                                value = coins_sum[new_coin]
                                coins_sum.update({new_coin: value + 1})
                            else:
                                heap.insert_key(new_coin)
                                coins_sum.update({new_coin: 1})

            elif item == 'k':
                if max == 0:
                    print('bb')
                else:
                    print(max)
        #     elif item == 'k':              
        #         if max == 0:
        #             if result == '':
        #                 result = result + 'bb'
        #             else:
        #                 result = result + ' bb'
        #         else:
        #             if result == '':
        #                 result = result + str(max)
        #             else:
        #                 result = result + ' ' + str(max)

        # print(result)
main()