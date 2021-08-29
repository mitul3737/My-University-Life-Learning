numbers = [17, 3, 9, 21, 2, 7, 5]
print("Before Sorting:", numbers)  # size/length is = 5

for index1 in range(0, len(numbers) - 1):  # 0,1,2,3 (Iteration 4)
    min_val = numbers[index1]
    min_index = index1
    # finding the minimum value from partition to rest of data
    # partition/index is moving to right

    for index2 in range(index1 + 1, len(numbers)):
        if numbers[index2] < min_val:
            min_val = numbers[index2]
            min_index = index2

    # swapping partition's right value with the min value
    temp = min_val
    numbers[min_index] = numbers[index1]
    numbers[index1] = temp

print("After Sorting:", numbers)




''''def selection_sort(L):
   n=len(L)
   for i in range(0,n-1):
      index_min=i
      for j in range(i+1,n):
         if L[j]<L[index_min]:
            index_min=j
      if index_min!=i:
         L[i],L[index_min]=L[index_min],L[i]
   return L

print(selection_sort([10,34,2,36,45,23]))'''