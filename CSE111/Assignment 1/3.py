str_0=input("")
new_str=""
for i in str_0:
    if i.isupper():
        new_str+=i
if str_0[str_0.index(new_str[0])+1:str_0.index(new_str[1])]=="":
    print("BLANK")
else:
    print(str_0[str_0.index(new_str[0])+1:str_0.index(new_str[1])])