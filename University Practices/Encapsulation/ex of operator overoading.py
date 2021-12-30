class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self): #if asked to print string type
        return "({0},{1})".format(self.x, self.y)

    def __add__(self, other): #works for + opetator
        x = self.x + self.y
        y = other.x + other.y
        return Point(x, y)


p1 = Point(1, 6)#worked for self
p2 = Point(9, 3)#other

print(p1+p2)#as p1 is first so self is for p1 and p2 gets others

