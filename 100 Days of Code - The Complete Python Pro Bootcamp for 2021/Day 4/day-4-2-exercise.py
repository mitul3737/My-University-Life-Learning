#Link: https://replit.com/@appbrewery/day-4-2-exercise

# Split string method
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
size=len(names)
rand_t=random.randint(0,size-1)
print(f"{names[rand_t]} is going to buy the meal today!")
