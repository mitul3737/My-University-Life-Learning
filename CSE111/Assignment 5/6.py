class Triangle:
    def __init__(self,var,var_1):
        self.__base=var
        self.__height=var_1
    def getBase(self):
        return self.__base
    def area(self):
        self.__area=0.5*self.__base*self.__height
        return self.__area
    def __mul__(self, other):
        return self.__base*self.__height
    def getHeight(self):
        return self.__height
    def setBase(self,var_1):
         self.__base=var_1
    def setHeight(self,var_2):
        self.__height=var_2
    def __sub__(self, other):
        if self.__base>other.__base:
            self.__base=self.__base-other.__base
        else:
            self.__base=other.__base-self.__base
        if self.__height>other.__height:
            other.__height=self.__height-other.__height
        else:
            self.__height=other.__height-self.__height

        return Triangle(self.__base,other.__height)

# Write your code here for subtasks 1-5

t1 = Triangle(10, 5)
print("First Triangle Base:" , t1.getBase())
print("First Triangle Height:" , t1.getHeight())
print("First Triangle area:" ,t1.area())
t2 = Triangle(5, 3)
print("Second Triangle Base:" , t2.getBase())
print("Second Triangle Height:" , t2.getHeight())
print("Second Triangle area:" ,t2.area())
t3 = t1 - t2
print("Third Triangle Base:" , t3.getBase())
print("Third Triangle Height:" , t3.getHeight())
print("Third Triangle area:" ,t3.area())



"""
First Triangle Base: 10
First Triangle Height: 5
First Triangle area: 25.0
Second Triangle Base: 5
Second Triangle Height: 3
Second Triangle area: 7.5
Third Triangle Base: 5
Third Triangle Height: 2
Third Triangle area: 5.0"""