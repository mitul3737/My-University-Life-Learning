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

    #Code for popping
    def pop(self):
        if self.length==0: #if the list is empty
            return None
        temp=self.head
        pre=self.head
        #for case having more than 2 nodes
        while(temp.next):
            pre=temp
            temp=temp.next
        self.tail=pre
        self.tail.next=None
        self.length-=1
        if self.length==0: #if the list had just one value , we will decrement the length and then set head and tail to None
            self.head=None
            self.tail=None  
        return temp #You can return temp.value to see the value of the node but as you have returned temp and thus it will return the node which has the address.



my_linked_list=LinkedList(1) #creating a node with value 1 and pointer to None
my_linked_list.append(2) #adding 2 to the end of the linked List

#Now removing the nodes
print(my_linked_list.pop()) # (when 2 items left) pops node 2 as we have 2 have 1 and 2 added in the linked list
print(my_linked_list.pop()) # (when 1 items left)pops node 1
print(my_linked_list.pop()) # (when 0 items left) will return None as we have nothing in the linked list now


"""Output:
<__main__.Node object at 0x0000023102606E20>
<__main__.Node object at 0x0000023102606FA0>
None
"""

#you can return temp.value to just see the value of the node.