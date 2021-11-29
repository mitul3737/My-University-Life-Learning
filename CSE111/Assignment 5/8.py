class Coordinates:
    def __init__(self,val_1,val_2):
        self.__val_1=val_1
        self.__val_2=val_2
    def detail(self):
        return (self.__val_1,self.__val_2)

    def __mul__(self, other):
        return Coordinates(self.__val_1*other.__val_1,self.__val_2*other.__val_2)

    def __sub__(self, other):
        return Coordinates(self.__val_1-other.__val_1,self.__val_2-other.__val_2)

    def __eq__(self, other):
        if self.detail()==other.detail():
            return "The calculated coordinates are the same."
        else:
            return "The calculated coordinates are NOT the same."



#Write your code here
#Do not change the following lines of code
p1 = Coordinates(int(input()),int(input()))
p2 = Coordinates(int(input()),int(input()))
p4 = p1 - p2
print(p4.detail())
p5 = p1 * p2
print(p5.detail())
point_check = (p4 == p5)
print(point_check)
