def show_palindrome(val_1):
    val_2=""
    for i in range(1,val_1+1):
         val_2=val_2+str(i)
    val_3=val_2[0:-1]
    for i in val_3[::-1]:
        val_2+=str(i)
    return val_2
print(show_palindrome(int(input(""))))

