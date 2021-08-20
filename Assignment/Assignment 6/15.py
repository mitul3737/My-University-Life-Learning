def function_name(val_1,loc="Dhanmondi"):
    val_0 = {"Rice": 105, "Potato": 20, "Chicken": 250, "Beef": 510, "Oil": 85}
    total = 0
    for i in val_1:
        if i in val_0.keys():
            total += val_0[i]
    if loc != "Dhanmondi":
        total += 70
    elif loc == "Dhanmondi":
        total += 30

    print(total)

function_name(["Rice", "Beef", "Rice"], "Mohakhali")



'''def function_name(val_1,loc="dhanmondi"):
    val_x=val_1.strip("][").split(",")
    val_2=[]
    for j in range(len(val_x)):
        if j==0:
           val_2.append(val_x[j][1:-1])
        else:
            val_2.append(val_x[j][2:-1])

    val_0 = {"Rice": 105, "Potato": 20, "Chicken": 250, "Beef": 510, "Oil": 85}
    total = 0
    for i in val_2:
        if i in val_0.keys():
            total += val_0[i]

    if loc_1 == "dhanmondi" or loc_1=="":
         print("prob")
         total += 30
    else:
         total += 70

    return total

value=input("")
loc_1=input("")
loc_1=loc_1.lower()
print(function_name(value,loc_1))'''