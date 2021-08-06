val_1 = input("").strip("][").split(",")

val_2 = []
val_3 = []
for x in val_1:
    if int(x) % 2 == 0:
        val_2.append(int(x))
    else:
        val_3.append(int(x))

if val_2 == [] and val_3 != []:
    print(f"First even: not found and First odd: {val_3[0]}")

elif val_3 == [] and val_2 != []:
    print(f"First even: {val_2[0]} and First odd: not found")
elif val_2 == [] and val_3 == []:
    print(f"First eve: not found and First odd not found ")
else:
    print(f"First even: {val_2[0]} and First odd: {val_3[0]}")
