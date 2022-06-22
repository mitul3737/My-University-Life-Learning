class Node:
    def __init__(self,value):
        self.value=value
        self.next=None


class LinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1
        
    # Code for printing the list
    def print_list(self):
        temp=self.head
        while temp != None:
             print(temp.value)
             temp=temp.next    



