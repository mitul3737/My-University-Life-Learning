lst_0=[]
lst_1=[]
lst_2=[]
sub_lst=[]
avl_lst=[]
team_play=0
for i in range(0,2):
    str_0=input("").split(" ")
    lst_0.append(str_0)


for j in lst_0:
    for k in j:
        lst_1.append(int(k))
    lst_2.append(lst_1)
    lst_1=[]


for m in range(0,lst_2[0][0]):
    sub_lst.append(5-lst_2[1][m])


for n in sub_lst:
    if n>=lst_2[0][1]:
        avl_lst.append(n)


team_play=len(avl_lst)//3
print(team_play)



