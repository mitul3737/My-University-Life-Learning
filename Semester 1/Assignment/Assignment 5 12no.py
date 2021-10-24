val_0 = {'A': [1, 2, 3], 'b': ['1', '2'], "c": [4, 5, 6, 7]}
sum=0
for i in val_0.keys():
    sum+=len(val_0[i])
print(sum)