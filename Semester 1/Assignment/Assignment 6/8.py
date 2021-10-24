def  show_palindromic_triangle(val_1):
    val_2=1
    spc=(val_1-1)
    for i in range (1,val_1+1):
        val_3=0
        for j in range(1,spc+1):
            print(" ",end=" ")
        for j in range(1,val_2+1):
            if (j<=i):
                val_3+=1
            else:
                val_3-=1
            print(val_3,end=" ")
        print()
        val_2=val_2+2
        spc=spc-1
    return " "
print(show_palindromic_triangle(int(input(""))))