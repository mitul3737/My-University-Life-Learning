class Person:
    species='Homo Sapiens' #class variables
    count=0


    def __init__(self,name,age):
        self.name=name
        self.age=age
        Person.count+=1 # count will be increased all the time the class is called and it enters __init__

    def display(self):
        print(f'{self.name} is {self.age} years old')


p1=Person('John',20)
p2=Person('Jack',34)

print(Person.species)
print(p1.species)
print(p2.species)

#same id as it is a class variable and is availabe fromsame address
print(id(Person.species))
print(id(p1.species))
print(id(p2.species))
