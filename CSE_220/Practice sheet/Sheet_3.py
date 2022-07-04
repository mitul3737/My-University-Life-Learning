#1
# class Node:
#     def __init__(self, elem,next):
#       self.elem = elem
#       self.next = next
#
# class SinglyLinkedList:
#     def __init__(self,a):
#         tail = None
#         self.head = None
#         for i in range(0,len(a)):
#             new_node = Node(a[i],None)
#             if i == 0:
#                 self.head = new_node #Don't use Node(a[i],None) instead of new_node cause it creates a new node every time and your Linked List losts everything
#                 tail = new_node
#             else:
#
#                 tail.next = new_node
#                 tail = new_node
#
#     def printlist(self):
#         temp=self.head
#         STR_0=""
#         while temp!=None:
#             STR_0+=str(temp.elem)+"->"
#             temp=temp.next
#         return print(STR_0+'None')
#
#
#     def nodeat(self,idx):
#         temp=self.head
#         count=0
#         while temp!=None:
#             if count==idx:
#                 return temp
#             temp=temp.next
#             count+=1
#         return None
#
#
#     def remove(self,val):
#         temp=self.head
#         prev=None
#         idx=0
#         count=0
#         #checking length of list
#         while temp!=None:
#             count+=1
#             temp=temp.next
#         temp=self.head
#         while temp!=None:
#             #when the node exists
#             if temp.elem==val:
#                 #when the node is the head
#                 if idx==0:
#                     self.head=temp.next
#                     return temp.elem
#                 #when the node is the tail
#                 elif idx==count:
#                     prev=self.nodeat(idx-1) # Getting the previous Node of the desired node
#                     prev.next=None
#                     return temp.elem
#                 #when the node is in the middle
#                 else:
#                     prev=self.nodeat(idx-1) # Getting the previous Node of the desired node
#                     prev.next=temp.next
#                     return temp.elem
#
#             temp=temp.next
#             idx+=1
#         return "Value not in the LinkedList"
#
#     def insert(self,elem,pos):
#         idx=pos-1
#         new_node = Node(elem, None)
#         temp=self.head
#         count=0
#         prev=None
#         while temp!=None:
#             count+=1
#             temp=temp.next
#         #for index=0
#         if idx==0:
#             new_node.next=self.head
#             self.head=new_node
#         #for last index
#         elif idx+1==count:
#             temp.next=new_node
#             new_node.next=None
#         #for index in middle
#         else:
#             prev=self.nodeat(idx-1)
#             new_node.next = prev.next
#             prev.next=new_node
#     def rotateRight(self,k):
#         for i in range(k):
#             temp=self.head
#             #getting the last node
#             while temp.next!=None:
#                 temp=temp.next
#
#             #getting the node before last node
#             n=self.head
#             while n.next!=temp:
#                 n=n.next
#
#             #Setting the last node as head
#             temp.next=self.head
#             self.head=temp
#             n.next=None
#
#     def rotateLeft(self,k):
#         for i in range(k):
#             #setting temp_1 as the next node of head
#             temp_1=self.head.next
#
#             #getting the last node as temp
#             temp=self.head
#             while temp.next!=None:
#                 temp=temp.next
#
#             #main process of rotating
#             temp.next=self.head#setting the self.head as the last node
#             self.head.next=None #seting None as the next node of the last node
#             self.head=temp_1 #setting the temp_1 as the head
#     def reverse(self):
#         temp=self.head
#         new_head=None
#         while temp!=None:
#             new_node=Node(temp.elem,None) #creating a new node
#             new_node.next=new_head #setting of the next of the new node to self.head
#             new_head = new_node #changing the head to the new node
#             temp=temp.next # changing the temp to go to next node
#         self.head=new_head # changing self.head to the last node (new head)
#
#
#
#
# h1=[92,56,88,55,19,67,66]
# h2=SinglyLinkedList(h1)
# print(h2.remove(56))
# h2.printlist()
# id=547
# h2.insert(id%23,4)
# h2.printlist()
# birthyear=2001
# h2.insert(birthyear%61,3)
# h2.printlist()
# h2.rotateRight(3)
# h2.printlist()
# h2.remove(92)
# h2.printlist()
# h2.remove(66)
# h2.printlist()
# h2.rotateLeft(4)
# h2.printlist()
# h2.reverse()
# h2.printlist()



