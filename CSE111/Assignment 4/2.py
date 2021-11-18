class Customer():
    def __init__(self,name):
        self.name=name

    def greet(self,name=None):
        if name==None:
            print("Hello!")
        else:
            print(f"Hello {name}!")

    def purchase(self,*val):
        var=str(val)
        if var.count(',')>1:
            var=var.strip(")(").split(", ")
        else:
            var=var.strip(")(").split(",")
        print(f"{self.name}, you purchased {len(var)} item(s):")

        for i in range(len(var)):
            print(var[i][1:-1])



customer_1 = Customer("Sam")
customer_1.greet()
customer_1.purchase("chips", "chocolate", "orange juice")
print("-----------------------------")
customer_2 = Customer("David")
customer_2.greet("David")
customer_2.purchase("orange juice")
