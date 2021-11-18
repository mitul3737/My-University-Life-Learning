class Avengers():
    def __init__(self,name_1,name_2):
        self.name_1=name_1
        self.name_2=name_2
    def super_powers(self,*sup_pow):
        str_0 = ""
        str_1 = ""
        str_0 = str(sup_pow)
        lst_0 = str_0.strip(")(").split(", ")
        for i in range(len(lst_0)):
            if lst_0[i][-2] == "'":
                str_1 += lst_0[i][1:-2] + ","
                str_1 += " "
            else:
                str_1 += lst_0[i][1:-1] + ','
                str_1 += " "
        self.sup_pow = str_1[:-2]
    def printAvengersDetail(self):
        print(f"Name: {self.name_1}")
        print(f"Partner: {self.name_2}")
        print(f"Super powers: {self.sup_pow}")

a1 = Avengers('Captain America', 'Bucky Barnes')
a1.super_powers('Stamina', 'Slowed ageing')
a2 = Avengers('Doctor Strange', 'Ancient One')
a2.super_powers('Mastery of magic')
a3 = Avengers('Iron Man', 'War Machine')
a3.super_powers('Genius level intellect', 'Scientist ')
print("=========================")
a1.printAvengersDetail()
print("=========================")
a2.printAvengersDetail()
print("=========================")
a3.printAvengersDetail()
print("=========================")