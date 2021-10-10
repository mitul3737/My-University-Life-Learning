
class Person:
    def __init__(self,n1,a1):
        self.name=n1 #sel
        self.age=a1
    def display(self):
        print('I am a ',self.name)
    def greet(self):
        if self.age<80:
            print("Hello, how are you?",self)
        else:
            print("Why me old?")


p1=Person('mitul',20)
p2=Person('Ikramul',80)

p1.display()
p1.greet()

p2.display()
p2.greet()

