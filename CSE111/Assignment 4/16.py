class Author():
    def __init__(self,name="Default",*book):
        self.name=name
        self.book=book
    def addBooks(self,*a_book):
        str_0 = ""
        lst_1=[]
        str_0 = str(a_book)  # change sup_pow
        lst_0 = str_0.strip(")(").split(", ")
        for i in range(len(lst_0)):
            if lst_0[i][-2] == "'":
                lst_1.append(lst_0[i][-2])

            else:
                lst_1.append(lst_0[i][1:-1])

        self.book = lst_1

    def printDetails(self):
        print(f"Author Name: {self.name}")
        print("--------")
        print("List of Books:")
        for i in self.book:
            print(i)
    def changeName(self,c_name):
        self.name=c_name

auth1 = Author('Humayun Ahmed')
auth1.addBooks('Deyal', 'Megher Opor Bari')
auth1.printDetails()
print('===================')
auth2 = Author()
print(auth2.name)
auth2.changeName('Mario Puzo')
auth2.addBooks('The Godfather', 'Omerta', 'The Sicilian')
print('===================')
auth2.printDetails()
print('===================')
auth3 = Author('Paolo Coelho', 'The Alchemist', 'The Fifth Mountain')
auth3.printDetails()
