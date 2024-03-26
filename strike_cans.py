def main():
    input_string = input()
    input_string = input_string.split(' ')
    harry = int(input_string[0])
    larry = int(input_string[1])
    all_cans = larry + harry - 1
    not_stroke_harry = all_cans-int(harry)
    not_stroke_larry = all_cans-int(larry)
    print(not_stroke_harry,not_stroke_larry)

main()