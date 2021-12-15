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

class CSEfresher(CSEstudent):
    def enroll_CSE(self):
        print("Enrolled in CSE110")

s1=CSEstudent("Bob",11,3)
s2=CSEfresher("Carol",55,1)
s1.details()
s2.details()

