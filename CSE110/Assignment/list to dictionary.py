val = [1, 2, 3, 3, 3, 3, 4, 5, 8, 8]
def function_name(val):
    val_1={}
    for i in range(len(val)):
        if i==0:
            val_1[val[i]]=1
        elif val[i] in val_1.keys():
            val_1[val[i]]+=1
        else:
             val_1[val[i]]=1

    print(val_1)
    return ""
function_name(val)