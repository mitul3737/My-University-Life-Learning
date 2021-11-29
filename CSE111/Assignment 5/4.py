class Color:
    def __init__(self,clr=None):
        self.clr=clr

    def __add__(self, other):
         if self.clr=="red" or other.clr=="red":
             if self.clr=="red" and other.clr=="yellow":

                 return Color("Orange")#returning it to constructor , so that it then gets self.clr=Orange and when we call C3.clr, we get this value
             else:

                 return Color("Violet")

         elif  self.clr=="blue" or other.clr=="blue":
            if self.clr=="blue" and other.clr=="yellow":

                return Color("Green")
            else:

                return Color("Violet")

         elif  self.clr=="yellow" or other.clr=="yellow":
             if self.clr=="yellow" and other.clr=="red":

                 return Color("Orange")
             else:

                 return  Color("Green")




#Do not change the following lines of code

C1 = Color(input("First Color: ").lower())
C2 = Color(input("Second Color: ").lower())
C3 = C1 + C2
print("Color formed:", C3.clr)