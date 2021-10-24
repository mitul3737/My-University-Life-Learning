str_0=input("")

if str_0.isdigit():
    print('NUMBER')
elif str_0.isalpha():
    print("WORD")
else:
    print("MIXED")