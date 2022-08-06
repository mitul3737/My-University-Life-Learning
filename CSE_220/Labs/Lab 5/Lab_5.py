#Stack with array solution
class Stack:
  def __init__(self, size=20):
      self.stack_array = []
      self._size = size



  def push(self, data):
      if len(self.stack_array) >= self._size:
          raise Exception('Stack overflow')
      else:
          self.stack_array.append(data)

  def pop(self):
      if len(self.stack_array) <= 0:
          raise Exception('Stack underflow')
      else:
          return self.stack_array.pop()

  def peek(self):
      if len(self.stack_array) <= 0:
          raise Exception('Stack underflow')
      else:
          return self.stack_array[-1]



my_stack = Stack()

str_0="1+2*[3*3+{4–5(6(7/8/9)+10)}–11+(12*8)/{13+13}]+14"
print(str_0)
idx=0
j=0
dict_0={}
flag=False
count=0
x=0
for i in str_0:
    j+=1
    if i in ('(', ')', '{', '}', '[', ']'):
        if i in ('(', '{', '['):
            if idx == 0:
                my_stack = Stack()
                my_stack.push(i)
                count+=1
                if i not in dict_0.keys():
                    dict_0[i] = [j]
                idx+= 1

            else:

                if i not in dict_0.keys():
                    dict_0[i] = [j]
                else:
                    dict_0[i].append(j)
                my_stack.push(i)
                count+=1

        elif i in (')', '}', ']'):
            if  count == 0:
                flag=False
                print("This expression is NOT correct.")
                print(f"Error at character # {j}. ‘{i}‘- not opened.")
                break
            elif my_stack.peek() == '(' or my_stack.peek() == '{' or my_stack.peek() == '[':
                var = my_stack.pop()
                count-=1
                if (var, i) == ('(', ')') or (var, i) == ('{', '}') or (var, i) == ('[', ']'):
                    x = dict_0[var].pop(0)
                    if count == 0:
                        flag = True

                else:
                    flag=False
                    x = dict_0[var].pop(0)
                    print("This expression is NOT correct.")
                    print(f"Error at character # {x}. ‘{var}‘- not closed.")
                    break

if count==0 and flag==True:
    print("This expression is correct.")











#Stack with Linked List
class Node:
    def __init__(self, value,next):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        new_node = Node(value,None)
        self.top = new_node
        self.height = 1


    def push(self, value):
        new_node = Node(value,None)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True

    def pop(self):
        #when we have no nodes in the stack
        if self.height == 0:
            raise Exception('Stack underflow')
        #when we have nodes in the stack
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp



str_0="1+2*(3/4)"
print(str_0)
idx=0
j=0
dict_0={}
flag=False
count=0
x=0
for i in str_0:
    j+=1 #counting index
    if i in ('(', ')', '{', '}', '[', ']'):
        # print(i)
        if i in ('(', '{', '['):
            if idx == 0: #used for the first time
                my_stack = Stack(i) #creating a stack
                count+=1#number of elements in stack
                if i not in dict_0.keys():
                    dict_0[i] = [j] #creating a dictionary with parentesis as key and index as value
                idx+= 1

            else:
                if i not in dict_0.keys(): #setting if the parenthises is for the first time in dictionary
                    dict_0[i] = [j] #creating a dictionary with parentesis as key and index as value
                else:
                    dict_0[i].append(j)
                my_stack.push(i) #pushing the parentesis into the stack
                count+=1#number of elements in stack

        elif i in (')', '}', ']'): #if the parentesis is closing
            if  count == 0: #if there is nothing in the stack
                flag=False
                print("This expression is NOT correct.")
                print(f"Error at character # {j}. ‘{i}‘- not opened.")
                break
            elif my_stack.top.value == '(' or my_stack.top.value == '{' or my_stack.top.value == '[':
                var = my_stack.pop() #pops the parentesis from the stack
                count-=1 #decreasing the number of elements in stack
                if (var.value, i) == ('(', ')') or (var.value, i) == ('{', '}') or (var.value, i) == ('[', ']'): #if we get a pair
                    x = dict_0[var.value].pop(0) #pops the index number from dictionary
                    if count == 0:#if no elements in the stack
                        flag = True #keep the flag true and keep the string moving

                else:#if the parentesis is not a pair
                    flag=False
                    x = dict_0[var.value].pop(0)
                    print("This expression is NOT correct.")
                    print(f"Error at character # {x}. ‘{var.value}‘- not closed.") #x is the popped index and var.value is the popped parentesis
                    break

if count==0 and flag==True: #still if the stack is empty and the flag is true
    print("This expression is correct.")




