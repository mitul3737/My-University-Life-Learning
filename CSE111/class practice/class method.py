
class Student:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    @staticmethod
    def statMethod():
        print('This is a static metod')

    @classmethod
    def classMethod(cls):
        print('This is a class method!')
        cls.statMethod()


st1=Student("Alice",1234)
st1.classMethod()
