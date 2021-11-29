#Do not change the following lines of code
class Marks:
    def __init__(self,mark):
        self.mark=mark



    def __add__(self, other):
        return Marks(self.mark+other.mark)


Q1 = Marks(int(input("Quiz 1 (out of 10): ")))
Q2 = Marks(int(input("Quiz 2 (out of 10): ")))
Lab = Marks(int(input("Lab (out of 30): ")))
Mid = Marks(int(input("Mid (out of 20): ")))
Final = Marks(int(input("Final (out of 30): ")))
total = Q1 + Q2 + Lab + Mid + Final
print("Total marks: {}".format(total.mark))



'''if they would give : print(Q1 + Q2 + Lab + Mid + Final) then would need to use 
    def __str__(self):
        return "{}".format(self.mark) as there are handling strings which was previously written as under print("Total marks: {}".format(total.mark)'''