class Bird:
    def __init__(self,name,fly_0=False):
        self.name=name
        self.fly_0=fly_0
        self.value="Flightless Birds"
    def fly(self):
        if self.fly_0:
            print(f"{self.name} can fly")
        else:
            print(f"{self.name} can not fly")
    def setType(self,value="Flightless Birds"):
           self.value=value

    def printDetail(self):
        print(f"Name:{self.name}\nType: {self.value}")






ostrich = Bird('Ostrich')
duck = Bird("Duck", True)
owl = Bird('Owl', True)
print("###########################")
ostrich.fly()
duck.fly()
owl.fly()
duck.setType('Water Birds')
owl.setType('Birds of Prey')
print("=========================")
ostrich.printDetail()
print("=========================")
duck.printDetail()
print("=========================")
owl.printDetail()


"""###########################
Ostrich can not fly
Duck can fly
Owl can fly
===========================
Name: Ostrich
Type: Flightless Birds
===========================    	
Name: Duck
Type: Water Birds
===========================
Name: Owl
Type: Birds of Prey

"""