#Multiple Inheritence
class Base1:
    pass
class Base2:
    pass
class MultiDerived(Base1,Base2):
    pass

class Base1:
    def funcBase1(self):
        print("funcBase1 is executing...")
class Base2:
    def funcBase2(self):
        print("funcBase2 is executing....")
class Base3:
    def funcBase3(self):
        print("funcBase3 is executing...")

class MultiDerived(Base1,Base2,Base3):
     def funcMultiDerived(self):
         print("funcMultiDerived() is executing ....")

md1=MultiDerived()
md1.funcBase1()
md1.funcBase2()
md1.funcBase3()
md1.funcMultiDerived()

