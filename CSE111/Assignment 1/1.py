str_0=input("")
upp=0
low=0
for i in str_0:
    if i.isupper():
        upp+=1
    else:
        low+=1
if upp>low:
   print(str_0.upper())
else:
   print(str_0.lower())