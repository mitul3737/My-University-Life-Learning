lst_0=[]
lst_1=[]
dict_0={}
inp=input("")
lst_0.append(inp)
while inp!="STOP":
    inp=input("")
    lst_0.append(inp)


for i in lst_0[:-1]:
    lst_1.append(int(i))


num_0=0
for k in lst_1:
    dict_0[k]=lst_1.count(k)

for l in dict_0.keys():
    print(f"{l} - {dict_0[l]} times")