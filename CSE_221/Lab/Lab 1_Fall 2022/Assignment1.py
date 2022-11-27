#1(a)
hola=open("input1a.txt", "r")#takes input from the same directory
content=hola.read() #read the file
with open("output1a.txt", "w") as content_file: #creates an output file
    val=content.split() #using input file, splits the string into a list
    inp=val[0] #takes the first value for input
    for i in val[1:]: #runs the whole list to iterate
        if int(i) % 2 == 0: #checks if the number is even
            content_file.write(f"{i} is an Even number.\n")
        else:
            content_file.write(f"{i} is an Odd number.\n")
hola.close() #closes the file


#1 (b)

with open("output1b.txt", "w") as content_file: #creates an output file
    hola=open("input1b.txt", "r")#takes input
    content=hola.readline() #read the file
    for i in range(0, int(content)):
        val=hola.readline()
        inp=val.split()
        valx=inp[2]
        if valx == "+":
            content_file.write(f"The result of {inp[1]} + {inp[3]} is {int(inp[1]) + int(inp[3])}\n")
        elif valx == "-":
            content_file.write(f"The result of {inp[1]} - {inp[3]} is {int(inp[1]) - int(inp[3])}\n")
        elif valx == "*":
            content_file.write(f"The result of {inp[1]} * {inp[3]} is {int(inp[1]) * int(inp[3])}\n")
        elif valx == "/":
            content_file.write(f"The result of {inp[1]} / {inp[3]} is {int(inp[1]) / int(inp[3])}\n")
hola.close() #closes the file"""




#2
def fibonacci_1(n):
    if n < 0:
        print("Invalid input!")
    elif n <= 1:
        return n
    else:
        return fibonacci_1(n-1)+fibonacci_1(n-2)
n = int(input("Enter a number: "))
nth_fib = fibonacci_1(n)
print("The {} th fibonacci number is {}.".format(n, nth_fib))





def fibonacci_2(n):
    if n<0:
        return "Invalid Input"
    if n<=1:
        return n
    fib = [0] * (n+1)
    fib[0] = 0
    fib[1] = 1
    for i in range(2,n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]
n = int(input("Enter a number: "))
nth_fib = fibonacci_2(n)
print("The {} th fibonacci number is {}.".format(n, nth_fib))




import time
import math
import matplotlib.pyplot as plt
import numpy as np
#change the value of n for your own experimentation
n = 30
x = [i for i in range(n)]
y = [0 for i in range(n)]
z = [0 for i in range(n)]
for i in range(n-1):
    start = time.time()
    fibonacci_1(x[i+1])
    y[i+1]= time.time()-start
    start = time.time()
    fibonacci_2(x[i+1])
    z[i+1]= time.time()-start
x_interval = math.ceil(n/10)
plt.plot(x, y, 'r')
plt.plot(x, z, 'b')
plt.xticks(np.arange(min(x), max(x)+1, x_interval))
plt.xlabel('n-th position')
plt.ylabel('time')
plt.title('Comparing Time Complexity!')
plt.show()




#3
"""The algorithm provided here compares all items in the list regardless of
whether the list is already sorted or not.Comparing all values is a waste of
time and resources if the given list has already been sorted.By improving the bubble sort,
we can cut down on time and resources spent on pointless iterations."""


hola=open("input3.txt", "r")#takes input from the same directory
content=hola.read() #read the file
with open("output3.txt", "w") as content_file: #creates an output file
    val=content.split()
    list_0=[]
    for x in val[1:]:
        list_0.append(int(x))
    def bubbleSort(array):
        for i in range(len(array)):# loop through each element of array
            swapped_already = False #tracks swapping
            for j in range(0, len(array) - i - 1):
                if array[j] > array[j + 1]:# compare two adjacent elements
                    temp = array[j]# We need to swap if elements are not in the right order
                    array[j] = array[j + 1]
                    array[j + 1] = temp
                    swapped_already = True
            if not swapped_already: #If the array is already sorted, then break the loop
                break
    inp = list_0
    bubbleSort(inp)
    for m in inp: #wrtiting it in the output file
        content_file.write(f"{m} ")




#4
#Task_4
input4_testCase1 = open("input4.txt", "rt")
output4 = open("output4.txt", "w")

