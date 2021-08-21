def individul_bonus_calculation(val_1,val_2,val_3,val_4):
    if val_3>=30:
        earn=(val_3*(val_4/100)*val_2)+10000
    elif val_3>=20 and val_3<30:
        earn = (val_3 * (val_4 / 100) * val_2) + 5000
    else:
        earn = (val_3 * (val_4 / 100) * val_2)

    print(f"{val_1} earned a bonus of {int(earn)} Taka for {val_3} goals.")


individul_bonus_calculation('Luis', 80000, 25, 10)