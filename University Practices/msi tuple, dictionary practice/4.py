dict_0={'w': 50, 'x': 100, 'y': 'Green', 'z': 400}
dict_1={'x': 300, 'y': 'Red', 'z': 600}
new_dict={}
for i in dict_0.keys():
    new_dict[i]=[dict_0[i]]
for j in dict_1.keys():
    if j in dict_0.keys():
        new_dict[j].append(dict_1[j])
print(new_dict)





