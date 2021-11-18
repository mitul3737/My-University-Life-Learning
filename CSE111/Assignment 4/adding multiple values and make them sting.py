def addBooks(self, *a_book): #change a_book
        str_0 = ""
        lst_1 = []
        str_0 = str(a_book)  # change sup_pow
        lst_0 = str_0.strip(")(").split(", ")
        for i in range(len(lst_0)):
            if lst_0[i][-2] == "'":
                lst_1.append(lst_0[i][-2])

            else:
                lst_1.append(lst_0[i][1:-1])

        self.book = lst_1  #gives  a list   #book was a vvariable set earlier or , book is a new variable set