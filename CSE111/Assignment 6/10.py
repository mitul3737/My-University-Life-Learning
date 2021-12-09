class SultansDine:
    branch=0
    sell_t=0
    list_0=[]

    def __init__(self,branch,sell=0):
        self.branch=branch
        self.sell=sell
        SultansDine.branch+=1


    @classmethod
    def details(cls):
        print(f"Total Number of branch(s): {SultansDine.branch}\nTotal Sell: {SultansDine.sell_t} Taka")
        str_0 = ""
        if SultansDine.list_0!=[]:
            for i in SultansDine.list_0:
                if i[0]!=SultansDine.list_0[-1][0]:
                   str_0 += f"Branch Name: {i[0]}, Branch Sell: {i[1]} Taka\nBranch consists of total sell's: {round((i[1] / SultansDine.sell_t) * 100, 2)}%\n"
                else:
                    str_0 += f"Branch Name: {i[0]}, Branch Sell: {i[1]} Taka\nBranch consists of total sell's: {round((i[1] / SultansDine.sell_t) * 100, 2)}%"
        if str_0!="":
            print(str_0)


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
        SultansDine.list_0.append([self.branch,self.sell])



    def branchInformation(self):
        print(f"Branch Name: {self.branch}\nBranch Sell: {self.sell} Taka")





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