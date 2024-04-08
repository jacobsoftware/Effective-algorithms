# https://www.spoj.com/problems/MPPZC/
class BigNum:
    def __init__(self, value):
        self.value = str(value)

    def __str__(self):
        return self.value

    def sqrt(self):

        num = int(self.value)
        if num == 0:
            return BigNum(0)

        guess = num
        while True:
            new_guess = (guess + num // guess) // 2
            if abs(new_guess - guess) < 1:
                break
            guess = new_guess

        return BigNum(guess)



def main():
    data_sets = int(input())
    results = [0]*data_sets
    for i in range(data_sets):
        n = BigNum(input())
        results[i] = n.sqrt()

    for result in results:
        print(result)

main()

# 255
# 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999