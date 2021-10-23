list_0=input()
list_1=list_0.strip().split(',')
list_2=[]
for x in list_1:
    list_2.append(int(x))
list_3=[]
for x in list_2:
    if x%2!=0:
        list_3.append(int(x))
print(list_3)