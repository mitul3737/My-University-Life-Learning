class Assassin:
    total=0
    def __init__(self,name,rate):
        self.name=name
        self.rate=rate
        Assassin.total+=1

    def   printDetails(self):
          print(f'Name: {self.name}\nSuccess rate: {self.rate}%\nTotal number of Assassin: {Assassin.total}')




    @classmethod
    def failureRate(cls,name,f_rate):
        name=name
        rate=100-int(f_rate)
        return cls(name,rate)

    @classmethod
    def failurePercentage(cls,name,f_rate):
        name = name
        rate = 100 - int(f_rate)
        return cls(name, rate)

john_wick = Assassin('John Wick', 100)
john_wick.printDetails()
print('================================')
nagisa = Assassin.failureRate("Nagisa", 20)
nagisa.printDetails()
print('================================')
akabane = Assassin.failurePercentage('Akabane', 10)
akabane.printDetails()