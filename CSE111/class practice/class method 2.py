class Student:
    uni_Name='BRACU'
    def __init__(self,name,id,dept):
        self.name=name
        self.__id=id
        self.dept=dept
        print(self.name,"object created")

    def details(self):
        print("Name: ",self.name,"ID:",self.__id,'University Name:',Student.uni_Name)


    @classmethod
    def up_uniname(cls,uni):
        cls.uni_Name=uni
    @classmethod
    def from_string(cls,info):
        name,id,dept=info.split('-')
        return cls(name,id,dept) #it then returns this value to object which means s2=Student(name,id)

    #instance method
    def up_uniname(self,un_ni):
        self.uni_Name=un_ni

st1=Student('Alice',15126727,'CSE')
st2=Student.from_string("Jahan-12435878-BBA")
st1.details()
st2.details()