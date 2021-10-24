list_0=input()
list_1=list_0.strip('][').split(',')
#[1,2,3,4,5] to [1,2,3,4,5]

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

"""[1,2,3,4]
[5,6,7,8] to [1,2,3,4] &[5,6,7,8]"""
