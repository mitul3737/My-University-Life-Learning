class Person:
    species='Homo Sapiens' #class variables
    count=0


    def __init__(self,name,age):
        self.name=name
        self.age=age
        Person.count+=1 # count will be increased all the time the class is called and it enters __init__

    def display(self):
        print(f'{self.name} is {self.age} years old')

    @classmethod
    def show_count(cls):
        print(f'There are {cls.count} {cls.species}')


Person.show_count() #check before instances call
p1=Person('John',20)
p2=Person('Jack',34)
Person.show_count() #calling after instance call

