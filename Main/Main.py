class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        #Creates a node
        new_node = Node(value)
        #Checks if the BInary Search Tree is empty or not. If empty, then adds the node there
        if self.root is None:
            self.root = new_node
            return True
        #starts working from the root to compare with the node
        temp = self.root
        while (True):
            #Checks if the node that we want to insert already exists
            if new_node.value == temp.value:
                return False
            #Checks if the node is smaller than the temp value
            if new_node.value < temp.value:
                #Checks if the left side of the temp value is empty or not
                if temp.left is None:
                    temp.left = new_node
                    return True
                #if not empty
                temp = temp.left
            else:
                #Checks if the right side of the temp value is empty or not
                if temp.right is None:
                    temp.right = new_node
                    return True
                #if not empty
                temp = temp.right

#Creating a BST
my_tree = BinarySearchTree()
#Inserting node 2 in the empty BST and thus the node 2 will be appointed as root & also temp value
my_tree.insert(2)
#First it will check if node 1 already exists or not
#Inserting node 1 . FIrst we will check if that node 1 is less than node 2 and then it will be moved to left
#temp.left= node 1
#as node 2 has nothing in left , that's why it will be added to left side
my_tree.insert(1)
#FIrst it will check if node 3 exists or not
#now node 3 is greater than 2 and thus temp.right will be node 3
#as there is nothing in right side of node 2, node 3 will be added.
my_tree.insert(3)


print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)
