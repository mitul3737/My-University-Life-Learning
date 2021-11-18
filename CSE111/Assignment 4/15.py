class Account():
    def __init__(self,name="Default Account",balance=0.00):
         self.name=name
         self.balance=balance

    def details(self):
         return f"{self.name} \n{self.balance}"


    def withdraw(self,w_bal):
        if self.balance>=int(w_bal):
            self.balance=self.balance-int(w_bal)
            print(f"Withdraw successful! New balance is: {self.balance}")
        else:
            print("Sorry, Withdraw unsuccessful! The account balance after deducting withdraw amount is equal to or less than minimum.")

a1 = Account()
print(a1.details())
print("------------------------")
a1.name = "Oliver"
a1.balance = 10000.0
print(a1.details())
print("------------------------")
a2 = Account("Liam")
print(a2.details())
print("------------------------")
a3 = Account("Noah",400)
print(a3.details())
print("------------------------")
a3.withdraw(6930)
print("------------------------")
a2.withdraw(600)
print("------------------------")
a1.withdraw(6929)