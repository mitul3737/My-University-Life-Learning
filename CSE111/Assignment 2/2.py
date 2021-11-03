mit_0=input("").strip(")(").split(",")
num3=int(mit_0[0])
num4=int(mit_0[1])


def BMI(height, weight):
    height_m=float(height/100)
    bmi=weight/((height_m)*(height_m))
    bmi=round(bmi,1)
    if bmi< 18.5:
        print(f"Score is {bmi}. You are Underweight")
    elif bmi<=24.9:
        print(f"Score is {bmi}. You are Normal")
    elif bmi<=30:
        print(f"Score is {bmi}. You are Overweight")
    else:
        print(f"Score is {bmi}. You are Obese")

BMI(num3,num4)