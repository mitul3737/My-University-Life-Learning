list_0=input()
list_1=list_0.strip('').split(',')
list_2=[]
for x in list_1:
    list_2.append(int(x))
min=0
max=0
min_1=0
max_1=0
list_3=list_2.copy()
for i in range(0,len(list_2)):
    if min>int(list_2[i]):
        min=int(list_2[i])
    elif max<int(list_2[i]):
        max=int(list_2[i])

list_3.remove(max)

for i in range(0,len(list_3)):
    if min_1>int(list_3[i]):
        min_1=int(list_3[i])
    elif max_1<int(list_3[i]):
        max_1=int(list_3[i])

for i in range(0,len(list_2)):
    if list_2[i]==max_1:
        y=i


print("My list:",list_2)
print("Second largest number in the list is",max_1," which was found at index",y)