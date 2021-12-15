class Student:
    def __init__(self,name,ID):
        self.name=name
        self.id=ID
    def details(self):
       print("Nmae:",self.name,"ID:",self.id)

class CSEstudent(Student):
    def __init__(self,name,Id,labs):
       super().__init__(name,Id)#calling the Parent class's __init__ method and gave the input so we have self.name=name, self.id=Id
       self.no_of_labs=labs
    def cry(self):
       print("CSE Student crying bcause of",self.no_of_labs,"labs")

class BBAstudent(Student):
    def party(self):
        print("All day party")




s1=CSEstudent("Bob",11,3)
s2=BBAstudent("carlo",36)
s1.details()
s2.details()
s1.cry()
s2.party()
"""print(help(s1))
print(help(s2))"""