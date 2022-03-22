#method under a class
def print_list(self):
    temp=self.head
    while temp != None:
        print(temp.value)
        temp=temp.next