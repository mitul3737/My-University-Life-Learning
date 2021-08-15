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