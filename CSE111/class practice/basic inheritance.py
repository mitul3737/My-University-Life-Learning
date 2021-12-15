class Animal:
    def __init__(self,name):
        self.name=name
    def eat(self):
        print(self.name,"is eating")

class Dog(Animal):
    def bark(self):
       print(self.name,"is barking")


a1=Animal("Jack")
d1=Dog("Rover")
d1.bark()