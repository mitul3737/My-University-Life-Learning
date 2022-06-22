"""Linear array has fixed size
for example Linear Array= [10,20,30,40,50,None,None]
This is a Linear array length is 7 but you can see that, after the None, there can be only None but no value
consistently value can be added. If we want to add a value 60, we can add it after 50 only
at index 5
ex:
Before adding 60
[10,20,30,40,50,None,None]
after adding it to index 5, [10,20,30,40,50,60,None]

but we can not add it at index 6
ex: [10,20,30,40,50,None,60] is not possible"""

#Linear Array
"""Linear_array=[10,20,30,40,50,60]
#If we have a liear array [10,20,30,40,50,60] and leftshift 3 times
#[20,30,40,50,60,0]
#[30,40,50,60,0,0]
#[40,50,60,0,0,0]
#Now we will shift k contents to move left.

def shiftLeft(source,k):
    # Checking size of elements (how many values are there)
    size=0
    for m in range(0,len(source)):
        if source[m]>0:
            size+=1

    for p in range(0,k): #how many times we are going to left shift
        #[10,20,30,40,50,60]
        #we have size 6
        #now for te 1st time in loop we will make [20,30,40,50,60,60]
        #Here, look carefully 5 values has been changed. Thus we will take range(0,size-1) == [0,1,2,3,4]
        #then we will make the last index as 0
        #[20,30,40,50,60,0]
        #1st loop done!
        #Same process goes for other steps
        for i in range(0,size-1):
            source[i]=source[i+1] #Changing values
        source[size-1]=0 # Setting the last value as 0
    return print(source)
shiftLeft(Linear_array,3)



#Now we will make [10,20,30,40,50,60] to this [40, 50, 60, 10, 20, 30]
def rotateLeft(source,k):

    #checking the size of the array
    size=0
    for m in range(0,len(source)):
        if source[m]>0:
            size+=1

    for p in range(0,k):#looping k times
        #[10,20,30,40,50,60] we will make this to
        #[20,30,40,50,60,10]
        #[30,40,50,60,20,20]
        #[40,50,60,10,20,30]
        x=source[0] #we are saving the 1st value because when we will left shift,this value will be gone. Also, we can use this value to the last index
        for i in range(0,size-1):
            source[i]=source[i+1]
        source[size-1]=x
    return print(source)

rotateLeft(Linear_array,3)


def shiftRight(source, k):
    # Checking the size
    size = 0
    for m in range(0, len(source)):
        if source[m] > 0:
            size += 1

    for k in range(0, k):  # looping for k times
        #Shifting the array [10,20,30,40,50,60] to 
        #[10,10,20,30,40,50]->[0,10,20,30,40,50]
        #[0,0,10,20,30,40] -> [0,0,10,20,30,40]
        #[0,0,0,10,20,30] ->[0,0,0,10,20,30]

        for i in range(size - 1, 0, -1):  # iterate from last value to 1
            source[i] = source[i - 1]
        source[0] = 0

    return print(source)


shiftRight(Linear_array, 3)


def rotateRight(source, k):
    # Cheecking size
    size = 0
    for m in range(0, len(source)):
        if source[m] > 0:
            size += 1

    for k in range(0, k):
        #From the array [10,20,30,40,50,60]
        #make this to
        #[10,10,20,30,40,50]->[60, 10, 20, 30, 40, 50]
        #[60,60,10,20,30,40]->[50, 60, 10, 20, 30, 40]
       # [50,50,60,10,20,30]->[40, 50, 60, 10, 20, 30]
        x = source[size - 1]  # saving the last indexes value

        # Right shift
        for i in range(size - 1, 0, -1):
            source[i] = source[i - 1]
        source[0] = x

    return print(source)


rotateRight(Linear_array, 3)

#From this list [10,20,30,40,50,90,30] to [10, 20, 30, 50, 90, 30, 0]
#removes 40 from the index 3 and left shifts


def remove(source, size, idx):
    if idx >= size:
        print("Index out of range for Linear array")
    else:
        # if we have max size
        if size == len(array_0):
            for i in range(idx + 1, size):
                source[i - 1] = source[i]
            source[size - 1] = 0
            return source
        else:  # if we have less than max size

            # Left shifts
            for i in range(idx, size + 1):
                source[i] = source[i + 1]
            source[size + 1] = 0
            return source


print(remove(Linear_array, 7, 3))



array_0=[10,2,30,2,50,2,2,8,9]

def remove(source, size, idx):
    if idx >= size:
        print("Index out of range for Linear array")
    else:
        # if we have max size
        if size == len(array_0):
            for i in range(idx + 1, size):
                source[i - 1] = source[i]
            source[size - 1] = 0
            return source
        else:  # if we have less than max size

            # Left shifts
            for i in range(idx, size + 1):
                source[i] = source[i + 1]
            source[size + 1] = 0
            return source


def removeAll(source, size, element):
    for k in range(0, size):
        if source[k] == element:
            new = k #saving the index number to new
            #from the desired index to size
            for i in range(new, size):
                if source[i] == element:#finds the index of the desired element to remove it
                    remove(source, size, i)

    return print(source)


removeAll(array_0, 9, 8)
"""

