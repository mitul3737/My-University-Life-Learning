class Library:
    def __init__(self,listOfBooks):
        self.avilableBooks=listOfBooks

    def displayAvailableBook(self):
        print()
        print("Available Books: ")
        for book in self.avilableBooks:
            print(book)
    def lendBook(self,requestedBook):
        if requestedBook in self.avilableBooks:
            print("You have now borrowed the book")
            self.avilableBooks.remove(requestedBook)
        else:
            print("Sorry, the book is not available in our list")
    def addBook(self,returnBook):
        self.avilableBooks.append(returnBook)
        print("You have returned the book. Thank you!")

class Customer:
    def requestBook(self):
        print("Enter the name of book you want to borrow: ")
        self.book=input()
        return self.book

    def returnBook(self):
        print("Enter the name of the book you want to return: ")
        self.book=input()
        return self.book

library=Library(['Think and grow Rich','Who will cry while you die',  'For One More Day'])
customer=Customer()

while True:
    print("Enter 1 to display the available books")
    print("Enter 2 to request for a book")
    print("Enter 3 to return a book")
    print("Enter 4 to exit")
    userChoice = int(input())
    if userChoice == 1:
        library.displayAvailableBook()
    elif userChoice == 2:
        requestedBook = customer.requestBook()
        library.lendBook(requestedBook)
    elif userChoice == 3:
        returnBook = customer.returnBook()
        library.addBook(returnBook)
    else:
        quit()
