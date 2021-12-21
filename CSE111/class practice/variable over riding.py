class Parent:
    def __init__(self,name,address):
        self.name=name
        self.address=address
        self.wealth="100 Million Dollar"
    def life_moto(self):
        print("Work smartly!")

class Child(Parent):
    def __init__(self,name,address,child_name):
        super().__init__(name,address)
        self.child_name=child_name
        self.wealth="0 taka"
    def life_moto(self):
        super().life_moto()
        print("and  Chill")



c1=Child("Karim","Texas","Mitul")
c1.life_moto()
print(c1.wealth)
