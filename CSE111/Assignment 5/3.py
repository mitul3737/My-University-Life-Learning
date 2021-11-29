class Team:
    def __init__(self,country=None):
        self.__country=country
        self.__lst_p=[]

    def setName(self,var):
        self.__country=var
    def addPlayer(self,var1):
        if isinstance(var1.list_p,list): # checking if we got a list
            for k in var1.list_p:
                self.__lst_p.append(k)
        elif isinstance(var1.list_p,str): #checking if we got a string
              self.__lst_p.append(var1.list_p)
    def printDetail(self):
        print("=====================")
        print(F"Team: {self.__country}\nList of Players:\n{self.__lst_p}")
        print("=====================")

class Player:
    def __init__(self,*args):
        if len(args)>1: # checking if user gives more than one value
            self.list_p=[]
            for i in args:
                self.list_p.append(i)
        elif isinstance(args[0],str):#checking if user gives a string input
            self.list_p=""
            self.list_p=args[0]


b = Team()
b.setName('Bangladesh')
mashrafi = Player("Mashrafi")
b.addPlayer(mashrafi)
tamim = Player("Tamim")
b.addPlayer(tamim)
b.printDetail()
a = Team("Australia")
ponting = Player("Ponting")
a.addPlayer(ponting)
lee = Player("Lee")
a.addPlayer(lee)
a.printDetail()


"""
=====================
Team: Bangladesh
List of Players:
['Mashrafi', 'Tamim']
=====================
=====================
Team: Australia
List of Players:
['Ponting', 'Lee']
====================="""