low=0
upp=0

def function_name(val_1):
    val_1=val_1.strip("'")
    for x in val_1:
        global upp
        global low
        if x.isupper()==True:
            upp+=1
        elif x!=" ":
            low+=1



function_name((input()))
print(f"No. of Uppercase characters : {upp}")
print(f"No. of Lowercase Characters: {low}")