N_0 = int(input4_testCase1.readline().strip())
val = (input4_testCase1.readlines())


id_y = val[0].split()# Making a list of Student ID's.
Si = [0]*N_0#print(Student id's)
idx_Si = 0
for i in id_y:
  Si[idx_Si] = int(i)
  idx_Si += 1


marks_0 = val[1].split()# making a list of student marks.
#print(marks)
Sm = [0]*N_0
idx_Sm = 0
for i in marks_0:
  Sm[idx_Sm] = int(i)
  idx_Sm += 1

for i in range(len(Sm)): #Selection sort applied to have minimum swaps
  for j in range(i):
    if Sm[j]<Sm[i]:
      temp_Sm = Sm[j]# swapping marks array
      Sm[j] = Sm[i]
      Sm[i] = temp_Sm
      temp_Si = Si[j]# swapping ID array
      Si[j] = Si[i]
      Si[i] = temp_Si

min_0 = 0
for i in range(N_0):# Sorting ID array when more than one individual have the same marks.
  for i in range(N_0-1):
    if Sm[i] == Sm[i+1]:
      if Si[i] > Si[i+1]:
        Temp = Si[i]
        Si[i] = Si[i+1]
        Si[i+1] = Temp

for i in range(N_0):#creating the text file to write answers
  ans = f"ID: {Si[i]} Mark: {Sm[i]} \n"
  output4.write(ans)

input4_testCase1.close() #closing the input file
output4.close() #closing the file



#Task 5
def asci(var):
    sum=0
    for i in var:
        sum+=ord(i)
    return sum

def convert(tm):
  lis=tm.split(':')
  time=int(lis[0])+int(lis[-1])/60
  return time

def selsort(a):
    for i in range(len(a)):
        min = i
        for j in range(i + 1, len(a)):
            if a[min] > a[j]:
                min = j
        a[i], a[min] = a[min], a[i]
    return a


count=0
with open("input5.txt", "r") as file:
  num=file.readline()
  name=[]
  val_0=[]
  place_0=[]
  time_0=[]

  for i in range(int(num)):
      sen=file.readline()
      lis=sen.split()
      name.append(lis[0])
      place_0.append(lis[-3])
      time_0.append(lis[-1])

  for i in name:
      value=asci(i)
      val_0.append(value)

  for i in range(len(val_0)):#sort based on asci value
      min_num=val_0[i]
      nam=name[i]
      min_ind=i
      for j in range(i+1,len(val_0)):
          if val_0[j]<min_num:
              min_num=val_0[j]
              min_ind = j
              nam=name[j]

      val_0[i],val_0[min_ind]=val_0[min_ind],val_0[i]
      name[i],name[min_ind]=name[min_ind],name[i]
      place_0[i],place_0[min_ind]=place_0[min_ind],place_0[i]
      time_0[i],time_0[min_ind]=time_0[min_ind],time_0[i]


  for i in range(len(val_0)):
      nam=name[i]
      min_ind=i
      for j in range(i+1,len(val_0)):
          if ord(nam[0])>ord(name[j][0]):
              min_ind = j
              nam=name[j]

      val_0[i],val_0[min_ind]=val_0[min_ind],val_0[i]
      name[i],name[min_ind]=name[min_ind],name[i]
      place_0[i],place_0[min_ind]=place_0[min_ind],place_0[i]
      time_0[i],time_0[min_ind]=time_0[min_ind],time_0[i]


  for i in range(len(val_0)):
        nam=name[i]
        min_ind=i
        for j in range(i+1,len(val_0)):
            if ord(nam[0])==ord(name[j][0]):
                if ord(nam[1])>ord(name[j][1]):
                    min_ind=j
                    nam = name[j]
        val_0[i],val_0[min_ind]=val_0[min_ind],val_0[i]
        name[i],name[min_ind]=name[min_ind],name[i]
        place_0[i],place_0[min_ind]=place_0[min_ind],place_0[i]
        time_0[i],time_0[min_ind]=time_0[min_ind],time_0[i]


  file_o=open("output5.txt","w")
  for i in range(len(name)):
      file_o.write(f"{name[i]} will departure for {place_0[i]} at {time_0[i]}"+"\n")
  file_o.close()
