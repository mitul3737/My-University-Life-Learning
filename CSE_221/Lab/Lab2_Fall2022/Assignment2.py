# 1
f1=open('input1.txt', 'r')
N=int(f1.readline())
id=[int(x) for x in f1.readline().split()]
marks=[int(x) for x in f1.readline().split()]

for i in range(N-1):
  temp1=marks[i+1]
  temp2=id[i+1]
  j=i
  while j>=0:
    if marks[j]<temp1:
      marks[j+1]=marks[j]
      id[j+1]=id[j]
    else:
      break
    j-=1
  marks[j+1]=temp1
  id[j+1]=temp2

str_id=''

for x in id:
  str_id+=str(x)+' '
f2=open('output1.txt', 'w')
f2.write(str_id) #adding outputs to the file
f1.close()
f2.close()

#2_b
hola = open("input2.txt", "r")  # takes input from the same directory
content = hola.readline()  # read the file
val = hola.read()
list_0 = val.split(" ")
list_1 = []
for i in list_0:
    list_1.append(int(i))


# mergesort algorithm in my way.
def merge(customList, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = customList[l + i]

    for j in range(0, n2):
        R[j] = customList[m + 1 + j]

    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            customList[k] = L[i]
            i += 1
        else:
            customList[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        customList[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        customList[k] = R[j]
        j += 1
        k += 1


def mergeSort(customList, l, r):
    if l < r:
        m = (l + (r - 1)) // 2
        mergeSort(customList, l, m)
        mergeSort(customList, m + 1, r)
        merge(customList, l, m, r)
    return customList


# output adding in the file
with open("output2.txt", "w") as content_file:
    out_0 = mergeSort(list_1, 0, len(list_1) - 1)
    for i in out_0:
        content_file.write(f"{i} ")

hola.close()
content_file.close()


#3
hola = open("input3.txt", "r")  # takes input from the same directory
content = hola.readline()  # read the file
val = hola.read()
list_0 = val.split(" ")
list_1 = []
for i in list_0:
    list_1.append(int(i))

def partition(customList, low, high):
    pivot = customList[high]
    i = low - 1
    for j in range(low,high):
        if customList[j] <= pivot:
            i += 1
            customList[i], customList[j] = customList[j], customList[i]
    customList[i+1], customList[high] = customList[high], customList[i+1]
    return (i+1)

def quickSort(customList, low, high):
    if low < high:
        pi = partition(customList, low, high)
        quickSort(customList, low, pi-1)
        quickSort(customList, pi+1, high)


with open("output3.txt", "w") as content_file:
    quickSort(list_1,0,len(list_1)-1)
    for i in list_1:
        content_file.write(f"{i} ")

hola.close()

#3b

list_1=[1,10,9,3,5,4,10]#provide the array
def partition(customList, low, high):
    i = low - 1
    pivot = customList[high]
    for j in range(low,high):
        if customList[j] <= pivot:
            i += 1
            customList[i], customList[j] = customList[j], customList[i]
    customList[i+1], customList[high] = customList[high], customList[i+1]
    return (i+1)

def kfind(customList, low, high, k):
    if low < high:
        pi = partition(customList, low, high)
        if pi == k:
            return customList[pi]
        elif pi > k:
            return kfind(customList, low, pi-1, k)
        else:
            return kfind(customList, pi+1, high, k)
    else:
        return customList[low]



val=int(input("Provide your desired nth value: ")) #provide your desired index
k = kfind(list_1,0,len(list_1)-1, val-1)
print(k)


#4-a
hola = open("input4.txt", "r")  # takes input from the same directory
val = hola.read()
list_0 = val.split("\n")
list_1 = []



class Queue:

    def __init__(self, size):

        self.queue = []
        self.front = self.rear = 0
        self.capacity = size

    def enque(self, name):


        if (self.capacity == self.rear):
            print("\nQueue is full")

        else:
            self.queue.append(name)
            customList=self.queue

            def bubbleSort(customList):
                for i in range(len(customList) - 1):
                    for j in range(len(customList) - i - 1):
                        if customList[j][1] > customList[j + 1][1]:
                            customList[j], customList[j + 1] = customList[j + 1], customList[j]


            bubbleSort(customList) #sorting the list
            self.rear += 1


    def seeDoctor(self):

        # If queue is empty
        if (self.front == self.rear):
            print("Queue is empty")


        else:
            x = self.queue.pop(0)
            self.rear -= 1

    def printQueue(self):

        if (self.front == self.rear):
            print("\nQueue is Empty")


        for i in self.queue:
            #just converting the list to the input format ['ABC', '1'] to ABC 1
            val_x=""
            for x in i:
                val_x+=x
                break
            print(val_x,"\n", end='')


q=Queue(50)

if __name__ == '__main__':
    for i in list_0:
        if i == "see doctor":
            q.seeDoctor()
        else:
            val_0 = []
            val_0 = i.split(" ")
            q.enque(val_0)



q.printQueue()
hola.close()


#4-b
hola = open("input4.txt", "r")  # takes input from the same directory
val = hola.read()
list_0 = val.split("\n")
list_1 = []



class Queue:

    def __init__(self, size):

        self.queue = []
        self.front = self.rear = 0
        self.capacity = size

    def enque(self, name):


        if (self.capacity == self.rear):
            print("\nQueue is full")

        else:
            self.queue.append(name)
            customList=self.queue
            #heap sort code
            def heapify(customList, n, i):
                smallest = i
                l = 2 * i + 1
                r = 2 * i + 2
                if l < n and customList[l][1] < customList[smallest][1]:
                    smallest = l


                if r < n and customList[r][1] < customList[smallest][1]:
                    smallest = r


                if smallest != i:
                    customList[i], customList[smallest] = customList[smallest], customList[i]
                    heapify(customList, n, smallest)

            def heapSort(customList):
                n = len(customList)
                for i in range(int(n / 2) - 1, -1, -1):
                    heapify(customList, n, i)

                for i in range(n - 1, 0, -1):
                    customList[i], customList[0] = customList[0], customList[i]
                    heapify(customList, i, 0)



            heapSort(customList) #sorting the list
            customList.reverse() #reverse it because generally it makes descending order
            self.rear += 1


    def seeDoctor(self):

        # If queue is empty
        if (self.front == self.rear):
            print("Queue is empty")


        else:
            x = self.queue.pop(0)
            self.rear -= 1

    def printQueue(self):

        if (self.front == self.rear):
            print("\nQueue is Empty")


        for i in self.queue:
            #just converting the list to the input format ['ABC', '1'] to ABC 1
            val_x=""
            for x in i:
                val_x+=x
                break
            print(val_x,"\n", end='')


q=Queue(50)

if __name__ == '__main__':
    for i in list_0:
        if i == "see doctor":
            q.seeDoctor()
        else:
            val_0 = []
            val_0 = i.split(" ")
            q.enque(val_0)



q.printQueue()
hola.close()


#4_c
"""The output for bubble sort is EWQ, OPN, TYU but it is OPN, ABC, TYU for the heap sort. Because bubble sort just swapped the first two elements but heap sort swapped the first and the last elements. 
But for heap sort, we collected date in heap bindary way and then we reversed it atlast because here it we create the code to descend it . So, because of the different approach in algorithm, the output is different."""

#4_d

"""Time complexity of bubble sort is O(n^2) and time complexity of heap sort is O(nlogn). So, heap sort is more efficient than bubble sort."""

"""So, the graph of the time complexity of heap sort is more near to x axis than bubble sort. So, heap sort is more efficient than bubble sort."""
def bubbleSort(customList):
    for i in range(len(customList) - 1):
        for j in range(len(customList) - i - 1):
            if customList[j] > customList[j + 1]:
                customList[j], customList[j + 1] = customList[j + 1], customList[j]


def heapify(customList, n, i):
        smallest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and customList[l] < customList[smallest]:
            smallest = l

        if r < n and customList[r] < customList[smallest]:
            smallest = r

        if smallest != i:
            customList[i], customList[smallest] = customList[smallest], customList[i]
            heapify(customList, n, smallest)

def heapSort(customList):
       print("yes")
       n = len(customList)
       for i in range(int(n / 2) - 1, -1, -1):
           heapify(customList, n, i)

       for i in range(n - 1, 0, -1):
           customList[i], customList[0] = customList[0], customList[i]
           heapify(customList, i, 0)



#change the value of

import time
import math
import matplotlib.pyplot as plt
import numpy as np
n=5
value = [[4,6,1,4,2,9,10,56,3,11,-1,45],[3,8,3,1,7,5,9,-12,0,4,14],[-3,7,0,12,4,7,3,2,12],[1,6,-2,3,0,12,3,14,15,11,18,10,3],[4,3,8,2,1,9,5,3,10,16,12,23,9,-4,-2]]
y = [0 for i in range(n)]
z = [0 for i in range(n)]

for i in range(4):
    start = time.time()
    heapSort(value[i+1])
    y[i+1]= time.time()-start
    start = time.time()
    bubbleSort(value[i+1])
    z[i+1]= time.time()-start
x_interval = math.ceil(n/10)

for x in value:
    plt.plot(x, y, 'r')
    plt.plot(x, z, 'b')
    plt.xticks(np.arange(min(x), max(x) + 1, x_interval))
    plt.xlabel('n-th position')
    plt.ylabel('time')
    plt.title('Comparing Time Complexity!')
    plt.show()


