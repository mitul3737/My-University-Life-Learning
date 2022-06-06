class Cookie:
    def __init__(self,color):
        self.color=color
    def get_color(self):
        return self.color
    def set_color(self,color):
        self.color= color


cookie_one=Cookie("green")
cookie_two=Cookie("yellow")

print("Cookie one is",cookie_one.get_color())
print("Cookie two is",cookie_two.get_color())
cookie_two.set_color("red")
print("Cookie two is",cookie_two.get_color())