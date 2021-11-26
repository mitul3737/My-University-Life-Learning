set_1={11,12,13,14,15}
#indexing not allowed set_1[0]

#add:
set_1.add(77)

#to update multiple items:
set_1.update([88,89,100])#list of numbers
set_1.update([34,35],{23,59,45}) #list and set of numbers
print(set_1) #output: {11, 12, 77, 13, 14, 15, 23, 88, 89, 34, 35, 100, 45, 59}

set_1.discard(10)#if 10 is not present, it wqont remove it and show no error but
#set_1.remove(10)# this will give error as 10 is not present in set_1
print(set_1.pop())#poing a value out of set
print(set_1)
set_2={0,1,2,3,4,5}
set_3={4,5,6,7,8,9}
#union
print(set_2 | set_3)
print(set_3|set_2)
print(set_2.union(set_3))
print(set_3.union(set_2))
#intersection
print(set_3 & set_2)
print(set_2 & set_3)
print(set_2.intersection(set_3))
#difference
print(set_3-set_2)
print(set_3.difference(set_2))
#symmetric difference :other tha common elements
print(set_2 ^ set_3)
print(set_2.symmetric_difference(set_3))

#membership
print(2 in set_2)

#iterate
for i in set("welcome"):
    print(i)

#built in
print(len(set_2))
print(max(set_2))
print(min(set_2))
print(sorted(set_2))

#frozen set
set_4=frozenset([1,2,3,4,5,67,5])
set_5=frozenset([9,46,34,67,0,3])
print(set_4.union(set_5))
print(set_4.intersection(set_5))
