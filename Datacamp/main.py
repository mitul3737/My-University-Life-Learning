def function_name(val_1,val_2):
    list_1=[]
    flag=True
    for j in val_1:
        for i in range(1, len(val_1)):
            if abs(j - val_1[i]) == val_2:
                list_2 = []
                list_2.append(j)
                list_2.append(val_1[i])
                list_1.append(list_2)
                print(list_1)
            else:
                flag = False
    if flag:
        print(list_1)
    else:
        "Not Possible"

    return " "


function_name([1, 5, 9, 15, 74], 4)