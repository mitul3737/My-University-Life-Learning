class Product:
    def __init__(self):
        self.data1=10
        self._data2=20 #protected variable
    def methodA(self):
        pass
    def _methodB(self): #private method
        print("Hello to private method")


p=Product()
print(dir(p)) #_data2', '_methodB', 'data1', 'methodA'
print(p._data2) #accessing the protected variable
p._methodB()