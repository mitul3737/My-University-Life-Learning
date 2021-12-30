"""Implement the HogwartsQuidditchSquad class derived from the Squad class
with necessary variables and methods so that the expected output is
generated. Do not change any given code.

[Hint: In order to form a squad, you need at least 5 members. And in order
to form a perfect squad you need 2 beaters, 1 seeker, 1 chaser and 1
keeper. ]"""

class Squad:
     playerCount=0
     def __init__(self,name,squadType):
         self.name = name
         self.squadType = squadType
     def formSquad(self):
         if Squad.playerCount >= 5:
             return True
         else:
             return False
     def __str__(self):
         s = f"{self.name} is a {self.squadType} team.\n"
         s+= f"Number of players in {self.name} is {Squad.playerCount}\n"
         return s

#Write your code here
class HogwartsQuidditchSquad(Squad):
    player_info={}
    perfect_squad={"Beater":2,"Seeker":1,"Chaser":1,"Keeper":1}
    check_squad=[]
    check_squad_d={}
    flag=False
    def __init__(self,name,squadType):
        super().__init__(name,squadType)

    def addPlayer(self,*args):
        for i in args:
            if i[1] not in HogwartsQuidditchSquad.player_info:
                 HogwartsQuidditchSquad.player_info[i[1]]=f"Player name: {i[0]}, House: {i[2]}"
                 Squad.playerCount+=1
            else:#note
                HogwartsQuidditchSquad.player_info[i[1]]= f"Player name: {i[0]}, House: {i[2]}"
                Squad.playerCount += 1


    def formSquad(self):
        HogwartsQuidditchSquad.check_squad=[]
        if super().formSquad():
            for x in HogwartsQuidditchSquad.player_info.keys():
                HogwartsQuidditchSquad.check_squad.append(x)
            for y in HogwartsQuidditchSquad.check_squad:
                if y not in HogwartsQuidditchSquad.check_squad_d:
                    HogwartsQuidditchSquad.check_squad_d[y]=HogwartsQuidditchSquad.check_squad.count(y)
            for o in HogwartsQuidditchSquad.perfect_squad.keys():
                for k in HogwartsQuidditchSquad.check_squad_d.keys():
                    if o==k:
                        if HogwartsQuidditchSquad.perfect_squad[o]==HogwartsQuidditchSquad.check_squad_d[k]:
                            flag=True


            if flag:
                print("We have enough players to form a squad.\nAlso we can form a perfect squad!!")
            else:
                print("We have enough players to form a squad.\nBut we cannot form a perfect squad.")
    def __str__(self):
        super().__str__()
        print("The Players are:")
        for a in HogwartsQuidditchSquad.player_info.keys():
            return f"{a}:\n{HogwartsQuidditchSquad.player_info[a]}"



f = HogwartsQuidditchSquad("Hogwart's Dragons","Quidditch")
f.addPlayer(["Harry Potter","Seeker","Gryffindor"],["KatieBell","Chaser","Gryffindor"])
print("1.====================================")
print(f)
print("2.====================================")
f.formSquad()
print("3.====================================")
f.addPlayer(["Vincent Crabbe","Beater","Slytherin"])
f.addPlayer(["Miles Bletchley","Keeper","Slytherin"])
print("4.====================================")
print(f)
print("5.====================================")
f.formSquad()
print("6.====================================")
f.addPlayer(["Ethan Humberstone","Keeper","Hufflepuff"])
f.formSquad()
print("7.====================================")
f.addPlayer(["Fred Weasley","Beater","Gryffindor"])
print(f)
print("8.====================================")
f.formSquad()

"""1.====================================
Hogwart's Dragons is a Quidditch team.
Number of players in Hogwart's Dragons is 2
The Players are:
Seeker:
Player name: Harry Potter, House: Gryffindor
Chaser:
Player name: Katie Bell, House: Gryffindor
2.====================================
We do not have enough players to form a squad.
3.====================================
4.====================================
Hogwart's Dragons is a Quidditch team.
Number of players in Hogwart's Dragons is 4
The Players are:
Seeker:
Player name: Harry Potter, House: Gryffindor
Chaser:
Player name: Katie Bell, House: Gryffindor
Beater:
Player name: Vincent Crabbe, House: Slytherin
Keeper:
Player name: Miles Bletchley, House: Slytherin
5.====================================
We do not have enough players to form a squad.
6.====================================
We have enough players to form a squad.
But we cannot form a perfect squad.
7.====================================
Hogwart's Dragons is a Quidditch team.
Number of players in Hogwart's Dragons is 6
The Players are:
Seeker:
Player name: Harry Potter, House: Gryffindor
Chaser:
Player name: Katie Bell, House: Gryffindor
Beater:
Player name: Vincent Crabbe, House: Slytherin
Player name: Fred Weasley, House: Gryffindor
Keeper:
Player name: Miles Bletchley, House: Slytherin
Player name: Ethan Humberstone, House: Hufflepuff
8.====================================
We have enough players to form a squad.
Also we can form a perfect squad!!"""

