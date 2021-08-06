import math
num=input().split(",")

val_1=int(num[0])
val_2=int(num[1])
val_3=int(num[2])
sum=(val_1+val_2+val_3)/2
area=sum*math.sqrt((sum-val_1)*(sum-val_2)*(sum-val_3))
print(area)