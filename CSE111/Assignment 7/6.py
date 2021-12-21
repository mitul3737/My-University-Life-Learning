class Shape:
    def __init__(self, name='Default', height=0, base=0):
        self.area = 0
        self.name = name
        self.height = height
        self.base = base

    def get_height_base(self):
        return "Height: " + str(self.height) + ",Base: " + str(self.base)


class triangle(Shape):
    def __init__(self, name="Default", height=0, base=0):
        super().__init__(name, height, base)

    def calcArea(self):
        self.area = 0.5 * self.base * self.height

    def printDetail(self):
        return f"Height: {self.height}, Base: {self.base}\nArea: {self.area}"


class trapezoid(Shape):
    def __init__(self, name, height, base, side):
        super().__init__(name, height, base)
        self.side = side

    def calcArea(self):
        self.area = (self.base + self.side) * self.height / 2

    def printDetail(self):
        return f"Height: {self.height}, Base: {self.base}, Side_A: {self.side}\nArea: {self.area}"


# write your code here
tri_default = triangle()
tri_default.calcArea()
print(tri_default.printDetail())
print('--------------------------')
tri = triangle('Triangle', 10, 5)
tri.calcArea()
print(tri.printDetail())
print('---------------------------')
trap = trapezoid('Trapezoid', 10, 6, 4)
trap.calcArea()
print(trap.printDetail())

"""Shape name: Default
Height: 0, Base: 0
Area: 0.0
---------------------------
Shape name: Triangle
Height: 10, Base: 5
Area: 25.0
---------------------------
Shape name: Trapezoid
Height: 10, Base: 6, Side_A: 4
Area: 50.0"""