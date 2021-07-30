import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("What do you choose? Type  0 for Rock, 1 for Paper oro 2 for Scissors")
num = int(input(""))
if num == 0:
    print(f"You chose: {rock}")
elif num == 1:
    print(f"You chose: +{paper}")
else:
    print(f"You chose: {scissors}")

num2 = random.randint(0, 2)

if num2 == 0:
    print(f"Computer chose: {rock}")
    if num2 == num:
        print("Match Draw")
    elif num == 1:
        print("You win")
    else:
        print("You lose")

if num2 == 1:
    print(f"Computer chose: {paper}")
    if num2 == num:
        print("Match Draw")
    elif num == 2:
        print("You win")
    else:
        print("You lose")

if num2 == 2:
    print(f"Computer chose: {scissors}")
    if num2 == num:
        print("Match Draw")
    elif num == 0:
        print("You win")
    else:
        print("You lose")
