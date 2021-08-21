def remove_odd(val_0):
    val_1 = []
    for i in val_0:
        if i % 2 == 0:
            val_1.append(i)
    return val_1

print(remove_odd([21, 33, 44, 66, 11, 1, 88, 45, 10, 9]))
