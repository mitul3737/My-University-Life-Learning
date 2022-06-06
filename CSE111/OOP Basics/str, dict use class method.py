class Person:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(f'I am {self.name},{self.age} years old')

    @classmethod
    def from_str(cls,s):
        name,age=s.split(',')
        return cls(name,int(age))

    @classmethod
    def from_dict(cls,d):
        return cls(d['name'],d['age'])


p1=Person('John',20)
p2=Person('Jack',34)

#using string to initialize
s='Jim, 23' #string
p3=Person.from_str(s)
p3.display()

#using dictionary to initialize
d={'name':'Jane','age':34} #dictionary
p4=Person.from_dict(d)
p4.display()

