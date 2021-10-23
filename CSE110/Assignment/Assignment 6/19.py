def function_name(val_0):
    flag = True
    val_2 = val_0.lower()
    val_1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    for i in val_1:
        if i in val_2:
            flag = True
        else:
            flag = False
            break
    if flag:
        return 5
    else:
        return 6



val_x=input("")
for i in range(function_name(val_x)):
    print("Chelsea is the best club in England")