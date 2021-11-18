class Programmer():
    def __init__(self,name,lang,exp):
        print("Horray! A new programmer is born")
        self.name=name
        self.lang=lang
        self.exp=exp
    def printDetails(self):
        print(f'Name: {self.name}')
        print(f'Language: {self.lang}')
        print(f'Experience: {self.exp}')
    def addExp(self,add_exp):
        print(f"Updating experience of {self.name}")
        self.exp+=add_exp


p1 = Programmer("Ethen Hunt", "Java", 10)
p1.printDetails()
print('--------------------------')
p2 = Programmer("James Bond", "C++", 7)
p2.printDetails()
print('--------------------------')
p3 = Programmer("Jon Snow", "Python", 4)
p3.printDetails()
p3.addExp(5)
p3.printDetails()