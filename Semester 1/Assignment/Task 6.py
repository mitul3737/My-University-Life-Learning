list_0=input()
list_1=list_0.strip('][').split(',')
list_2=[]
for x in list_1:
    list_2.append(int(x))
min=0
max=0
for i in range(0,len(list_2)):
    if min>int(list_2[i]):
        min=int(list_2[i])
    elif max<int(list_2[i]):
        max=int(list_2[i])
        y=i

print("My list:",list_2)
print("Largest number in the list is",max," which was found at index",y)