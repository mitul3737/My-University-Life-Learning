class MyClass():
    a=5
    def __init__(self,x):
        self._x=x

    def method1(self):
        print(self.x)

    #class method
    @classmethod
    def method2(cls): #cls refers to class object
        print(cls.a)


MyClass.method2()#calling class method (prints 5)