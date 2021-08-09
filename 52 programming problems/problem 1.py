val_1=int(input(""))
val_3=[]
for x in range(0,val_1):
    val_2=int(input(""))
    if val_2% 2 == 0:
        val_3.append(1)

    else:
        val_3.append(0)
for j in val_3:
    if j==1:
        print("even")
    else:
        print("odd")