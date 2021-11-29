class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def compare(self,val):
        if self.age>val.age:
            print(f"{val.name} is younger than me.")
        elif self.age<val.age:
            print(f"{val.name} is older than me.")
        elif self.age==val.age:
            print(f"{val.name} is the same age as me.")

p1 = Person("Nancy", 45)

p2 = Person("Maya", 36)

p3 = Person("Allen", 45)


p1.compare(p2)
p2.compare(p1)
p1.compare(p3)
