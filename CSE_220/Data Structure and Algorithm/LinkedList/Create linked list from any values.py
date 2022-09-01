class Node:
    def __init__(self, data=None, link=None):
        self.data = data
        self.link = link

    def __str__(self):
        return str(self.data)


# user defined class for Linked list
class LinearList:
    def __init__(self, start=None, nodecount=0):
        self.start = start
        self.nodecount = nodecount  # stores number of nodes in linked list

    def addBegNode(self, value=None):  # Adding nodes at beginning
        node = Node(value)
        node.link = self.start
        self.start = node
        self.nodecount = self.nodecount + 1

    def printList(self):  # traverse abd display nodes
        ptr = self.start
        while ptr:
            print(ptr)
            ptr = ptr.link
        print()


ll = LinearList()
numele = input('How many elements to be added in the Linked List??')
# add nodes at begging in the Linked List
for cnt in range(int(numele)):
    ele = input('Enter a value to be added at the beginning of the Linked List ')
    ll.addBegNode(ele)
    cnt = cnt + 1
# Print Linked List  before sorting
print("Linked List Initially")
ll.printList()