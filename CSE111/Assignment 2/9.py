str_0=input("")[2:-2]

def grammarly_bracu(sentence):
    lst_0=[".","!","?"]
    lst_1=[]# inexes of /,/?
    lst_2=[]
    lst_3=[] # I indexes
    lst_4=[]# list of indexes already changed
    str_1=""
    for i in range(0,len(sentence)):
        if sentence[i] in lst_0:
            lst_1.append(i)
        elif sentence[i]=="i":
             lst_2.append(i)
    for j in lst_2:
        if sentence[j-1]==" " and sentence[j+1]==" ":
            lst_3.append(j)
    #print(lst_3)
    str_1 = sentence[0].upper()
    for k in range(1,len(sentence)):

        if k in lst_1 and k!=len(sentence)-1:

            if sentence[k + 1] == " ":
                str_1+=sentence[k]
                #print(sentence[k])
                str_1+=sentence[k+1]
                #print(sentence[k+1])
                str_1+= sentence[k + 2].upper()
                #print(sentence[k+2].upper())
                #print(str_1)
                lst_4.append(k+1)
                lst_4.append(k+2)
            else:
                str_1 += sentence[k]
                #print(sentence[k])
                str_1+= sentence[k + 1].upper()
                #print(sentence[k+1].upper())

                lst_4.append(k+1)
        elif k in lst_3 : # making I upper case
            if k not in lst_4: # check if after . /, ? there is I already made upper case or not
                     str_1 += sentence[k].upper()
                     lst_4.append(k)
                     #print(sentence[k].upper())
        elif k not in lst_4:
            str_1 += sentence[k]

    return str_1




print(grammarly_bracu(str_0))
