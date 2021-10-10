'''Make a class that represents a bank account. Create four methods named set_details, display, withdraw and deposit.

In the set_details method, create two instance variables : name and balance. The default value for balance should be zero. In the display method, display the values of these two instance variables.

Both the methods withdraw and deposit have amount as parameter. Inside withdraw, subtract the amount from balance and inside deposit, add the amount to the balance.

Create two instances of this class and call the methods on those instances.'''


class bank_account:
    def set_details(self,name,balance=0):
        self.name=name
        self.balance=balance
    def display(self):

        print(self.name ,"has balance",self.balance)

    def withdraw(self,amount):
        if self.balance<amount:
            print(self.name," don't have sufficient balance to withdraw")
        else:
            self.balance-=amount
    def deposit(self,amount):
        self.balance+=amount


person_1=bank_account()
person_2=bank_account()

person_1.set_details('Mouly',1000)
person_2.set_details('Mitul')


person_1.display()

person_2.display()


person_1.withdraw(200)
person_2.withdraw(500)

person_1.deposit(30)
person_2.deposit(300)

person_1.display()
person_2.display()
