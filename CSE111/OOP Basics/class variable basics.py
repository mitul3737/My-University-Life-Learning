class Book():
    x = 5  # class variable
    y=6

    def __init__(self):
        self.x = 100  # instance variable

    def display(self):
        print(self.x)


b = Book()
print(Book.x)  # printing class variable
print(b.x)  # printing instance variable
print(Book.y)

#changng the class variable changes the value for class and instance
Book.y=7
print(Book.y)
print(b.y)

#changing instance variuable does not change the variable y
b.y=90
print(b.y)
print(Book.y)