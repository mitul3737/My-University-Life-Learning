#bubble sort
list_1=[5,3,1,9,8,2,4,7]

for i in range(len(list_1)-1):
    for j in range(0,len(list_1)-i-1):
        if list_1[j]>list_1[j+1]:
            temp=list_1[j]
            list_1[j]=list_1[j+1]
            list_1[j+1]=temp

print(list_1)

'''def bubble_sort(L):
   n=len(L)
   for i in range(0,n):
      for j in range(0,n-i-1):
         if L[j]>L[j+1]:
            L[j],L[j+1]=L[j+1],L[j]
   return L
print(bubble_sort([10,34,23,6,7,45,24]))'''