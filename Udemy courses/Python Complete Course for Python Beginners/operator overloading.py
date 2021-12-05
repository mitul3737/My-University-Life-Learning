class myPoint:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    def __str__(self): #if there is any string value passed, we then use this
        return "({0},{1})".format(self.x,self.y)

    def __add__(self, other):
        x=self.x+other.x
        y=self.y+other.y
        return myPoint(x,y)

    def __lt__(self, other):
        self_mag=(self.x**2)+(self.y**2)
        other_mag=(other.x**2)+(other.y**2)
        return self_mag < other_mag  #if self_mag < other_mag then will return True


p1=myPoint(1,2)
p2=myPoint(4,5)
print(p1)
print(p2)
print(p1<p2)
print(p1+p2)
print(p1.__lt__(p2))
print(p2.__lt__(p1))