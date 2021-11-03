mit_0=input("").strip(")(").split(",")
num3=int(mit_0[0])
num4=int(mit_0[1])

def fraction(num1,num2):
    if num1==0 or num2==0:
        res=0
    else:
        fract = num1 / num2
        fract_0 = num1 // num2
        res = fract - fract_0

    return res

print(fraction(num3,num4))