class PlayerEarning:
    def __init__(self, name):
        self.name = name

    def calculateTotal(self, value, goal=0):
        self.value = value
        self.goal = goal

    def printDetails(self):
        if self.goal != 0:
            if self.goal > 30:
                self.bonus = (5 / 100) * self.value + 10000
            else:
                self.bonus = (5 / 100) * self.value
        else:
            self.bonus = 0

        print(
            f"Player Name: {self.name}\nPlayer Season Earning without bonus: {self.value}\nBonus: {int(self.bonus)}\nPlayer Season Earning After Bonus: {int(self.bonus + self.value)}")


print("**********************")
player1 = PlayerEarning('Buffon')
player1.calculateTotal(250000)
player1.printDetails()

print("\n**********************")
player2 = PlayerEarning('Dybala')
player2.calculateTotal(250000, 31)
player2.printDetails()

print("\n**********************")
player3 = PlayerEarning('Cuadrado')
player3.calculateTotal(250000, 20)
player3.printDetails()

"""**********************
Player Name: Buffon
Player Season Earning without bonus: 250000
Bonus: 0
Player Season Earning After Bonus: 250000

**********************
Player Name: Dybala
Player Season Earning without bonus: 250000
Bonus: 22500
Player Season Earning After Bonus: 272500

**********************
Player Name: Cuadrado
Player Season Earning without bonus: 250000
Bonus: 12500
Player Season Earning After Bonus: 262500
"""