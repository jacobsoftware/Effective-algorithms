def reverse_polish_notation(expression):
    dict_of_operators = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    postfix = []
    for char in expression:
        if char.isalpha(): postfix.append(char)

        elif char == '(': stack.append(char)

        elif char == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()  

        elif char in dict_of_operators.keys():
            while stack and stack[-1] != '(' and dict_of_operators(stack[-1]) >= dict_of_operators[char]:
                postfix.append(stack.pop())
            stack.append(char)

    string = ''
    return string.join(postfix)


def main():

    data_sets = int(input())
    results = [0]*data_sets

    for i in range(data_sets):
        expression = input()
        results[i] = reverse_polish_notation(expression)

    for result in results:
        print(result)

main()