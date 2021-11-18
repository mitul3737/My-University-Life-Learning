class Shinobi():
    def __init__(self,name,rank,salary=0,mission=0):
        self.name=name
        self.rank=rank
        self.salary=salary
        self.mission=mission
    def calSalary(self,cal_s):
        self.mission=cal_s
    def printInfo(self):
        print(f"Name: {self.name}")
        print(f"Rank: {self.rank}")
        print(f"Number of mission: {self.mission}")
        if self.rank == 'Genin':
            self.salary=self.mission*50
        elif self.rank=='Chunin':
            self.salary=self.mission*100
        else:
            self.salary=self.mission*500
        print(f"Salary: {self.salary}")
    def  changeRank(self,c_rank):
        self.rank=c_rank

naruto = Shinobi("Naruto", "Genin")
naruto.calSalary(5)
naruto.printInfo()
print('====================')
shikamaru = Shinobi('Shikamaru', "Genin")
shikamaru.printInfo()
shikamaru.changeRank("Chunin")
shikamaru.calSalary(10)
shikamaru.printInfo()
print('====================')
neiji = Shinobi("Neiji", "Jonin")
neiji.calSalary(5)
neiji.printInfo()