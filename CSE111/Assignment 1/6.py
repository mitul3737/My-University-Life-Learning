str_0=input("")
special=["_","$","#","@"]
low_0=0
upp_0=0
dig_0=0
spc_0=0
str_01=""
for i in str_0:
    if i.isupper():
        upp_0+=1
    elif i.islower():
          low_0+=1
    elif i.isdigit():
         dig_0+=1
    elif i in special:
        spc_0+=1

if low_0>0:
    pass
else:
    str_01+="Lowercase Missing,"

if upp_0>0:
    pass
else:
    str_01+="Uppercase Missing,"
if dig_0>0:
    pass
else:
    str_01+="Digit Missing,"
if spc_0>0:
    pass
else:
    str_01+="Special Missing,"

if str_01=="":
   print("OK")
else:
   print(str_01[:-1])


