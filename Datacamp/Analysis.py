val_1=input("")
val_2=input("")
val_3=""
i=0
for x in val_2:
    print(x)
    for y in val_1:
        if x not in val_1:
            val_3 += val_1[i]
            print(val_3)
            i += 1
        else:
             break

print(val_3)
