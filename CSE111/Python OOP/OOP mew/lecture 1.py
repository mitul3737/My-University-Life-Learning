class Person:
    def set_details(self,n1,a1):
        self.name=n1 #sel
        self.age=a1
    def display(self):
        print('I am a ',self.name)
    def greet(self):
        if self.age<80:
            print("Hello, how are you?",self)
        else:
            print("Why me old?")
        self.display()

p1=Person()
p2=Person()

p1.set_details('Mitul',22)
p2.set_details('Royena',90)


p1.greet()

p2.greet()

print(p1.name)
print(p1.age)

print(p2.name)
print(p2.age)