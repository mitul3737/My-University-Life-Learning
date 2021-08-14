val_1={'a' : 6, 'b' : 7, 'c' : 9, 'd' : 8, 'e' : 11, 'f' : 12, 'g' : 13}
val_2=input("").split(", ")
val_3={}
min=int(val_2[0])
max=int(val_2[1])
count=0
for i in val_1:
    count+=1

for i in val_1.keys():
    if val_1[i]>=min and val_1[i]<max:
        val_3[i]=val_1[i]

print(val_3)