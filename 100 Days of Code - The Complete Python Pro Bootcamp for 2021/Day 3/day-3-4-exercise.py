#Link: https://replit.com/@appbrewery/day-3-4-exercise




# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆
bill=0
#Write your code below this line 👇
if size=="L":
  bill=25
  if add_pepperoni=="Y":
    bill+=3
  else:
    if extra_cheese=="Y":
      bill+=1
    else:
      bill+=0

if size=="M":
  bill=20
  if add_pepperoni=="Y":
    bill+=3
  else:
    if extra_cheese=="Y":
      bill+=1
    else:
      bill+=0


if size=="S":
  bill=15
  if add_pepperoni=="Y":
    bill+=2
  else:
    if extra_cheese=="Y":
      bill+=1
    else:
      bill+=0


print(f"Your final bill is: ${bill}.")

