class Batsman():
    def __init__(self,name,runs_s=0,ball_f=0):
        if type(name) == str:
            self.name = name
            self.runs_s = runs_s
            self.ball_f = ball_f
        else:
            self.name = "New Batsman"
            self.runs_s = name
            self.ball_f = runs_s


    def printCareerStatistics(self):
        print(f"Name: {self.name}")
        print(f"Runs Scored: {self.runs_s} , Balls Faced: {self.ball_f}")
    def battingStrikeRate(self):
        return (self.runs_s/self.ball_f )*100
    def setName(self,s_name):
        self.name=s_name

b1 = Batsman(6101, 7380)
b1.printCareerStatistics()
print("============================")
b2 = Batsman("Liton Das", 678, 773)
b2.printCareerStatistics()
print("----------------------------")
print(b2.battingStrikeRate())
print("============================")
b1.setName("Shakib Al Hasan")
b1.printCareerStatistics()
print("----------------------------")
print(b1.battingStrikeRate())
