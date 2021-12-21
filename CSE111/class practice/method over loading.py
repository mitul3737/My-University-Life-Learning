
class Parent:
    def __init__(self,name,address):
        self.name=name
        self.address=address
    def life_moto(self):
        print("Work smartly!")

class Child(Parent):
    def __init__(self,name,address,child_name):
        super().__init__(name,address)
        self.child_name=child_name
    def life_moto(self):
        print("Only Chill")



c1=Child("Karim","Texas","Mitul")
c1.life_moto()

