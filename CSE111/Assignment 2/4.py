mit_0=input("").strip(")(").split(",")
str_3=mit_0[0][1:-1]
if len(mit_0)==2:
    str_4=mit_0[1][2:-1]



def order(meal, location="Mohakhali"):
    dict_0={"BBQ Chicken Cheese Burger":250,"Beef Burger":170,"Naga Drums":200}
    del_chrg=0

    if location.lower()=="mohakhali":
        del_chrg=40
    else:
        del_chrg=60
    tax=dict_0[meal]*float(8/100)
    total_cost=dict_0[meal]+del_chrg+tax
    return total_cost

if len(mit_0)==2:
    print(order(str_3,str_4))
else:
    print(order(str_3))
