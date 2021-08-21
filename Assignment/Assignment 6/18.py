val_1=int(input(""))
val_2=int(input(""))
val_3=int(input(""))
val_4=int(input(""))
def function_name( val_1,val_2,al_3,val_4):
    cnt = 0
    for i in range(val_1, val_2):
        if (i % val_3 == 0 or i % val_4 == 0) and i % (val_3 * val_4):
            cnt += i
    return cnt

print(function_name(val_1,val_2,val_3,val_4))