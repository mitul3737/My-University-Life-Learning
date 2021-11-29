import math
class Circle:
    def __init__(self,radius=0):
        self.__radius=radius

    def getRadius(self):
        return self.__radius

    def setRadius(self,var):
        self.__radius=var

    def area(self):
        self.__area=math.pi*self.__radius*self.__radius
        return self.__area

    def __mul__(self, other):
        return self.__radius*other.__radius
    def __add__(self, other):
        return  Circle(self.__radius+other.__radius)

# Write your code here for subtasks 1-5

c1 = Circle(4)
print("First circle radius:" , c1.getRadius())
print("First circle area:" ,c1.area())
c2 = Circle(5)
print("Second circle radius:" ,c2.getRadius())
print("Second circle area:" ,c2.area())
c3 = c1 + c2
print("Third circle radius:" ,c3.getRadius())
print("Third circle area:" ,c3.area())


"""
First circle radius: 4
First circle area: 50.26548245743669
Second circle radius: 5
Second circle area:
78.53981633974483
Third circle radius: 9
Third circle area:
254.46900494077323"""