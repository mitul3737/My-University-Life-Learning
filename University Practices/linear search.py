def linear_search(l1,x):
    for i in  l1:
        if i ==x:
            return  l1.index(i)
    return -1


list_1=[1,2,34,5,89,67,3]


index=linear_search(list_1,5)

if index!=-1:
    print("Element found at index ",index)
else:
    print("Element not found")



'''
def linear_search(L,x):
   n=len(L)
   i=0
   while i<n:
      if L[i]==x:
          return i
      i+=1
   i=-1
   return i

print(linear_search([1,2,5,7,3,8,4,65,34,23,89,45],23))

'''