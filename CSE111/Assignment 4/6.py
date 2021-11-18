
class Vehicle:
    def __init__(self,x_coor=0,y_coor=0):
        self.x_coor=x_coor
        self.y_coor=y_coor

    def moveUp(self):
        self.y_coor+=1
    def moveDown(self):
        self.y_coor-=1
    def moveLeft(self):
        self.x_coor-=1
    def moveRight(self):
        self.x_coor+=1

    def print_position(self):
        print(f'({self.x_coor},{self.y_coor})')


car = Vehicle()
car.print_position()
car.moveUp()
car.print_position()
car.moveLeft()
car.print_position()
car.moveDown()
car.print_position()
car.moveRight()