# https://www.spoj.com/problems/MWPZ031/



def pages_reading(pages,n):
    if '1' not in pages:
        return 0
    elif n == 1 and pages[0] == 1:
        return 1
    elif '1' in pages[0] and '1' not in pages[1:] and n > 1: 
        return 2
    elif ('0' in pages[0] and '0' not in pages[1:]) or '0' not in pages:
        return 1
    else:
        return 'NIGDY'


def main():
    data_sets = int(input())
    results = [0]*data_sets
    for i in range(data_sets):
        n = int(input())
        pages = input()
        results[i] = pages_reading(pages,n)
    for result in results: print(result)

main()












# def pages_reading(pages,n):
#     rounds = 0
#     if 1 not in pages: return rounds
#     else:
#         for i in range(n):
            
#             if pages[0] == 1 and i == 0:
                 
#                 for j in range(n):
#                     print('WArunek',pages[j])
#                     if pages[j] == 1: 
#                         pages[j] = 0
#                     else: 
#                         pages[j] = 1
#                 rounds += 1
#             else:
#                 pages.pop(0)
#                 for j in range(n-1):
#                     if j == 0 and pages[j] == 1 :
#                         pages[0] = 0                    
#                     elif j==0 and pages[j] == 0: 
#                         break

#                     if j != 0 and pages[j] == 1: 
#                         pages[j] = 0
#                     elif j != 0 and pages[j] == 0: 
#                         pages[j] = 1
#                 pages.append(0)
#                 rounds += 1
#             if 1 not in pages: 
#                 return rounds
        

#         if 1 in pages: 
#             return 'NIGDY'
#         else: 
#             return rounds


# def main():
#     data_sets = int(input())
#     results = [0]*data_sets
#     for i in range(data_sets):
#         n = int(input())
#         pages = list(map(int,input().split()))
#         results[i] = pages_reading(pages,n)
#     for result in results: print(result)

# main()


