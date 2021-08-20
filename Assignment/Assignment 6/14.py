val_1=input("").strip('""')
num=int(input(""))

def function_name(val_1,num):
    cnt = len(val_1)
    val_s = ""
    res = ""
    for i in range(cnt):
        if i == 0:
            val_s += val_1[0]
        if (i != 0) and (i % num != 0):
            val_s += val_1[i]
        elif i != 0 and i % num == 0:
            res += val_1[i]

    val_s += res
    print(val_s)


function_name(val_1,num)


'''val_1=input("").strip('""')
num=int(input(""))

def function_name(val_1,num):
    cnt = len(val_1)
    val_s = ""
    res = ""
    for i in range(cnt):
        if i == 0:
            val_s += val_1[0]
        if (i != 0) and (i % num != 0):
            val_s += val_1[i]
        elif i != 0 and i % num == 0:
            res += val_1[i]

    val_s += res
    return val_s


print(function_name(val_1,num))'''