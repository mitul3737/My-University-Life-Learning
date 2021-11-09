class box():
    def __init__(self,lst_0):
        self.height=lst_0[0]
        self.width=lst_0[1]
        self.breadth=lst_0[2]
        lst_1=lst_0


print("Box 1")
b1 = box([10,10,10])
print('Creating a Box!')
print(f'Volume of the box is {b1.height*b1.width*b1.breadth} cubic units')
print("=========================")
print("Height:", b1.height)
print("Width:", b1.width)
print("Breadth:", b1.breadth)
print("-------------------------")
print("Box 2")
b2 = box((30,10,10))
print('Creating a Box!')
print(f'Volume of the box is {b2.height*b2.width*b2.breadth} cubic units')
print("=========================")
print("Height:", b2.height)
print("Width:", b2.width)
print("Breadth:", b2.breadth)
b2.height = 300
print("Updating Box 2!")
print("Height:", b2.height)
print("Width:", b2.width)
print("Breadth:", b2.breadth)
print("-------------------------")
print("Box 3")
b3 = b2
print("Height:", b3.height)
print("Width:", b3.width)
print("Breadth:", b3.breadth)