def make_square(tup):
    val,val_0=tup
    val_1={}
    for i in range(val,val_0+1):
        val_1[i]=i*i
    print(val_1)
    return " "
print(make_square((1,3)))




'''def make_square(tup):
    val,val_0=tup
    val_1={}
    for i in range(val,val_0+1):
        val_1[i]=i*i

    return val_1
print(make_square((1,3)))'''