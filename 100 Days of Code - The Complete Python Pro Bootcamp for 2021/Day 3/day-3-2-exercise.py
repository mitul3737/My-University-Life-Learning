#Link: https://replit.com/@appbrewery/day-3-2-exercise
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi=weight/(height*height)
bmi=round(bmi)

if bmi<=18.5:
   print(f"Your BMI is {bmi}, you are underweight.")
elif bmi>18.5 and bmi<=25:
   print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi>25  and bmi<=30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi>30 and bmi<=35:
  print(f"Your BMI is {bmi}, you are obese.")
elif bmi>35:
  print(f"Your BMI is {bmi}, you are clinically obese.")



