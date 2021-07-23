n1_list=input()
n2_list=input()
list_1=n1_list.strip('][').split(',')
list_2=n2_list.strip('][').split(',')
list_one=[]
list_two=[]
x="False"
for x in list_1:
    list_one.append(int(x))
for y in list_2:
    list_two.append(int(y))
for i in list_one:
    if i in list_two:
        x="True"
        break

if x=="True":
    print("True")
else:
    print(False)