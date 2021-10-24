str_0=input("")
try:
    if str_0.index("too good")>0:
        new_str=str_0.replace("too good","excellent")
        print(new_str)
except:
    print(str_0)