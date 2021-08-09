val_0=input("").strip('""').lower()
val_1=[]
for i in val_0:
    val_1.append(i)

val_2={}
for i in val_1:
    if i!=" ":
       val_2[i]=int(val_1.count(i))


print(val_2)