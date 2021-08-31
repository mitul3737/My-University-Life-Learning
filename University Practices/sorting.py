list_1=[7,5,4,2]

for i in range(len(list_1)):
    min_index=i#taking minimum index as the range value

    for j in range(i+1,len(list_1)):#starting after the range value to the length of the list
        if list_1[j]<list_1[min_index]:
            min_index=j
    temp=list_1[min_index]
    list_1[min_index]=list_1[i]
    list_1[i]=temp

print(list_1)