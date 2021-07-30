#link: https://replit.com/@appbrewery/day-4-3-exercise

# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
num=input("Where do you want to put the treasure? ")
list_1=[]
list_1.append(int(num[1]))
list_1.append(int(num[0]))

num1=list_1[0]-1
num2=list_1[1]-1
map[num1][num2]='X'

print(f"{row1}\n{row2}\n{row3}")