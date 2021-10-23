val_1=input("").strip("][").split(",")
val_2=[]
for str_1 in val_1:
    str_1=str_1[1:-1]
    rev = ""


    num1 = len(str_1)
    j = num1 - 1
    for i in range(0, num1):
        rev = rev + str_1[j]
        j = j - 1

    val_2.append(rev)
print(val_2)

