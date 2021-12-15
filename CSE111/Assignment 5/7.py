class Dolls:
   def __init__(self,name,price):
       self.__name=name
       self.__price=price


   def detail(self):
       return f"Doll: {self.__name}\nTotal Price: {self.__price} taka"


   def __add__(self, other):
        self.__name=self.__name+" "+other.__name
        self.__price=self.__price+other.__price
        return Dolls(self.__name,self.__price)

   def __gt__(self, other):
       if self.__price>=other.__price:
          return True
       else:
          return False


# Write your code here
obj_1 = Dolls("Tweety", 2500)
print(obj_1.detail())
if obj_1 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")
print("=========================")
obj_2 = Dolls("Daffy Duck", 1800)
print(obj_2.detail())
if obj_2 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")
print("=========================")
obj_3 = Dolls("Bugs Bunny", 3000)
print(obj_3.detail())
if obj_3 > obj_1:
   print("Congratulations! You get the Tweety as a gift!")
else:
   print("Thank you!")
print("=========================")
obj_4 = Dolls("Porky Pig", 1500)
print(obj_4.detail())
if obj_4 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")
print("=========================")
obj_5 = obj_2 + obj_3
print(obj_5.detail())
if obj_5 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")


"""
Doll: Tweety
Total Price: 2500 taka
Thank you!
=========================
Doll: Daffy Duck
Total Price: 1800 taka
Thank you!
=========================
Doll: Bugs Bunny
Total Price: 3000 taka
Congratulations! You get the Tweety as a gift!
=========================
Doll: Porky Pig
Total Price: 1500 taka
Thank you!
=========================
Dolls: Daffy Duck Bugs Bunny
Total Price: 4800 taka
Congratulations! You get the Tweety as a gift!"""