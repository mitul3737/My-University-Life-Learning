#Link: https://replit.com/@appbrewery/day-3-5-exercise

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1=name1.lower()
name2=name2.lower()
t_count=name1.count("t")+name2.count("t")
r_count=name1.count("r")+name2.count("r")
u_count=name1.count("u")+name2.count("u")
e_count=name1.count("e")+name2.count("e")

l_count=name1.count("l")+name2.count("l")
o_count=name1.count("o")+name2.count("o")
v_count=name1.count("v")+name2.count("v")
e_count=name1.count("e")+name2.count("e")

tot_1=t_count+r_count+u_count+e_count
tot_2=l_count+o_count+v_count+e_count

tot_3=str(tot_1)+str(tot_2)
tot3=int(tot_3)


if tot3<10 or tot3>90:
  print(f"Your score is {tot3}, you go together like coke and mentos.")
elif tot3>40 and tot3<=50:
  print(f"Your score is {tot3}, you are alright together.")
else:
  print(f"Your score is {tot3}.")


