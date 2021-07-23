n1_list=input()
n2_list=input()
list_1=n1_list.strip('][').split(',')
list_2=n2_list.strip('][').split(',')
list_one=[]
list_two=[]
for x in list_1:
    list_one.append(int(x))
for y in list_2:
    list_two.append(int(y))
list_one=list_one[:-1]
list_three=list_one+list_two
print(list_three)