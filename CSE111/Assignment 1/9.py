lst_0=[]
lst_01=[]
lst_02=[]
lst_03=[]
for i in range(0,2):
    str_0 = input("").split(" ")
    lst_0.append(str_0)

for i in lst_0:
    for j in i:
        lst_01.append(int(j))
    lst_02.append(lst_01)
    lst_01=[]


for i in lst_02[0]:
    for j in lst_02[1]:
        lst_03.append(i*j)


print(lst_03)