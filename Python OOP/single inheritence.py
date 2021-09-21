class Apple:
    manufacturer="Apple Inc."
    contactWebsite="www.apple.com/contact"

    def contactDetails(self):
        print("To contact us, log into ",self.contactWebsite)
class MacBook(Apple):
    def __init__(self):
         self.yearOfManufacturer=2017
    def manufactureDetails(self):
          print("This Macbook was manufactured in the year {} by {}".format(self.yearOfManufacturer,self.manufacturer))

macBook=MacBook()
macBook.manufactureDetails()
macBook.contactDetails()
