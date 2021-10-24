val_1 = input("").strip("][").split(", ")
val_2 = int(input(""))
val_3 = []
for i in range(1, val_2 + 1):
    for x in val_1:
        x = x[1:-1]
        x = x + str(i)
        val_3.append(x)

print(val_3)