def splitting_money(val_0):
    val_1 = val_0
    val_2 = {}
    lst_1 = [500, 100, 50, 20, 10, 2, 1]
    for x in lst_1:
        if val_1 >= x:
            val_4 = val_1 % x
            val_3 = val_1 // x
            val_2[x] = val_3
            val_1 = val_4
    val_5 = '"'
    val_6=len(val_2)
    cnt=0
    for j in val_2:
        if cnt!=len(val_2)-1:
            cnt += 1
            val_5 += f"{j} Taka: {val_2[j]} note(s)\n"
        else:
            val_5 += f'{j} Taka: {val_2[j]} note(s)"'

    return val_5

print(splitting_money(1234))
