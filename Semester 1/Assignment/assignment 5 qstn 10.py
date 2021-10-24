val_0={'sci fi': 12, 'mystery': 15, 'horror': 8, 'mythology': 10, 'young_adult': 4, 'adventure':14} #will work for any dictionary

for i in val_0.keys():
    max=val_0[i]
    break;

for i in val_0.keys():
    if val_0[i]>=max:
        max=val_0[i]
        ind=i

print(f"The highest selling book genre is '{ind}' and the number of books sold are {max}.")