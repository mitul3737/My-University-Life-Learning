str_0=input("")
low_0=""
upp_0=""
odd_0=""
even_0=""

for i in str_0:
    if  i.islower():
        low_0+=i
    elif i.isupper():
        upp_0+=i
    elif i.isdigit():
         if int(i)%2==0:
            even_0+=i
         else:
             odd_0+=i


def sort_my_str(x):
    str_01=""
    x=sorted(x)
    for i in x:
        str_01+=i
    return str_01


low_0=sort_my_str(low_0)
upp_0=sort_my_str(upp_0)
odd_0=sort_my_str(odd_0)
even_0=sort_my_str(even_0)

final_str=low_0+upp_0+odd_0+even_0

print(final_str)
