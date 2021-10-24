list_0=input()
list_1=list_0.strip().split(',')

list_2=[]
list_3=[]
for x in list_1:
    list_2.append(x)
for y in list_2:
    list_3.append(int(y))

list_4=[]
for i in list_3:
    if i not in list_4:
        list_4.append(i)
print(list_4)
