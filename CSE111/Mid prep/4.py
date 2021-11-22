class Team():
    def __init__(self,count):
        self.name=count
        self.dict={"Batsman":[],"Bowler":[]}


    def addPlayer(self,*args):
        for i in args:
            if i.p_stat!=None:
                print(f"{i.p_name} added in team ")
                self.dict[i.p_stat].append(f"Player name: {i.p_name} Jersey No: {i.p_code}")
            else:
               print("A player cannot be added without a role.")

    def showPlayers(self):
        for k,v in self.dict.items():
            if v!=[]:
                print(f"{k}:")
                for x in v:
                    print(x)





class Player():
    def __init__(self,name,stat=None,code=0):
        self.p_name=name
        self.p_stat=stat
        self.p_code=code

        if type(self.p_stat)==int:
            self.p_code=self.p_stat
            self.p_stat=None







    def setRole(self,role):
        self.p_stat=role

#Write your code here
team = Team("Bangladesh")
p1 = Player("Mahmudullah", "Batsman",30)
print("=================================")
team.addPlayer(p1)
print("=================================")
team.showPlayers()
print("=================================")
p2 = Player("Mustafizur Rahman", "Bowler",90)
p3 = Player("Tamim Iqbal", 28)
print("=================================")
team.addPlayer(p2,p3)
print("=================================")
team.showPlayers()
print("=================================")
p3.setRole("Batsman")
print("=================================")
team.addPlayer(p3)
print("=================================")
team.showPlayers()
print("=================================")
p4 = Player("Mushfiqur Rahim", "Batsman",15)
p5 = Player("Taskin Ahmed", "Bowler",3)
print("=================================")
team.addPlayer(p4,p5)
print("=================================")
team.showPlayers()


"""Expected Output:
=================================
Mahmudullah added in team
=================================
Batsman:
Player name: Mahmudullah Jersey No: 30
=================================
=================================
Mustafizur Rahman added in team
A player cannot be added without a role.
=================================
Batsman:
Player name: Mahmudullah Jersey No: 30
Bowler:
Player name: Mustafizur Rahman Jersey No: 90
=================================
=================================
Tamim Iqbal added in team
=================================
Batsman:
Player name: Mahmudullah Jersey No: 30
Player name: Tamim Iqbal Jersey No: 28
Bowler:
Player name: Mustafizur Rahman Jersey No: 90
=================================
=================================
Mushfiqur Rahim added in team
Taskin Ahmed added in team
=================================
Batsman:
Player name: Mahmudullah Jersey No: 30
Player name: Tamim Iqbal Jersey No: 28
Player name: Mushfiqur Rahim Jersey No: 15
Bowler:
Player name: Mustafizur Rahman Jersey No: 90
Player name: Taskin Ahmed Jersey No: 3"""