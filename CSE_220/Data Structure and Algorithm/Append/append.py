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


    #Code for appending 
    def append(self,value):
         new_node=Node(value) #Node is a class
         if self.head is None: #case for empty linked List
             self.head=new_node #making the node head
             self.tail=new_node #making the node tail
         else: #case for already having a value
             self.tail.next=new_node 
             self.tail=new_node
         self.length+=1 
         return True #created for later use in bigger code of Node class     


my_linked_list=LinkedList(1) #creating a node with value 1 and pointer to None
my_linked_list.append(2) #adding 2 to the end of the linked List
my_linked_list.print_list()
 

