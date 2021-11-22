
class OlympicCountry():
    def __init__(self,cname):
        self.cname=cname
        self.dict={"Gold":[],"Silver":[],"Bronze":[]}
        self.count=0




    def add_player(self,*args):
        for i in args: #we are getting the address (by reference) i is a address and from that address we are just calling the varibales of Awardedplayer functiion()
            # to use something from this class we will use self but to use from oter we will use i  as self
            if i.award!=None:
                self.dict[i.award].append(i.name)
                self.count+=1

            else:
                print("A player must have a medal. Add the medal first")

    def show_medal_info(self):
        print(f"Total medals won by {self.cname} is {self.count}")
        print("**")
        for k,v in self.dict.items():
            print(k,v)



class AwardedPlayer():
      def __init__(self,name,award=None):
          self.name=name
          self.award=award

      def add_medal(self,award1):
          self.award=award1




country1 = OlympicCountry('Jamaica')
country2 = OlympicCountry('USA')
player1 = AwardedPlayer('Usain Bolt')
player2 = AwardedPlayer('Shelly-Ann Fraser-Pryce','Silver')
player3 = AwardedPlayer('Elaine Thompson Herah','Gold')
player4 = AwardedPlayer('Michael Phelps','Gold')
player5 = AwardedPlayer('Caeleb Dressel','Gold')
print('-----------------------------------------')
country1.add_player(player1)
print('-----------------------------------------')
player1.add_medal('Gold')
country1.add_player(player1)
country1.add_player(player2)
country1.add_player(player3)
print('-----------------------------------------')
country1.show_medal_info()
print('-----------------------------------------')
country2.add_player(player4)
country2.add_player(player5)
print('-----------------------------------------')
country2.show_medal_info()

"""Expected Output:
-----------------------------------------
A player must have a medal. Add the medal first
-----------------------------------------
-----------------------------------------
Total medals won by Jamaica is 3
**
Gold ['Usain Bolt', 'Elaine Thompson Herah']
Silver ['Shelly-Ann Fraser-Pryce']
Bronze []
-----------------------------------------
-----------------------------------------
Total medals won by USA is 2
**
Gold ['Michael Phelps', 'Caeleb Dressel']
Silver []
Bronze []"""

