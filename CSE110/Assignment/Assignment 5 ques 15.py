val_1=( [1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12])
val_0=input("")
val_2=[]
val_3=()
count=0
for i in val_1:
    count+=1
for i in range(0,count):
    val_1[i][2]=val_0


print(val_1)
