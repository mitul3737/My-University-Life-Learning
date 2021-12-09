class Laptop:
    laptopCount=0
    def __init__(self,name,count):
        self.name=name
        self.count=count
        Laptop.laptopCount+=count

    @classmethod
    def advantage(cls):
        return("Laptops are portable")

    @classmethod
    def resetCount(cls):
        cls.laptopCount=0
        return cls.laptopCount




lenovo = Laptop("Lenovo", 5)
dell = Laptop("Dell", 7)
print(lenovo.name, lenovo.count)
print(dell.name, dell.count)
print("Total number of Laptops", Laptop.laptopCount)
Laptop.advantage()
Laptop.resetCount()
print("Total number of Laptops", Laptop.laptopCount)
