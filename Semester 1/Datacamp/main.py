class Panda:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def sleep(self, time=None):
        if time == None:
            food = "bamboo leaves"
            time = "unknown"
            return (f"{self.name}'s duration is unknown thus should have only bamboo leaves")
        else:
            if time >= 3 and time <= 5:
                food = "Mixed Veggies"
            elif time >= 6 and time <= 8:
                food = "Eggplant & Tofu"
            elif time >= 9 and time <= 11:
                food = "Broccoli Chicken"

            return (f"{self.name} sleeps {time} hours daily and should have {food}")


panda1 = Panda("Kunfu", "Male", 5)
panda2 = Panda("Pan Pan", "Female", 3)
panda3 = Panda("Ming Ming", "Female", 8)
print("{} is a {} Panda Bear who is {} years old".format(panda1.name, panda1.gender, panda1.age))
print("{} is a {} Panda Bear who is {} years old".format(panda2.name, panda2.gender, panda2.age))
print("{} is a {} Panda Bear who is {} years old".format(panda3.name, panda3.gender, panda3.age))
print("===========================")
print(panda2.sleep(10))
print(panda1.sleep(4))
print(panda3.sleep())