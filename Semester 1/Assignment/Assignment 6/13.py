val_1=input("").strip('""')
val_2=float(input(""))
val_3=float(input(""))
def function_name(val_1,val_2,val_3):
    if val_1 == "+":
        fin = val_2 + val_3
    elif val_1 == "*":
        fin = val_2 * val_3
    elif val_1 == "/":
        fin = val_2 / val_3
    elif val_1 == "-":
        fin = val_2 - val_3
    print(fin)

function_name(val_1,val_2,val_3)


'''val_1=input("").strip('""')
val_2=float(input(""))
val_3=float(input(""))
def function_name(val_1,val_2,val_3):
    if val_1 == "+":
        fin = val_2 + val_3
    elif val_1 == "*":
        fin = val_2 * val_3
    elif val_1 == "/":
        fin = val_2 / val_3
    elif val_1 == "-":
        fin = val_2 - val_3
    return fin

print(function_name(val_1,val_2,val_3))'''