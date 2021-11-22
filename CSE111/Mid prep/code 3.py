class ShoppingCart():
    def __init__(self,name):
        self.comp=name
        self.lst=[]
        self.dict={}
        self.cost=0

    def  addGadget(self,*args):
         for i in range(0,len(args),2):
             new=[]
             new.append(args[i])
             for j in new:
                 if j.quant>=args[i+1]:
                     self.dict[j.prod]=f"Gadget:{j.name} Model:{j.prod} Price:{j.price}$ Quantity:{args[i+1]} Stock:{j.quant} pcs"
                     self.cost+=j.price*args[i+1]
                 else:
                     print(f"{j.prod} stock is less than required quantity. Cannot add to cart.")





    def printCartDetails(self):
        for l in self.dict.values():
            print(l)
        print(f"Total cost of cart: {self.cost}$")




class Product():
     def __init__(self,prod,name,price,quant=0):
         self.prod=prod
         self.name=name
         self.price=price
         self.quant=quant




#Write your code here
s1 = ShoppingCart("Amazon")
p1 = Product("Razer BlackShark","Headset",99.99,5)
p2 = Product("Logitech G ProX Superlight","Mouse",150)
print("1.====================================")
s1.addGadget(p1,2,p2,1)
print("2.====================================")
p3 = Product("Razer Huntsman", "Keyboard", 249.99,12)
s1.addGadget(p3,1)
s1.addGadget(Product("HyperX Fury","Mousepad",26.99,1), 2)
print("3.====================================")
s1.printCartDetails()

"""Output:
1.================================
Logitech G ProX Superlight stock is less than required quantity. Cannot add
to cart.
2.================================
HyperX Fury stock is less than required quantity. Cannot add to cart.
3.================================
Details of Amazon cart:
Total gadgets in cart: 2
Gadget:Headset Model:Razer BlackShark Price:99.99$ Quantity:2 Stock:5 pcs
Gadget:Keyboard Model:Razer Huntsman Price:249.99$ Quantity:1 Stock:12 pcs
Total cost of cart: 449.97$"""