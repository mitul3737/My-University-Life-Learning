list_0=input()
list_1=list_0.strip('][').split(',')
list_2=[]
for x in list_1:
    list_2.append(int(x))
if len(list_2)<4:
    print("Not possible")
else:
    print(list_2[2:-2])
