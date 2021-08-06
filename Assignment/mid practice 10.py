val_1=input("").lower()
val_2=input("").lower()
val_3=""

for x in val_2:

    for y in val_1:
        if x !=y:
            val_3 += y

    val_1=val_3
    val_3=""


print(val_1)
