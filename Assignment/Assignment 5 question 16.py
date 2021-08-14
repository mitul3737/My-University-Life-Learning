val_1={'c1':'Red', 'c2':'Green', 'c3':None, 'd4':'Blue', 'a5':None}
val_2={}
for i in val_1.keys():
    if val_1[i]!=None:
        val_2[i]=val_1[i]

print(val_2)
