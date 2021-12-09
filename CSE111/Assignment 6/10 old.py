class SultansDine:
    branch=0
    sell_t=0
    str_0=""
    dict_0={}

    def __init__(self,branch,sell=0):
        self.branch=branch
        self.sell=sell
        SultansDine.branch+=1


    @classmethod
    def details(cls):
        print(f"Total Number of branch(s): {SultansDine.branch}\nTotal Sell: {SultansDine.sell_t} Taka")

    def sellQuantity(self,sell):

        if sell<10:
             self.sell = 300 * sell
             SultansDine.sell_t += self.sell
        elif sell<20:
             self.sell = 350 * sell
             SultansDine.sell_t += self.sell
        else:
            self.sell = 400 * sell
            SultansDine.sell_t += self.sell

        SultansDine.dict_0[self.branch]=self.sell

    def branchInformation(self):
        for i,j in SultansDine.dict_0.items():
            SultansDine.str_0+=f"Branch Name:{i}, Branch Sell: {j} Taka \nBranch consists of total sell's: {round((j/SultansDine.sell_t)*100,2)}%\n"
        print(SultansDine.str_0)
        SultansDine.str_0=""



SultansDine.details()
print('########################')
dhanmodi = SultansDine('Dhanmondi')
dhanmodi.sellQuantity(25)
dhanmodi.branchInformation()
print('-----------------------------------------')
SultansDine.details()
print('========================')
baily_road = SultansDine('Baily Road')
baily_road.sellQuantity(15)
baily_road.branchInformation()
print('-----------------------------------------')
SultansDine.details()
print('========================')
gulshan = SultansDine('Gulshan')
gulshan.sellQuantity(9)
gulshan.branchInformation()
print('-----------------------------------------')
SultansDine.details()