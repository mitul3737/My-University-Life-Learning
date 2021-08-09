val_1=input("").strip(")(").split(",") #making a list from the string

if val_1[0].isdigit()==True: #checks if your contents are all integers
    val_2 = []
    for i in val_1:
        val_2.append(int(i))
    val_2 = tuple(val_2)
    print(val_2)
else: # if the contents in your tuple are of string, tis case is applied
    val_2=[]
    for i in range(0,len(val_1)):
        if i==0:
            val_2.append(val_1[i][1:-1])
        else:
            val_2.append(val_1[i][2:-1])

    val_2=tuple(val_2)
    print(val_2)

