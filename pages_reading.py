def read_input():
    # Read the number of test cases
    d = int(input())
    test_cases = []
    
    # Read each test case
    for _ in range(d):
        n = int(input())
        a = list(map(int, input().split()))
        test_cases.append((n, a))
    
    return test_cases

def solve_test_case(n, a):
    # Initialize variables
    rounds = 0
    flipped = False
    
    # Check if all cards are correctly oriented
    while not all(a):
        # If the first card is flipped, flip the entire stack
        if a[0] == 1:
            a = [1 - x for x in a]
            flipped = not flipped
        else:
            # Rotate the stack until the first card is correctly oriented
            for i in range(n):
                if a[i] == 1:
                    a = a[i:] + a[:i]
                    break
        rounds += 1
    
    return rounds if flipped else 0

def main():
    test_cases = read_input()
    for n, a in test_cases:
        result = solve_test_case(n, a)
        print(result)

if __name__ == "__main__":
    main()
