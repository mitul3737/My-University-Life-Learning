dict_0={1:['.',',','?','!',':'],2:['a','b','c'],3:['d','e','f'],4:['g','h','i'],5:['j','k','l'],6:['m','n','o'],7:['p','q','r','s'],8:['t','u','v'],9:['w','x','y','z'],0:[" "]}
str_0="Hello, World!".lower()
dict_1={}
str_1=""
str_2=""
for i in str_0:
   for j in dict_0.keys():
         if i  in dict_0[j]:
             ind=(dict_0[j].index(i))+1
             for l in range(0,ind):
                 str_1+=str(j)

                 dict_1[i]=str_1

             str_1=""


for g in str_0:
    str_2+=dict_1[g]

print(str_2)