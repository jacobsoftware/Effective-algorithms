def main():
    n = int(input())
    stack_of_values = []
    results = []
    for i in range(n):
        action = input().split()

        if 'PUSH' in action[0]:
            stack_of_values.append(int(action[1]))

        elif 'POP' in action[0]:
            stack_of_values.pop()
            
        elif 'MIN' in action[0]:
            results.append(min(stack_of_values))
    for result in results:
       print(result)

main() 