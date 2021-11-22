class TechShop:
    def __init__(self, cname):
        self.dic = {}
        self.cname = cname

    def addProduct(self, *args):

        #doing works while adding
        for elm in args:
            if elm.code != None:
                self.dic[elm.item] = f"Catagory:{elm.catagory} Product Code:{elm.code}"
                print(f"Product with Code:{elm.code} added")
            else:
                print("A product without code cannot be added")

    def printProducts(self):
        for k, v in self.dic.items():
            print("Product name:" + k + " " + str(v))


class Product:
    def __init__(self, item, catagory, code=None):
        self.item = item
        self.catagory = catagory
        self.code = code



    def setCode(self, code):
        self.code = code


# Write your code here
obj = TechShop("Star Tech")
p1 = Product("Core i7 11700", "Processor", 16039)
print("=================================")
obj.addProduct(p1)
print("=================================")
obj.printProducts()
print("=================================")
p2 = Product("Ryzen 5900X", "Processor")
p3 = Product("ASRock B550 Taichi", "Motherboard", 18080)
print("=================================")
obj.addProduct(p2, p3)
print("=================================")
obj.printProducts()
print("=================================")
p2.setCode(17699)
print("=================================")
obj.addProduct(p2)
print("=================================")
obj.printProducts()
print("=================================")
p4 = Product("ASUS ROG Strix Z390-F", "Motherboard", 8694)
p5 = Product("ASUS ROG Strix RTX3080", "GPU", 17071)
print("=================================")
obj.addProduct(p4, p5)
print("=================================")
obj.printProducts()
print("=================================")