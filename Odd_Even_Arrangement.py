lists=[1,2,3,4,5,6]

lists2=[]
seen={"Even":[],"Odd":[]}

for val in sorted(lists):
    if val % 2 == 0:
        seen["Even"].append(val)
    else:
        seen["Odd"].append(val)
        
even_index = 0
odd_index = 0
for i in range(len(lists)):
    if i % 2 == 0:
        lists2.append(seen["Even"][even_index])
        even_index += 1
    else:
        lists2.append(seen["Odd"][odd_index])
        odd_index += 1
        
     

print(lists2)