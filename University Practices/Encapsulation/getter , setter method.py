class Student:
    def __init__(self, name, ID):
        self.name = name
        self.__id = ID

    def details(self):
        print("Name:", self.name, "Id:", self.__id)

    def UpId(self, Id):
        if (Id > 0):
            self.__id = Id
        else:
            print("Invalid ID, enter ID again")

    # getter method
    def get_Id(self):
        return self.__id

    def get_name(self):
        return self.name
        # setter method

    def set_name(self, name):
        self.name = name


s1 = Student("bob", 11)
s2 = Student("Mitul", 13)

s1.UpId(66)
s1.details()
s2.details()
