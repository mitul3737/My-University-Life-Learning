inp=int(input(""))
lst_0=[]
lst_01=[]
lst_02=[]

for i in range(0,inp):
    str_0=input("").split(" ")
    lst_0.append(str_0)

for i in lst_0:
    for j in i:
        lst_01.append(int(j))
    lst_02.append(lst_01)
    lst_01=[]



sum_max=sum(lst_02[0])
for m in lst_02:
    if sum_max<=sum(m):
        sum_max=sum(m)

print(sum_max)
for n in lst_02:
    if sum(n)==sum_max:
        print(n)
