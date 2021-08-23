dict_1 = dict_1 = {"N":(4,9,3),"k":[95,37,197],"F":(32,5,97),"s":[31,94,55]}
dict_n={}
for i in dict_1.keys():
     if ord(i)>=97 and ord(i)<=122:
         print(i)
         lst_p=[]
         for j in dict_1[i]:
             #print(f"again: {j}")
             lst_q = []
             for k in range(2,j):
                 if j%k==0:
                   lst_q.append(k)
                 #print(f"lst_q {lst_q}")
                 #print(len(lst_q))
             if len(lst_q) == 0:
                 #print("ok")
                 lst_p.append(j)
                 print(f"lst_p: {lst_p}")
         dict_n[i]=lst_p
     else:
         tup_p = ()
         for j in dict_1[i]:
             print(j)
             print(f"again: {j}")
             tup_q = ()
             for k in range(2, j):
                 if j % k == 0:
                    n_tup=(j,)
                    tup_q+=n_tup
                # print(f"lst_q {lst_q}")
                # print(len(lst_q))
             if len(tup_q) == 0:
                 # print("ok")
                 tup_p+=(j,)
                 print(f"tup_q: {tup_p}")
         dict_n[i] = tup_p


print(dict_n)