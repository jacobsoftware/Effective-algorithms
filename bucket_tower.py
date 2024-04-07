# https://www.spoj.com/problems/MWPZ034/

class MyStack:
    def __init__(self):
        self.stack = []
        self.size = 0
    
    def push(self, item):
        self.stack.append(item)
        self.size += 1
    
    def pop(self):
        if not self.stack:
            return None
        self.size -= 1
        return self.stack.pop()
    
    
    def top(self):
        if not self.stack:
            return None
        return self.stack[-1]
    


def bucket_tower(values,n):

    s = MyStack()
    s.push((values[0],values[1],0))
    for i in range(1, n):
        pod = s.top()[2]

        while (s.top() is not None) and (s.top()[0] <= values[i*2]):

            if pod < s.top()[1] + s.top()[2]:
                pod = s.top()[1] + s.top()[2]

            s.pop()

        s.push((values[i*2],values[i*2+1],pod))

    height = max_height(s)

    return height


def max_height(s):
    max = 0
    while s.top() is not None:
        height = s.top()[1] + s.top()[2]
        if height > max:
            max = height
        s.pop()
    return max


def main():
    data_sets = int(input())
    results = [0]*data_sets
    for i in range(data_sets):
        n = int(input())
        values = [int(x) for x in input().split()]
        results[i] = bucket_tower(values, n)

    for result in results:
        print(result)


main()


