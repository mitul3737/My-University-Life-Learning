def rem_duplicate(val_1):
    comp=(val_1[0],)
    for i in range(len(val_1)):
        if val_1[i] not in comp:
            comp_1=(val_1[i],)
            comp=comp+comp_1

    print(comp)

rem_duplicate(("Hi", 1, 2, 3, 3, "Hi",'a', 'a', [1,2]))



'''def rem_duplicate(val_1):
    comp=(val_1[0],)
    for i in range(len(val_1)):
        if val_1[i] not in comp:
            comp_1=(val_1[i],)
            comp=comp+comp_1

    return comp

print(rem_duplicate(("Hi", 1, 2, 3, 3, "Hi",'a', 'a', [1,2])))'''