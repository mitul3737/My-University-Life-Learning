from math import pi as p
class Cylinder:
    radius=5
    height=18
    def __init__(self,new_r,new_h):
        self.new_r=new_r
        self.new_h=new_h
        print(f"Default radius={Cylinder.radius} and height={Cylinder.height}.")
        print(f"Updated: radius={self.new_r} and height={self.new_h}.")
        Cylinder.radius=new_r
        Cylinder.height=new_h

    @staticmethod
    def area(x_0,y_0):
        print(f"Area: {2 *p*(float(x_0)**2)+2* p * float(x_0) *float(y_0)}")

    @staticmethod
    def volume(x_1,y_1):
        print(f"Volume: {p* (float(x_1)**2)*float(y_1)}")

    @classmethod
    def swap(cls,height_0,radius_0):
        return cls(radius_0,height_0)
    @classmethod
    def changeFormat(cls,hola):
        rad,height=hola.split("-")
        return cls(float(rad),float(height))


c1 = Cylinder(0,0)
Cylinder.area(c1.radius,c1.height)
Cylinder.volume(c1.radius,c1.height)
print("===============================")
c2 = Cylinder.swap(8,3)
c2.area(c2.radius,c2.height)
c2.volume(c2.radius,c2.height)
print("===============================")
c3 = Cylinder.changeFormat("7-13")
c3.area(c3.radius,c3.height)
c3.volume(c3.radius,c3.height)
print("===============================")
Cylinder(0.3,5.56).area(Cylinder.radius,Cylinder.height)
print("===============================")
Cylinder(3,5).volume(Cylinder.radius,Cylinder.height)