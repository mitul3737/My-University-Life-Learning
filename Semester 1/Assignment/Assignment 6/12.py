def function_name(val):
    val_1={}
    for i in range(len(val)):
        if i==0:
            val_1[val[i]]=1
        elif val[i] in val_1.keys():
            val_1[val[i]]+=1
        else:
             val_1[val[i]]=1


    val_2=[]
    rem=0
    for i in val_1.keys():
        if val_1[i]<=2:
             for j in range(val_1[i]):
                val_2.append(i)

        else:
           rem=val_1[i]-2
           for j in range(2):
               val_2.append(i)

    print(f"Removed: {rem}")
    print(val_2)


    return ""
function_name([10, 10, 15, 15, 20])