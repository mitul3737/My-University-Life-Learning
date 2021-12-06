class Student:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    @staticmethod
    def statMethod():
        print('This is a static metod')


Student.statMethod()