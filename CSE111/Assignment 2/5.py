mit_0=input("").strip(")(").split(",")
str_3=mit_0[0][1:-1]
str_4=mit_0[1][2:-1]
if len(mit_0)==3:
    str_5=mit_0[2][2:-1]





def replace_domain(check_0,new_domain,old_domain="sheba.xyz"):
    find_0=check_0.find('@')
    if new_domain==old_domain:
        print(f"Unchanged: {check_0}")
    else:
        mail_0=check_0[:find_0]+'@'+new_domain
        print(f"Changed: {mail_0}")


if len(mit_0)==3:
     replace_domain(str_3,str_4,str_5)
else:
    replace_domain(str_3,str_4)



