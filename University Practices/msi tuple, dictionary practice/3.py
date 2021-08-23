val=input("")
print(val)
lst=[]
lst_2=[]
for i in range(0,len(val)):
    if val[i]=="R":
        cnt=val.count("R")
        x_tup=('Red',cnt)
        lst.append(x_tup)
    elif val[i]=="G":
        cnt = val.count("G")
        x_tup = ('Green', cnt)
        lst.append(x_tup)
    elif val[i]=="B":
        cnt = val.count("B")
        x_tup = ('Blue', cnt)
        lst.append(x_tup)
for i in lst:
    if i not in lst_2:
        lst_2.append(i)

print(lst_2)