import math
num=input().split(",")

val_1=int(num[0])
val_2=int(num[1])
val_3=int(num[2])
if val_1+val_2>val_3:
    print("Valid triangle")
else:
    print("Not a valid triangle")