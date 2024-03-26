def input_list():
    list_of_ints = []
    x=0
    while True:
        value_in = int(input())
        list_of_ints.append(value_in)
        if value_in == 42: break
    return list_of_ints
data = input_list()
for item in data:
    if item != 42: print(item)
    else: break
