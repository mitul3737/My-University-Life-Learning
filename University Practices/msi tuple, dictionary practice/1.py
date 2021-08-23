num=int(input(""))
lst_1=[]
for i in range(num):
    val_o=input("")
    lst_1.append(str(val_o))

lst_2=[]
lst_3=[]
for val in lst_1:
    siz_0=len((val))
    sum_even=0
    sum_odd=0
    for i in range(2,siz_0+1,2):
        sum_even+=int((val[i-1]))
    for j in range(1,siz_0+1,2):
        sum_odd+=int((val[j-1]))
    if sum_odd==sum_even:
        lst_2.append(int(val))
    else:
        lst_3.append(int(val))


tup_1=tuple(lst_2)
tup_2=tuple(lst_3)
print(f"({tup_1},{tup_2})")
