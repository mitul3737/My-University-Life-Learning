class Calculator:
    def __init__(self, fir_1, sec_2, thir_3):
        self.fir_1 = int(fir_1)
        self.sec_2 = sec_2
        self.thir_3 = int(thir_3)
        print("Let’s Calculate!")
        print("Value 1:", self.fir_1)
        print("Operator:", self.sec_2)
        print("Value 2:", self.thir_3)
        if (self.sec_2) == "+":
            self.add()
        elif (self.sec_2) == "-":
            self.subtract()
        elif (self.sec_2) == "*":
            self.multiply()
        else:
            self.divide()

    def add(self):
        print("Result: ", self.fir_1 + self.thir_3)

    def subtract(self):
        print("Result:", self.fir_1 - self.thir_3)

    def multiply(self):
        print("Result:", self.fir_1 * self.thir_3)

    def divide(self):
        print("Result:", self.fir_1 / self.thir_3)


ls_0 = []

for i in range(3):
    ls_0.append(input(""))
op = Calculator(ls_0[0], ls_0[1], ls_0[2])

