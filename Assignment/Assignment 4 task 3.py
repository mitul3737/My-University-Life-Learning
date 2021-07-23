list_1=[]
for x in range (0,5):
    val=input("")
    list_1.append(int(val))
list_2=list_1.copy()
list_2.reverse()

for y in list_2:
    print(y)