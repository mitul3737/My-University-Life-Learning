class Player:
    playerNo=0
    database={}
    playerNo = 0
    def __init__(self,name,team,jerseyNo):
        self.name = name
        self.team = team
        self.jerseyNo = jerseyNo
        Player.playerNo+=1
    def __str__(self):
        return "Name:{}\nTeam:{}\nJersey No:{}".format(self.name,self.team,self.jerseyNo)
class  FootballPlayer(Player):
    def __init__(self,name,team,jersey,goal,reti="Not yet retired"):
       super().__init__(name,team,jersey)
       self.id=""
       self.id+=str(Player.playerNo)
       for i in self.name.split(" "):
           self.id+=i[0]
       self.id+=str(self.jerseyNo)
       self.goal=goal
       self.ret=reti
       Player.database[self.id]=[self.name,self.team,self.jerseyNo,self.goal,self.ret]
    def __str__(self):
        return f"Player ID:{self.id}\nName:{self.name}\nTeam:{self.team}\nJersey No:{self.jerseyNo}\nGoals Scored:{self.goal}\nRetirement date:{self.ret}"

    @staticmethod
    def createPlayer(name,team,jersey,goal,reti="Not yet retired"):
        return FootballPlayer(name,team,jersey,goal,reti)


#Write your code here

print("Number of players:",Player.playerNo)
print("Player Database:",Player.database)
print("#################################")
p1 = FootballPlayer("Lionel Messi","Barcelona",10,231)
print("------Details of the player------")
print(p1)
print("#################################")
p2 = FootballPlayer("Cristiano Ronaldo","Juventus",7,215)
print("------Details of the player------")
print(p2)
print("#################################")
p3 = FootballPlayer.createPlayer("Miroslav Klose","Lazio",11, 71,"11 Aug,2014")
print("------Details of the player------")
print(p3)
print("#################################")
print("Number of players:",Player.playerNo)
print("Player Database:",Player.database)

"""Number of players: 0
Player Database: {}
#################################
------Details of the player------
Player ID:1LM10
Name:Lionel Messi
Team:Barcelona
Jersey No:10
Goals Scored:231
Retirement date:Not yet retired
#################################
------Details of the player------
Player ID:2CR7
Name:Cristiano Ronaldo
Team:Juventus
Jersey No:7
Goals Scored:215
Retirement date:Not yet retired
#################################
------Details of the player------
Player ID:3MK11
Name:Miroslav Klose
Team:Lazio
Jersey No:11
Goals Scored:71
Retirement date:11 Aug,2014
#################################
Number of players: 3
Player Database: {'1LM10': ['Lionel Messi', 'Barcelona', 10, 231, 'Not yet retired'], '2CR7': ['Cristiano Ronaldo', 'Juventus', 7, 215, 'Not yet retired'], '3MK11': ['Miroslav Klose', 'Lazio', 11, 71, '11 Aug,2014']}
"""