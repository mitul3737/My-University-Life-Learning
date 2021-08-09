val_=input("").strip("}{").split(",")


val_1=[]
count=0
val_2={}
for i in val_:
    count+=1


for i in range(0,count):
    if i==0:
        val_1.append(val_[i])
    else:
        val_1.append(val_[i][1:])




for i in range(0,count):
    if i==0:
        x=int(val_1[i].split(":")[1])
        val_2[val_1[i].split(":")[0][1:-1]]=x
    else:
        x = int(val_1[i].split(":")[1])
        val_2[val_1[i].split(":")[0][1:-1]] = x

print(val_2)
