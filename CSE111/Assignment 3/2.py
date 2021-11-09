class Flower():
    def __init__(self):
        pass
    """def name(self,name):
        self.name=name

    def color(self,color):
        self.color = color

    def petal(self,num_of_petal):
        self.num_of_peal = num_of_petal"""

flower1 = Flower()
flower1.name="Rose"
flower1.color="Red"
flower1.num_of_petal=6
print("Name of this flower:", flower1.name)
print("Color of this flower:",flower1.color)
print("Number of petal:",flower1.num_of_petal)
print("=====================")
flower2 = Flower()
flower2.name="Orchid"
flower2.color="Purple"
flower2.num_of_petal=4
print("Name of this flower:",flower2.name)
print("Color of this flower:",flower2.color)
print ("Number of petal:",flower2. num_of_petal)

print("\nSubtask 2 & 3:")
print(flower1)
print(flower2)
#print(id(flower1))
#print(id(flower2))
if flower1==flower2:
    print("they are same")
else:
    print("they are different")