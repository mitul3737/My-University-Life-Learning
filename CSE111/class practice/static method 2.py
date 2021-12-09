class Student:
    uni_name="BRACU"

    def __init__(self,name,id):
        self.name=name
        self.__id=id


    # instance method
    def details(self):
        print("Name:",self.name,"ID:",self.__id,Student.uni_name)


    @classmethod
    def up_uni_name(cls,u_name):
        cls.uni_name=u_name

    @staticmethod
    def check_department(Id):
        if Id[3:5]=="01":print("CSE")
        elif Id[3:5]=="47":print("CS")


s1=Student("Bob",11)
s2=Student("Motin",47)
s1.details()
s2.details()
#staticmethod is not specific for class or instance. it is open for all and thus it is different than instance method and class method
Student.check_department("20001547") #works for class
s1.check_department("20047547") #works for instance or object
s2.check_department("134015890")  #works for instance or object