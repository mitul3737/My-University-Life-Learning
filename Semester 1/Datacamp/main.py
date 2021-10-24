dict_0={}
lst_1=[]
lst_0=[]
for i in range(0,2):
    str_0=input("").split(", ")
    lst_0.append(str_0)
str_lst=[]
tup=()
for i in lst_0:
    for j in i:
        str_1= j.split(": ")
        if str_1[0] not in dict_0.keys():
              dict_0[str_1[0]]=int(str_1[1])
        else:
            dict_0[str_1[0]] += int(str_1[1])

print(dict_0)

for b in dict_0.keys():
    if dict_0[b] not in str_lst:
         str_lst.append(dict_0[b])

str_lst=sorted(str_lst)


for e in str_lst:
    tup_1=(e,)
    tup+=tup_1

print(f"Values: {tup}")