dict_0={}
lst_1=[]
srt_0=input("").split(", ")

for i in srt_0:
    str_1=i.split(" : ")
    if str_1[1] not in dict_0.keys():
        lst_1=[str_1[0]]
        dict_0[str_1[1]]=lst_1
    else:
        dict_0[str_1[1]].append(str_1[0])
    lst_1=[]
print(dict_0)
