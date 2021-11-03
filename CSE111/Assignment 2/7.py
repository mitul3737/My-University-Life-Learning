str_3=input("")[1:-1]


def palindrome(word):
    lst_0=[]
    lst_1=[]
    str_0=""
    for i in word:
        if i!=" ":
            str_0+=i

    for i in str_0:
        lst_0.append(i)


    for j in reversed(str_0):
        lst_1.append(j)

    if lst_0==lst_1:
        print("Palindrome")
    else:
        print("Not a palindrome")


palindrome(str_3)
