#Link: https://replit.com/@appbrewery/Day-7-Hangman-1-Start

word_list = ["aardvark", "baboon", "camel"]
import random
val_0=random.choice(word_list)
num_0=input("")
for i in val_0:
  if i==num_0:
    print("Right")
  else:
    print("Wrong")
