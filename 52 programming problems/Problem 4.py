val_1=int(input(""))
val_2=int(input(""))
val_3=int(input(""))
val_4=int(input(""))
val_5=[val_2,val_3,val_4]
val_6=[]
i=1
for x in val_5:
    for y in range(1,x+1,1):
        print(y)
        if x%y==0:
            val_6.append(y)


for x in range(0, len(val_6)):
    if val_6[x] == 1 and x == 0:
        print("Case", i, ":", end='')
        print(val_6[x], "\t", end='')
        i = i + 1
    elif val_6[x] == 1 and x != 0:
        print("\nCase", i, ":", end='')
        print(val_6[x], "\t", end='')
        i = i + 1
    elif val_6[x] != 1:
        print(val_6[x], "\t", end='')
