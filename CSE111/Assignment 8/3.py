class Account:

    def __init__(self, balance):
        self._balance = balance

    def getBalance(self):
        return self._balance

    def __str__(self):
        return f"Account Balance: {self.getBalance()}"


class CheckingAccount(Account):
    numberOfAccount = 0

    def __init__(self, val=0.0):
        super().__init__(val)
        CheckingAccount.numberOfAccount += 1


print('Number of Checking Accounts: ', CheckingAccount.numberOfAccount)
print(CheckingAccount())
print(CheckingAccount(100.00))
print(CheckingAccount(200.00))
print('Number of Checking Accounts: ', CheckingAccount.numberOfAccount)

"""
Number of Checking
Accounts: 0
Account Balance: 0.0
Account Balance: 100.00
Account Balance: 200.00
Number of Checking
Accounts: 3
"""