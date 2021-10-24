str_0=input("").strip().split(", ")
flag=False
str_01=""
j_0=0

try:
    for i in str_0[0]:
        for k in str_0[1]:
            if i == k:
                str_01 += i
                flag = True

    for j in str_0[0]:
        if j == str_0[1][j_0]:
            str_01 += j
            j_0 += 1
            flag = True
        else:
            j_0 += 1
except IndexError:
    print("Nothing in common.")

if flag:
   print(str_01)
