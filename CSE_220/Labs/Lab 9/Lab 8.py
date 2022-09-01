1.
def min_index(arr, i, j):# Returns the  minimum index of the array
    if i == j:
        return i
    k = min_index(arr, i + 1, j)
    return (i if arr[i] < arr[k] else k)


def recursion_selectionSort(a, n, i=0):
    if i == n:
        return -1
    k = min_index(a, i, n - 1)  # this returns the lowest index
    if k != i:
        a[k], a[i] = a[i], a[k] #swaps the values
    recursion_selectionSort(a, n, i + 1) #calling the function again


arr = [3, 1, 5, 2, 7, 0]
n = len(arr)
recursion_selectionSort(arr, n) # makes the array sorted using selection sort
print(arr) # prints the array


2.
def insertionSort(arr,l,r):
  if l>=r:
    return #returns None
  else:
    insertionSort(arr,l,r-1) #calls the function again with the new l and r-1
  for i in range(1,len(a)):
    key=a[i]
    j=i-1

    #swaps the values
    while j>=0 and arr[j]>key:
      a[j+1]=arr[j]
      j-=1
    arr[j+1]=key


#tester
a=[6,7,3,5,9,-9,0]
insertionSort(a,0,len(a)-1) #calls the  functions to sort using insertion sort
print(a) #prints the sorted array





3.
class Node:
    def __init__(self, e, n):
        self.element = e
        self.next = n


class LinkedList:
    def __init__(self, a):
        if type(a) == list:
            tail = None
            self.head = None
            self.count = 0
            for i in range(0, len(a)):
                new_node = Node(a[i], None)
                if self.head == None:
                    self.head = new_node
                    tail = new_node
                    self.count += 1
                else:
                    tail.next = new_node
                    tail = new_node
                    self.count += 1
        else:
            self.head = a

    # Printing the linked list
    def printList(self):
        temp = self.head
        str_0 = ""
        while temp != None:
            str_0 += str(temp.element) + " -> "
            temp = temp.next

        print(str_0[:-3])

    def bubble_sort(self):
        for i in range(self.count - 1):
            curr = self.head
            nxt = curr.next
            prev = None
            while nxt:
                if curr.element > nxt.element:
                    if prev == None:
                        prev = curr.next
                        nxt = nxt.next
                        prev.next = curr
                        curr.next = nxt
                        self.head = prev
                    else:
                        temp = nxt
                        nxt = nxt.next
                        prev.next = curr.next
                        prev = temp
                        temp.next = curr
                        curr.next = nxt
                else:
                    prev = curr
                    curr = nxt
                    nxt = nxt.next
            i = i + 1


arr = [10, 3, 5, 9, 0, 2, 5, -4, 5, 0, -100, 100]
a = LinkedList(arr)
a.bubble_sort()
a.printList()



4.
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


    #Printing the linked list
    def printList(self):
        temp = self.head
        str_0 = ""
        while temp != None:
            str_0 += str(temp.element) + " -> "
            temp = temp.next
        print(str_0[:-3])


    #Swap nodes
    def swapNodes(self,head_ref, cur_val, min_val, prev_val):
        head_ref = min_val
        prev_val.next = cur_val
        temp = min_val.next
        min_val.next = cur_val.next
        cur_val.next = temp
        return head_ref


    #Selection sort using recursion
    def recurSelectionSort(self,head):
        # Base case
        if (head.next == None):
            return head
        min_O = head
        before_Min = None
        mit = head
        while (mit.next != None):
            if (mit.next.element < min_O.element):
                min_O = mit.next
                before_Min = mit
            mit = mit.next
        if (min_O != head):
            head = self.swapNodes(head, head, min_O, before_Min)  # returns head , min node and before the min node
        # Head.next still remains unsorted. We sort it sending the head.next reference
        head.next = self.recurSelectionSort(head.next)
        return head


    def sort(self):
        if ((self.head) == None):
                return None
        self.head = self.recurSelectionSort(self.head)
        return self.printList() #printing the sorted linked list





arr = [10, 3, 5, 9, 0, 2, 5,-4,5,0,-100,100]
a = LinkedList(arr)
a.sort()



5.
class Node:

    def __init__(self, element):
        self.data = element
        self.prev = None
        self.next = None


def getNode(data):
    newNode = Node(0)
    newNode.data = data
    newNode.prev = newNode.next = None
    return newNode


def sortedInsert(head_ref, newNode):
    current = None
    if (head_ref == None):
        head_ref = newNode
    elif ((head_ref).data >= newNode.data):
        newNode.next = head_ref
        newNode.next.prev = newNode
        head_ref = newNode
    else:
        current = head_ref
        while (current.next != None and
               current.next.data < newNode.data):
            current = current.next
        newNode.next = current.next
        if (current.next != None):
            newNode.next.prev = newNode
        current.next = newNode
        newNode.prev = current

    return head_ref;



def insertionSort(head_ref):
    sorted = None
    current = head_ref
    while (current != None):
        next = current.next
        current.prev = current.next = None
        sorted = sortedInsert(sorted, current)
        current = next
    head_ref = sorted

    return head_ref



def printList(head):
    while (head != None):
        print(head.data, end=" ")
        head = head.next



def push(head_ref, new_data):
    new_node = Node(0)
    new_node.data = new_data
    new_node.next = (head_ref)
    new_node.prev = None
    if ((head_ref) != None):
        (head_ref).prev = new_node
    (head_ref) = new_node
    return head_ref





arr=[9,3,5,10,12,8,7,100,-100,0,4,2,1,-200]
def array_doubly_linked_list(arr):
    head = None
    for i in range(len(arr)):
        head = push(head, arr[i])
    return head

head = insertionSort(array_doubly_linked_list(arr))
printList(head)



6.
def binarySearch(a,value,l,r):
  if l>r:
    return "The value you provided is not in the list"
  mid=(l+r)//2
  if a[mid]==value:
    return mid
  elif a[mid]>value:
    return binarySearch(a,value,l,mid-1)
  else:
    return binarySearch(a,value,mid+1,r)

a=[1,2,6,7,34,78] #sorted array
print(binarySearch(a,34,0,len(a)-1)) # format: binarySearch(a, value to look for,search sarting from , last index)



7.

A=[] #creating a list
def F(n):
 if (n==0 or n==1):
    return 1
 else:
    return F(n-1)+F(n-2)
def FM(n):
 if(A[n] > 0):
    return A[n]
 if(n == 0 or n==1):
    return 1
 else:
    return A[n].append(FM(n-1)+FM(n-2))


def CalcFib():
 A.insert(0,1)
 A.insert(1,1)
 for i in range(2,100): #Set the fibonacci limit to 100 index. You can change it too to your own benefit
    A.insert(i,A[i-1]+A[i-2])


CalcFib()
#The fibonacci series is: 0,1,1,2,3,5,8,13,21,........... which follows f(n)=f(n-1)+f(n-2)
var=input("Which fibonacci number  do you want to know? Kindly enter the index number: ")
"""For example
Which fibonacci number  do you want to know? Kindly enter the index number: 0
1"""
print(F(int(var)))





