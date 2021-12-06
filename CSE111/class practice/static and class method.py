class Student:
    def __init__(self,name,id,dept):
        self.name=name
        self.id=id
        self.dept=dept


    @staticmethod
    #no  parameter of its own
    def stat_Method():
        print("This is  a static method")


    @classmethod
    def class_method(cls):
        print("This is a class method")
        cls.studentNum = 100 #can modify class variables in class method
        cls.stat_Method() #can call static methods

    #instance method
    def details(self):
        print(self.name,'with id',self.id,'and dept',self.dept)






st1=Student("Alice",1234,'CSE')
st2=Student('Karim',1245,'BBA')
Student.class_method()
