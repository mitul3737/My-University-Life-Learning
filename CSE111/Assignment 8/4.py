class Fruit:
    def __init__(self, formalin=False, name=''):
        self.__formalin = formalin
        self.name = name

    def getName(self):
        return self.name

    def hasFormalin(self):
        return self.__formalin


class testFruit:
    def test(self, f):
        print('----Printing Detail----')
        if f.hasFormalin():
            print('Do not eat the', f.getName(), '.')
            print(f)
        else:
            print('Eat the', f.getName(), '.')
            print(f)


class Mango(Fruit):
    def __init__(self, name="Mango"):
        super().__init__(True, name)

    def __str__(self):  # the object created gets these value
        return "Mangos are bad for you"


class Jackfruit(Fruit):
    def __init__(self, name="Jackfruit"):
        super().__init__(False, name)

    def __str__(self):  # the object created gets these value
        return "Jackfruits are good for you"


m = Mango()
j = Jackfruit()
t1 = testFruit()
t1.test(m)
t1.test(j)

"""
----Printing Detail-----
Do not eat the Mango.
Mangos are bad for you
----Printing Detail-----
Eat the Jackfruit.
Jackfruits are good for you
"""