inp=input("")
try:
    if inp.index("too good")>0:
        new_str=inp.replace("too good","excellent",1)
        print(new_str)
except:
    print(inp)