#source_0=[10,20,30,40,50,0,0]
#Bassic codes

#Iteration
def iteration(source_0):
    for i in range(len(source_0)):
        print(source_0[i])
iteration(source_0)


#ReverseIteration
def reverseIteration(source):
      for i in range(len(source) - 1, -1, -1):#last index to 0
              print(source[i])

reverseIteration(source_0)



def copyArray(source):
     newArray = [None] * len(source)
     for i in range(len(source)):
             newArray[i] = source[i]
     return newArray

def copyArray(source):
    newArray = [None] * len(source)
    #creates a list of same length with None
    #[None,None,.............]

    for i in range(len(source)):
        newArray[i] = source[i]#Copies each value
    return newArray #Returns the list

print(copyArray(source_0))


def resizeArray(oldArray, newCapacity):
    newArray = [None] * newCapacity  # making a list with all None

    for i in range(len(oldArray)):
        newArray[i] = oldArray[i]  # copying all the value
    return newArray


print(resizeArray(source_0, 10))


#Left shift 1time
#source_0=[10,20,30,40,50,60,70]
def shiftLeft(arr):
    for i in range(1, len(arr)):
        arr[i - 1] = arr[i]
    arr[len(arr) - 1] = None
    return arr


print(shiftLeft(source_0))


#source_0=[10,20,30,40,50,60,70]
#Right shift
def shiftRight(arr):
    for i in range(len(arr) - 1, 0, -1):
        print(i)
        arr[i] = arr[i - 1]
    arr[0] = None
    return arr


print(shiftRight(source_0))


#source_0=[10,20,30,40,50,60,0]
def insertElement(arr, size, elem, index):
# Practice how to throw exception if there
    if size == len(arr):#The list is full
         print("No space left. Insertion failed")

    #If not full
    else:
        for i in range(size, index, -1):
            """from size to the index for ex: print(insertElement(source_0,6,3,2)) 
            it will be 6,5,4,3"""
            arr[i] = arr[i - 1] #Right shifting
            """[10,20,30,30,40,50,60] is made and then changes the 3rd index to element value
            so, it is [10,20,3,30,40,50,60]"""
        arr[index] = elem #Inserting element
        return arr
print(insertElement(source_0,6,3,2))


#source_0=[10,20,30,40,50,10,20,0]
def removeElement(arr, index, size):
    if size==len(source_0): #size  and length equal
        for i in range(index + 1, size):
              arr[i - 1] = arr[i] #Shifting left from
        arr[size - 1] = None #Making last space em
        return arr
    else: #not equal
        for i in range(index + 1, size+1):
              arr[i - 1] = arr[i] #Shifting left from
        arr[len(source_0)-1] = None #Making last space em or, arr[size-1]=None
        return arr


print(removeElement(source_0,1,7))




