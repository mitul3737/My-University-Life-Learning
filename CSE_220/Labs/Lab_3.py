class Node:
    def __init__(self, e, n):
        self.element = e
        self.next = n


class LinkedList:
    def __init__(self, a):
        if type(a) == list:
            tail = None
            self.head = None
            for i in range(0, len(a)):
                new_node = Node(a[i], None)
                if self.head == None:
                    self.head = new_node
                    tail = new_node
                else:
                    tail.next = new_node
                    tail = new_node
        else:
            self.head = a

    def countNode(self):
        temp = self.head
        count = 0
        while temp != None:
            count += 1
            temp = temp.next
        return count

    def printList(self):
        temp = self.head
        str_0 = ""
        while temp != None:
            str_0 += str(temp.element) + ", "
            temp = temp.next
        print(str_0[:-2])

    def nodeAt(self, idx):
        temp = self.head
        count = 0
        while temp != None:
            count += 1
            temp = temp.next

        #Check if exceeds the length of the list
        if idx < 0 or idx >= count:
            return None
        #checks if it does not exceed
        else:
            count_0=0
            temp_0 = self.head
            while temp_0 != None:
                if  count_0 == idx:
                    return temp_0
                count_0+=1
                temp_0 = temp_0.next

    """def nodeAt(self,idx):
        temp=self.head
        count=0
        while temp!=None:
            if count==idx:
                return temp
            count+=1
            temp=temp.next
        return None #returns if it does not find the idx"""


    # updates the element of the Node at the given index.
    # Returns the old element that was replaced. For invalid index return None.
    # parameter: index, element
    def set(self, idx, elem):
        temp = self.head
        count = 0
        while temp != None:
            count += 1
            temp = temp.next

        if idx < 0 or idx >= count:
            return None
        else:
            temp = self.head
            for _ in range(idx):
                temp = temp.next
            if temp:
                x = temp.element
                temp.element = elem
            return x
        return False

    def get(self, idx):
        temp = self.head
        count = 0
        while temp != None:
            count += 1
            temp = temp.next
        if idx < 0 or idx >= count:
            return None
        temp = self.head
        for _ in range(idx):
            temp = temp.next
        return temp.element  # returns

    def indexOf(self, elem):
        temp = self.head
        count_0 = 0
        while temp != None:
            if temp.element == elem:
                return count_0
            temp = temp.next
            count_0 += 1
        return -1

    def contains(self, elem):
        temp = self.head
        while temp != None:
            if temp.element == elem:
                return True
            temp = temp.next
        return False

    # Makes a duplicate copy of the given List. Returns the reference of the duplicate list.
    def copyList(self):
        copyhead = self.head
        copytail = self.head
        while copytail != None:
            copytail = copytail.next
        return copyhead

    def reverseList(self):
        reversehead = None
        temp = self.head
        while temp != None:
            new_node = Node(temp.element, None)  # Created a node using every value
            new_node.next = reversehead  # changed the new nodes next to reversehead
            reversehead = new_node  # now changing the reversehead
            temp = temp.next
        return reversehead  # returning reversehead

    def insert(self, elem, idx):
        # checce validity
        temp = self.head
        count = 0
        while temp != None:
            count += 1
            temp = temp.next
        if idx < 0 or idx > count:
            return print("Invalid index")

        # Creating a node for the new element
        else:
            new_node = Node(elem, None)
            # Adding at beginning
            if idx == 0:
                new_node.next = self.head
                self.head = new_node
            # adding in middle or last
            elif idx < count:  # for middle values
                pred = self.nodeAt(idx - 1)
                new_node.next = pred.next
                pred.next = new_node
            else:  # to add with the last index
                pred = self.nodeAt(idx - 1)
                new_node.next = pred.next
                pred.next = new_node

    def remove(self, index):
        temp = self.head
        count = 0
        while temp != None:
            count += 1
            temp = temp.next
        # checking if the index exists or not
        if index < 0 or index >= count:
            return None
        else:
            # if need to remove the first index Case 1
            if index == 0:
                if count == 0:
                    return None
                temp = self.head
                self.head = self.head.next
                temp.next = None
                count -= 1
                tail = self.head
                while tail != None:
                    tail = tail.next
                if count == 0:
                    tail = None
                return temp.element
            # if need to remove the last index    Case 2
            if index == count - 1:
                if count == 0:
                    return None
                temp = self.head
                pre = self.head
                while (temp.next):
                    pre = temp
                    temp = temp.next
                self.tail = pre
                self.tail.next = None
                count -= 1
                tail = self.head
                while tail != None:
                    tail = tail.next
                if count == 0:
                    self.head = None
                    tail = None
                return temp.element

            # if need to remove in the middle    Case 3
            #Creating a get method to get the elementS Node at the given index
            def get(idx):
                temp = self.head
                count = 0
                while temp != None:
                    count += 1
                    temp = temp.next
                if idx < 0 or idx >= count:
                    return None
                temp = self.head
                for _ in range(idx):
                    temp = temp.next
                return temp

            pre = get(index - 1)
            temp = pre.next
            pre.next = temp.next
            temp.next = None
            count -= 1
            return temp.element


    def rotateLeft(self):
        tail=self.head
        while tail.next!=None:
            tail=tail.next

        p=self.head
        tail.next=self.head
        self.head=p.next
        p.next=None

    def rotateRight(self):
        tail = self.head
        while tail.next != None:
            tail = tail.next
        p=self.head
        while p.next!=tail:
            p=p.next

        #print(p.element)
        #print(tail.element)
        tail.next=self.head
        self.head=tail
        p.next=None


