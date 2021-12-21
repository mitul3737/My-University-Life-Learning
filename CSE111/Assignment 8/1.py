class RealNumber:
    def __init__(self, r=0):
        self.__realValue = r

    def getRealValue(self):
        return self.__realValue

    def setRealValue(self, r):
        self.__realValue = r

    def __str__(self):
        return 'RealPart: ' + str(self.getRealValue())


class ComplexNumber(RealNumber):
    def __init__(self, real=1, comp=1):
        super().setRealValue(real)
        self.comp = comp

    def __str__(self):
        return f'RealPart: {str(float(self.getRealValue()))}\nImaginaryPart: {str(float(self.comp))}'


cn1 = ComplexNumber()
print(cn1)
print('---------')
cn2 = ComplexNumber(5, 7)
print(cn2)

"""RealPart: 1.0
ImaginaryPart: 1.0
--------------------
RealPart: 5.0
ImaginaryPart: 7.0"""