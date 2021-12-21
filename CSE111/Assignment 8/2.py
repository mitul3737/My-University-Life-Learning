class RealNumber:
    def __init__(self, number=0):
        self.number = number

    def __add__(self, anotherRealNumber):
        return self.number + anotherRealNumber.number

    def __sub__(self, anotherRealNumber):
        return self.number - anotherRealNumber.number

    def __str__(self):
        return str(self.number)


class ComplexNumber(RealNumber):
    def __init__(self, number1, number2):
        self.number = number1
        self.complex = number2

    def __add__(self, otherComplex):
        return f'{self.real + otherComplex.real} + {self.comp + otherComplex.comp}i'

    def __sub__(self, otherComplex):
        return f'{self.real - otherComplex.real} - {abs(self.comp - otherComplex.comp)}i'

    def __str__(self):
        self.real = int(super().__str__())
        self.comp = int(self.complex)
        return f'{self.real} + {self.comp}i'


r1 = RealNumber(3)
r2 = RealNumber(5)
print(r1 + r2)
cn1 = ComplexNumber(2, 1)
print(cn1)
cn2 = ComplexNumber(r1, 5)
print(cn2)
cn3 = cn1 + cn2
print(cn3)
cn4 = cn1 - cn2
print(cn4)

"""8
2 + 1i
3 + 5i
5 + 6i
-1 - 4i"""