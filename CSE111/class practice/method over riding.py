class parent:
    def __init__(self):
        print("Constructor of parent")
    def method1(self):
        print("method1 of parent ")
    def method2(self):
        print("method2 of parent ")

class child1(parent):#inherits its parents

    def method3(self):
        super().method1()#calling method1
        print("method of child1")
        super().method2()#calling method2
    def method1(self): #method overridding as we have alredy method1
        print("method of child2")



p=child1()
p.method1()# as grandchild inherits parent
