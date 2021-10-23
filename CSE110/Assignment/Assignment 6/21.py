def function_name(*args):
    for i in range(0,len(args),4):
        val_1=args[i]
        val_2=args[i+1]
        val_3 = args[i + 2]
        val_4 = args[i + 3]
        individul_bonus_calculation(val_1,val_2,val_3,val_4)



def individul_bonus_calculation(val_1,val_2,val_3,val_4):
    if val_3>=30:
        earn=(val_3*(val_4/100)*val_2)+10000
    elif val_3>=20 and val_3<30:
        earn = (val_3 * (val_4 / 100) * val_2) + 5000
    else:
        earn = (val_3 * (val_4 / 100) * val_2)

    print(f"{val_1} earned a bonus of {int(earn)} Taka for {val_3} goals.")


function_name("Neymar", 1200000, 35, 5, 'Jamal', 700000, 19, 8, 'Luis', 80000, 25, 10)