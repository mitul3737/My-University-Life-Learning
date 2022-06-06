class Product:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def display(self):
        print(self._x, self._y)

    @property  # to get any value using this method written  a variable ex: object.method or, p.value not like p.value()
    def value(self):
        return self._x

    @value.setter  # to set a function to assign value
    def value(self, val):
        self._x = val

    # while we delete a value,this method will be applied ex: del p.value
    @value.deleter
    def value(self):
        print('Value  deleted')


p = Product(12, 24)
