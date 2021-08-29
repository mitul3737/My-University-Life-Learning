def binary_search(data, size, key):
    left = 0
    right = size - 1

    while left <= right:
        mid = int((left + right) // 2)
        if key == data[mid]:
            return mid
        elif key > data[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # sentinel if not found


data = [-5, 5, 10, 15, 20, 50, 100, 150, 200, 300]
binary_search(data, len(data), 5)



'''''def binary_search(L,x):
   left,right=0,len(L)-1
   while left<=right:
      mid=(left+right)//2
      if L[mid]==x:
         return mid
      elif L[mid]<x:
         left=mid+1
      else:
         right=mid-1
   return -1


print(binary_search([1,2,3,4,5,6,7,8,9,10,11,12,13],5))'''