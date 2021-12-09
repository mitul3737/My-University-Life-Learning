class Cat:
    Number_of_cats=0

    def __init__(self,color,work):
        self.color=color
        self.work=work
        Cat.Number_of_cats+=1

    @classmethod
    def no_parameter(cls):
        color="White"
        work="sitting"
        return cls(color,work)

    @classmethod
    def first_parameter(cls,f_p):
        color=f_p
        return cls(f_p,"sitting")

    @classmethod
    def second_parameter(cls,s_p):
        work=s_p
        return cls("Grey",work)



    def printCat(self):
        print(f"{self.color} cat is {self.work}")

    def changeColor(self,new_cc):
        self.color=new_cc



print("Total number of cats:", Cat.Number_of_cats)
c1 = Cat.no_parameter()
c2 = Cat.first_parameter("Black")
c3 = Cat("Brown", "jumping")
c4 = Cat("Red", "purring")
c5 = Cat.second_parameter("playing")
print("=======================")
c1.printCat()
c2.printCat()
c3.printCat()
c4.printCat()
c5.printCat()
c1.changeColor("Blue")
c3.changeColor("Purple")
c1.printCat()
c3.printCat()
print("=======================")
print("Total number of cats:", Cat.Number_of_cats)
