n1_list=input()
n2_list=input()
list_1=n1_list.strip('').split(',')
list_2=n2_list.strip('').split(',')
list_one=[]
list_two=[]
for x in range(0, len(list_1)):
    if x == 0:
        list_one.append(list_1[x])
    elif x > 0:
        list_one.append(str(list_1[x][1:]))


for x in range(0, len(list_2)):
    if x == 0:
        list_two.append(list_2[x])
    elif x > 0:
        list_two.append(str(list_2[x][1:]))

list_three=[]

for i in list_one:
    if i not in list_three:
        if i in list_two:
            list_three.append(i)

print(list_three)
