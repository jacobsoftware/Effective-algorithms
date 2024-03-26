def looking_for_vip(members):
    for i in range(0,len(members)):
        if members[i].count('1') == 1:
            
            vip_id = i+1
            break
    
    return vip_id

data_sets = int(input())
results = []
for _ in range(data_sets):
    n = int(input())
    members = []
    for _ in range(n):
        members.append(input())

    results.append(looking_for_vip(members))

for result in results:
    print(result) 
