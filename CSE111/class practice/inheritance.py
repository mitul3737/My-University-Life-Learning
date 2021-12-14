class parent:
    def __init__(self):
        print("Constructor of parent")
    def method1(self):
        print("method1 of parent ")
    def method2(self):
        print("method2 of parent ")

class child1(parent):#inherits its parents
    def __init__(self):
        print("constructor of child1")
    def method3(self):
        print("method of child1")
    def method4(self):
        print("method of child2")

class child2(parent):
    def __init__(self):
        print("constructor of child2")
    def method5(self):
        print("method of child2")
    def method6(self):
        print("method of child2")

class grandchild(child1,child2,parent):
    def __init__(self):
        super().__init__()#calling the left most variables constructor . here as child1
        print("constuctor of grandchild")
    def method7(self):
        print("method of grandchild")
    def method8(self):
        print("method of grandchild")

p=grandchild()
p.method1()# as grandchild inherits parent
