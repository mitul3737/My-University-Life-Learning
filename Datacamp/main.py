list_one = [1, -8, 4, -7, -20, 26, 70, -85]
list_2=[]
list_3=[]
for i in range(0,len(list_one)):
     for j in range(i+1,len(list_one)):
        list_2.append(list_one[i]+list_one[j])

def sum_checker(x):
    for i in range(0, len(list_one)):
        for j in range(i + 1, len(list_one)):
            if list_one[i] + list_one[j] == x:
                print(f'Two pairs which have the smallest sum = {list_one[i]} and {list_one[j]}')
    return " "

def bubble_sort(L):
    n=len(L)
    for i in range(0,n):
        for j in range(0,n-i-1):
            if L[j]>L[j+1]:
                L[j],L[j+1]=L[j+1],L[j]
    return L
list_2_1=bubble_sort(list_2)
print(list_2_1)

for k in bubble_sort(list_2):
    if k==0:
        list_3=[]
        break
    elif k<0:
        list_3.append(k)


if list_3==[]:
    sum_checker(0)
else:
    sum_checker(list_3[-1])