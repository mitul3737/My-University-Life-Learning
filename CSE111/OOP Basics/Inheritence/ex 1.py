class Person:
    def __init__(self,name,age,address,phone):
        self.name=name
        self.age=age
        self.address=address
        self.phone=phone

    #instance method
    def greet(self):
        print('Hello I am',self.name)

    def is_adult(self):
         if self.age>18:
             return True
         else:
              return False

    def contact_details(self):
         print(self.address,self.phone)

#inherited from Person claass
class Employee(Person):
    def __init__(self,name,age,address,phone,salary,office_address,office_phone):

        super().__init__(name,age,address,phone) #using from Person init
        #or, Person.__init__(self,name,age,address,phone)  #using from Person init
        '''or, self.name=name
        self.age=age
        self.address=address
        self.phone=phone'''
        self.salary=salary
        self.office_address=office_address
        self.office_phone=office_phone


    def calculate_tax(self):
        if self.salary<5000:
            return 0
        else:
            return self.salary*0.05

    def contact_details(self):
         super().contact_details()#Person.contact_details() or, print(self.address,self.phone)  using from Person contact details()
         print(self.office_address,self.office_phone)


emp=Employee('Jack',30,'D4, XYZ Street, Delhi','994477291',8000,'ABC street , dhaka','896738383')


'''print(emp.age)
print(emp.address)
print(emp.phone)

print(isinstance(emp,Employee))#check if emp is an instance of Employee class
print(isinstance(emp,Person))

print(issubclass(Employee,Person))#Employee is a subclass of Person
print(issubclass(Person,object)) #Person is a subclass of object . Almost everything is subclass of object
print(issubclass(str,object))
print(issubclass(int,object))'''



"""print(emp.calculate_tax())
print(emp.contact_details())"""