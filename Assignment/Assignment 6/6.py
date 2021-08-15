val_1=int(input(""))
def function_name(val_1):
    years=val_1//365
    months=((val_1%365))//30
    days=(((val_1%365))%30)
    print(f"{years} years, {months} months and {days} days")
print(function_name(val_1))