val_1=input("").strip("][").split(",")
val_2=input("").strip("][").split(",")
x=0
y=-1
if len(val_1)==len(val_2):
    for i in range(len(val_1)):
        print(f"{val_1[x]} {val_2[y]}")
        x+=1
        y-=1


