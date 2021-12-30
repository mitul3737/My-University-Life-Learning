class Account:
    count=0
    def __init__(self,name,age,occ,money):
        self.name=name
        self.age=age
        self.occ=occ
        self.money=money
        Account.count+=1
    def addMoney(self,val):
        self.money+=val
    def printDetails(self):
        print(f"Name: {self.name}\nAge: {self.age}\nOccupation:  {self.occ}\nTotal Amount:  {self.money}")

    def withdrawMoney(self,val_0):
        if self.money<val_0:
            self.money=self.money
        else:
            self.money-=val_0

print('No of account holders:', Account.count)
print("=========================")
p1 = Account("Abdul", 45, "Service Holder", 500000)
p1.addMoney(300000)
p1.printDetails()
print("=========================")
p2 = Account("Rahim", 55, "Businessman", 700000)
p2.withdrawMoney(700000)
p2.printDetails()
print("=========================")
p3 = Account("Ashraf", 62, "Govt. Officer", 200000)
p3.withdrawMoney(250000)
p3.printDetails()
print("=========================")
print('No of account holders:', Account.count)

"""No of account holders: 0
=========================
Name: Abdul
Age: 45
Occupation:  Service Holder
Total Amount:  800000
=========================
Name: Rahim
Age: 55
Occupation:  Businessman
Total Amount:  0
=========================
Name: Ashraf
Age: 62
Occupation:  Govt. Officer
Total Amount:  200000
=========================
No of account holders: 3
"""