print("////// Test 01 //////")
a1 = [10, 20, 30, 40]
h1 = LinkedList(a1)  # Creates a linked list using the values from the array
# head will refer to the Node that contains the element from a[0]

h1.printList()  # This should print: 10,20,30,40
print(h1.countNode())  # This should print: 4

print("////// Test 02 //////")
# returns the reference of the Node at the given index. For invalid idx return None.
myNode = h1.nodeAt(1)
print(myNode.element)  # This should print: 20. In case of invalid index This will generate an Error.

print("////// Test 03 //////")
# returns the element of the Node at the given index. For invalid idx return None.
val = h1.get(2)
print(val)  # This should print: 30. In case of invalid index This will print None.

print("////// Test 04 //////")

# updates the element of the Node at the given index.
# Returns the old element that was replaced. For invalid index return None.
# parameter: index, element

print(h1.set(1, 85))  # This should print: 20
h1.printList()  # This should print: 10,85,30,40.
print(h1.set(15, 85))  # This should print: None
h1.printList()  # This should print: 10,85,30,40.

print("////// Test 05 //////")
# returns the index of the Node containing the given element.
# if the element does not exist in the List, return -1.
index = h1.indexOf(40)
print(index)  # This should print: 3. In case of element that doesn't exists in the list this will print -1.

print("////// Test 06 //////")
# returns true if the element exists in the List, return false otherwise.
ask = h1.contains(40)
print(ask)  # This should print: True.

print("////// Test 07 //////")
a2 = [10, 20, 30, 40, 50, 60, 70]
h2 = LinkedList(a2)  # uses theconstructor where a is an built in list
h2.printList()  # This should print: 10,20,30,40,50,60,70.
# Makes a duplicate copy of the given List. Returns the head reference of the duplicate list.
copyH = h2.copyList()  # Head node reference of the duplicate list
h3 = LinkedList(copyH)  # uses the constructor where a is head of a linkedlist
h3.printList()  # This should print: 10,20,30,40,50,60,70.

print("////// Test 08 //////")
a4 = [10, 20, 30, 40, 50]
h4 = LinkedList(a4)  # uses theconstructor where a is an built in list
h4.printList()  # This should print: 10,20,30,40,50.
# Makes a reversed copy of the given List. Returns the head reference of the reversed list.
revH = h4.reverseList()  # Head node reference of the reversed list
h5 = LinkedList(revH)  # uses the constructor where a is head of a linkedlist
h5.printList()  # This should print: 50,40,30,20,10.

print("////// Test 09 //////")
a6 = [10, 20, 30, 40]
h6 = LinkedList(a6)  # uses theconstructor where a is an built in list
h6.printList()  # This should print: 10,20,30,40.

# inserts Node containing the given element at the given index. Check validity of index.
h6.insert(85, 0)
h6.printList()  # This should print: 85,10,20,30,40.
h6.insert(95, 3)
h6.printList()  # This should print: 85,10,20,95,30,40.
h6.insert(75, 6)
h6.printList()  # This should print: 85,10,20,95,30,40,75.

print("////// Test 10 //////")
a7 = [10, 20, 30, 40, 50, 60, 70]
h7 = LinkedList(a7)  # uses theconstructor where a is an built in list
h7.printList()  # This should print: 10,20,30,40,50,60,70.

# removes Node at the given index. returns element of the removed node.
# Check validity of index. return None if index is invalid.

print("Removed element:", h7.remove(0))  # This should print: Removed element: 10
h7.printList()  # This should print: 20,30,40,50,60,70.
print("Removed element: ", h7.remove(3))  # This should print: Removed element: 50
h7.printList()  # This should print: 20,30,40,60,70.
print("Removed element: ", h7.remove(4))  # This should print: Removed element: 70
h7.printList()  # This should print: 20,30,40,60.

print("////// Test 11 //////")
a8 = [10, 20, 30, 40]
h8 = LinkedList(a8)  # uses theconstructor where a is an built in list
h8.printList()  # This should print: 10,20,30,40.

# Rotates the list to the left by 1 position.
h8.rotateLeft()
h8.printList()  # This should print: 20,30,40,10.

print("////// Test 12 //////")
a9 = [10, 20, 30, 40]
h9 = LinkedList(a9)  # uses theconstructor where a is an built in list
h9.printList()  # This should print: 10,20,30,40.

# Rotates the list to the right by 1 position.
h9.rotateRight()
h9.printList()  # This should print: 40,10,20,30.