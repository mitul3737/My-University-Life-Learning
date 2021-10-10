class Product:
    def __init__(self,x,y):
        self._x=x
        self._y=y

    def display(self):
        print(self._x,self._y)

    @property  #getter method
    def value(self):
        return self._x

    @value.setter #setter method
    def value(self,val):
        self._x=val


p=Product(12,34)


print(dir(Product))
print(p.value)

p.value=190
print(p.value)