class Product:
    def __init__(self):
        self.data1=10
        self._data2=20 #private variable
    def methodA(self):
        pass
    def _methodB(self): #private method
        pass


p=Product()
print(dir(p)) #_data2', '_methodB', 'data1', 'methodA'
print(p._data2) #accessing the private method