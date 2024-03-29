class StackWithMin:
    def __init__(self):
        self.stack = []  
        self.min_stack = []  

    def push(self, value):
        self.stack.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self):
        if not self.stack:
            return "EMPTY"
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        return self.stack.pop()

    def get_min(self):

        if not self.min_stack:
            return "EMPTY"
        return self.min_stack[-1]

def main():
    n = int(input())
    stack = StackWithMin()
    results = []
    for _ in range(n):
        action = input().split()
        if action[0] == "PUSH":
            stack.push(int(action[1]))
        elif action[0] == "POP":
            stack.pop()
        elif action[0] == "MIN":
            results.append((stack.get_min()))
    for result in results:
        print(result)

main()