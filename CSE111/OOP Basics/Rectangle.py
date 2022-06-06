'''
class Rectangle():
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
        self.diagonal=(self.length*self.length+self.breadth*self.breadth)**0.5


    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)





r=Rectangle(2,5)
print(r.diagonal)
print(r.area())
print(r.perimeter())


r.length=10 # if we change the length
print(r.area()) #area changes
print(r.perimeter()) # perimeter changes
print(r.diagonal) # remains same
reason: methods has changed their values but instances or variales did not . like area(), perimeter() did change but length, breadth, diagonal did not change0'''


'''Solving this issue with @property:::'''


class Rectangle():
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    @property
    def diagonal(self):
        return (self.length*self.length+self.breadth*self.breadth)**0.5


    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)





r=Rectangle(2,5)
print(r.diagonal)
print(r.area())
print(r.perimeter())


r.length=10 # if we change the length
print(r.area()) #area changes
print(r.perimeter()) # perimeter changes
print(r.diagonal) # Now this is updated after using @property

