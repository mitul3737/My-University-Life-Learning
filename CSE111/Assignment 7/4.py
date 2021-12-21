class Product:
    def __init__(self, id, title, price):
        self.__id = id
        self.__title = title
        self.__price = price

    def get_id_title_price(self):
        return "ID: " + str(self.__id) + " Title: " + self.__title + " Price: " + str(self.__price)


class Book(Product):
    def __init__(self, id, title, price, isbn, publ):
        super().__init__(id, title, price)
        self.isbn = isbn
        self.publ = publ

    def printDetail(self):
        print(self.get_id_title_price())
        return f"ISBN: {self.isbn} Publisher: {self.publ}"


class CD(Product):
    def __init__(self, id, title, price, band, dur, genre):
        super().__init__(id, title, price)
        self.band = band
        self.dur = dur
        self.genr = genre

    def printDetail(self):
        print(self.get_id_title_price())
        return f"Band: {self.band} Duration: {self.dur}minutes\nGenre: {self.genr}"


# write your code here
book = Book(1, "The Alchemist", 500, "97806", "HarperCollins")
print(book.printDetail())
print("-----------------------")
cd = CD(2, "Shotto", 300, "Warfaze", 50, "Hard Rock")
print(cd.printDetail())