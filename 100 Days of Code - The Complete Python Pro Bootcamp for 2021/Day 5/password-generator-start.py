#Link: https://replit.com/@appbrewery/password-generator-start

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password=""
for x in range(1,nr_letters+1):
  random_p=random.choice(letters)
  password+=random_p
for x in range(1,nr_symbols+1):
  random_s=random.choice(symbols)
  password+=random_s
for x in range(1,nr_numbers+1):
  random_n=random.choice(numbers)
  password+=random_n


print(f"Easy Password: {password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password=[]
for x in range(1,nr_letters+1):
  random_p=random.choice(letters)
  password.append(random_p)
for x in range(1,nr_symbols+1):
  random_s=random.choice(symbols)
  password.append(random_s)
for x in range(1,nr_numbers+1):
  random_n=random.choice(numbers)
  password.append(random_n)



random.shuffle(password)

n_password=""
for x in password:
  n_password+=x

print(f"Hard Password: {n_password}")