#2 no code
# class Node:
#     def __init__(self,elem,next):
#         self.elem=elem
#         self.next=next
# class LinkeList:
#     def __init__(self,a):
#         self.head=None
#         tail=None
#         for i in range(0,len(a)):
#             new_node=Node(a[i],None)
#             if i==0:
#                 self.head=new_node
#                 tail=new_node
#             else:
#                 tail.next=new_node
#                 tail=new_node
#
#     def printlist(self):
#         temp=self.head
#         STR_0=""
#         while temp!=None:
#               STR_0+=str(temp.elem)+"->"
#               temp=temp.next
#         return print(STR_0[:-2])
#
#     def reverselist(self,head,k):
#         temp=head
#         prev=None
#         next=None
#         count=0
#         while temp!=None and count<k:
#             next=temp.next
#             temp.next=prev
#             prev=temp
#             temp=next
#             count+=1
#         if next!=None:
#             """when k=3 :
#             After 1st iteration for reverse,
#             we have 4->5->6............. where 4 is next
#             3->2->1->None where 3 is previous"""
#             head.next=self.reverselist(next,k)
#             """We have now set 3->2->1->4->5->6-...... and 4 is set as head of new list and the reverse will start from 4->5->6->..... """
#             """After the 2nd iteration , we will have 3->2->1->6->5->4->7->8->9->None where 7 is head of new list and the reverse will start from 7->8->9->..... """
#         return prev
#
#
# a=input("")
# str_0=a.split(" and ")
# demo=str_0[0].split("->")
# l1=[]
# for i in range(0,len(demo)):
#     l1.append(int(demo[i]))
#
# a1=LinkeList(l1)
# a1.printlist()
# a1.head=a1.reverselist(a1.head,int(str_0[1]))
# a1.printlist()



#3 no
# class Node:
#     def __init__(self,elem,next):
#         self.elem=elem
#         self.next=next
# class LinkeList:
#     def __init__(self,a):
#         self.head=None
#         tail=None
#         for i in range(0,len(a)):
#             new_node=Node(a[i],None)
#             if i==0:
#                 self.head=new_node
#                 tail=new_node
#             else:
#                 tail.next=new_node
#                 tail=new_node
#
#     def printlist(self):
#         temp=self.head
#         STR_0=""
#         while temp!=None:
#               STR_0+=str(temp.elem)+"->"
#               temp=temp.next
#         return print(STR_0[:-2])
#
#     def reverse(self,a):
#         temp = a
#         new_head = None
#         while temp != None:
#             new_node = Node(temp.elem, None)  # creating a new node
#             new_node.next = new_head  # setting of the next of the new node to self.head
#             new_head = new_node  # changing the head to the new node
#             temp = temp.next  # changing the temp to go to next node
#         return new_head
#
#     def even_odd_reverse(self):
#         Even_start=None
#         Even_end=None
#         Odd_start=None
#         Odd_end=None
#         temp=self.head
#         while temp!=None:
#             if temp.elem%2==0:
#                 if Even_start==None:
#                     Even_start=temp
#                     Even_end=temp
#                 else:
#                     Even_end.next=temp
#                     Even_end=temp
#             else:
#                 if Odd_start==None:
#                     Odd_start=temp
#                     Odd_end=temp
#                 else:
#                     Odd_end.next=temp
#                     Odd_end=temp
#             temp=temp.next
#
#
#         #Setting the next of the last node to None
#         # 1->2->3->4->5->6->7->8 for this case we have 2->4->6->8->None and 1->3->5->7->None
#         Even_end.next=None
#         Odd_end.next=None
#
#         #Setting the even head
#
#
#
#         #If we need to reverse the Even list also
#         # even_head=self.reverse(Even_start)
#         # #getting last node of even list
#         # even_tmp=even_head
#         # while even_tmp.next!=None:
#         #     even_tmp=even_tmp.next
#         # #Gets the even end
#         # Even_end=even_tmp
#
#         #Setting Odd_head
#         odd_head=self.reverse(Odd_start)
#
#         # getting last node of even list
#         odd_tmp = odd_head
#         while odd_tmp.next != None:
#             odd_tmp = odd_tmp.next
#
#         #Setting odd end
#         Odd_end = odd_tmp
#
#
#
#         #Now connecting this 2 linked list
#         Even_end.next=odd_head
#         Odd_end.next=None
#
#         #Setting the head of the list as Even head
#         self.head=Even_start
#
#
#
#
#
#
# a=input("")
#
# demo=a.split("->")
# l1=[]
# for i in range(0,len(demo)):
#     l1.append(int(demo[i]))
#
# a1=LinkeList(l1)
# #a1.printlist()
# a1.even_odd_reverse()
# a1.printlist()


