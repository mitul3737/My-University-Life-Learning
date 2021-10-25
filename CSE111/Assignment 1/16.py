lst_1=[]
dict_0={}
lst_0=[]
lst_n=[]
count_0=0
try:
    for i in range(0, 2):
        str_0 = input("")
        lst_n.append(str_0)

    for i in lst_n:
        for j in i:
            if j not in dict_0.keys():
                lst_0 = [i.index(j)]
                dict_0[j] = lst_0
            else:
                dict_0[j].append(i.index(j))
            lst_0 = []

    for i in dict_0.keys():
        if dict_0[i][0] != dict_0[i][1]:
            lst_1.append("OK")

    for l in lst_1:
        if l == 'OK':
            count_0 += 1

    if count_0 == len(lst_n[0]):
        print("Those strings are anagrams.")
    else:
        print("Those strings are not anagrams.")
except:
    print("Those strings are not anagrams.")


