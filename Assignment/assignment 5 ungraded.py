val_1=[(11, 22), (33, 55), (55, 77), (11, 44)]
val_2=[]
count=0
for i in val_1:
    count+=1

for i in range(0,count):
    val_2.append(val_1[i][0]*val_1[i][1])

print(val_2)
