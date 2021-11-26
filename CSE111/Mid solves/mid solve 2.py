class Chocolates:
    def __init__(self):
        self.dict={'White':[],'Daek':[]}
        self.count=0
        self.white=[]
        self.dark=[]


    def print_info(self):
        if self.count==0:
            print(f"Number of chocolates : {self.count}")
        else:
            print(f"Number of chocolates : {self.count}")
            if self.white!=[]:
                print(f"White: {self.white}")
            if self.dark!=[]:
                print(f"Dark: {self.dark}")

    def update_info(self,var):
        if var.type=="White":
            self.count+=1
            self.white.append([var.name,var.flav,var.ing])
        elif var.type=="Dark":
            self.count+=1
            self.dark.append([var.name,var.flav,var.ing])



class White:
    def __init__(self,name,type="White",flav="Plain",*ing):
        self.name=name
        self.type=type
        self.flav=flav
        self.ing=ing

    def print_info(self):
        print(f"Name: {self.name}\nType: {self.type}\nFlavor: {self.flav}\nIngredients: {self.ing}")


class Dark:
    def __init__(self,name,type="Dark",flav="Plain",*ing):
        self.name = name
        self.type = type
        self.flav = flav
        self.ing = ing
    def print_info(self):
        print(f"Name: {self.name}\nType: {self.type}\nFlavor: {self.flav}\nIngredients: {self.ing}")


# Write you code here
Choco = Chocolates()
print("*********************************************")
Choco.print_info()
print("1================================")
c1 = White("Dairy Milk")
c1.print_info()
print("2================================")
Choco.update_info(c1)
Choco.print_info()
print("3================================")
c2 = White("Hershey's","White", "Hazelnut","milk","sugar")
c2.print_info()
print("4================================")
Choco.update_info(c2)
Choco.print_info()
print("5================================")
c3 = Dark("Galaxy","Dark","Wafer")
c4 = Dark("Kitkat")
print("6================================")
c3.print_info()
print("7================================")
c4.print_info()
print("8================================")
Choco.update_info(c3)
Choco.update_info(c4)
print("9================================")
Choco.print_info()
print("10================================")
c5 = Dark("Dairy Milk", "White", "Plain","milk","sugar")
Choco.update_info(c5)
Choco.print_info()



"""CHOCOLATES!
*********************************************
Number of chocolates : 0
1================================
Name: Dairy Milk
Type: White
Flavor: Plain
Ingredients: ()
2================================
Number of chocolates : 1
White: [['Dairy Milk', 'Plain', ()]]
3================================
Name: Hershey's
Type: White
Flavor: Hazelnut
Ingredients: ('milk', 'sugar')
4================================
Number of chocolates : 2
White: [['Dairy Milk', 'Plain', ()], ["Hershey's", 'Hazelnut',
('milk', 'sugar')]]
5================================
6================================
Name: Galaxy
Type: Dark
Flavor: Wafer
Ingredients: ()
7================================
Name: Kitkat
Type: Dark
Flavor: Plain
Ingredients: ()
8================================
9================================
Number of chocolates : 4
White: [['Dairy Milk', 'Plain', ()], ["Hershey's", 'Hazelnut',
('milk', 'sugar')]]
Dark: [['Galaxy', 'Wafer', ()], ['Kitkat', 'Plain', ()]]
10================================
Number of chocolates : 5
White: [['Dairy Milk', 'Plain', ()], ["Hershey's", 'Hazelnut',
('milk', 'sugar')]]
Dark: [['Galaxy', 'Wafer', ()], ['Kitkat', 'Plain',"""



"""5 [This is the number of advertisements that will be given as input.]
Dhanmondi 1209 9A 128 1700sqft 45000
Mirpur 1216 6B 10 1700sqft 23000
Dhanmondi 1209 4A 43 2000sqft 40000
Gulshan 1212 7C 102 2300sqft 60000
Mirpur 1216 5A 103 2000sqft 33000"""