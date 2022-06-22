#source_0=[10,20,30,40,50,10,20,None,None] #linear aray



def CircularArray(cir, start, size):
   list_0=[None]*len(source_0)
   k = start
   for i in source_0:
      list_0[k]=i
      k = (k + 1) % len(cir)
   return list_0


print(CircularArray(source_0,3,7))



#circular_0=[20, None, None, 10, 20, 30, 40, 50, 10] #circular array which had starting index at 3 & size 7
def forwardIteration(cir, start, size):
     k = start
     for i in range(size):
         print(cir[k])
         k = (k + 1) % len(cir)

forwardIteration(circular_0,3,7)


#circular_0=[20, None, None, 10, 20, 30, 40, 50, 10] #circular array which had starting index at 3 & size 7
"""This code will iterate from 0, last index, last index-1,last index-2,.......... untill the size ends"""
def backwardIteration(cir, start, size):
        k = (start + size - 1) % len(cir) #k=0
        for i in range(size):
             print(cir[k])
             k = k - 1 # k will have values: 8,7,6,5,....
             if k == -1:
                   k = len(cir) - 1 #set to last index 8

print(backwardIteration(circular_0,3,7))


#circular_0=[20, None, None, 10, 20, 30, 40, 50, 10] #circular array which had starting index at 3 & size 7

def linearizingCircularArray(cir_arr, start,size):
    lin_arr = [None] * size # Initializing wit [None,None,None,..]
    k = start #setting starting index
    for i in range(size):
        lin_arr[i] = cir_arr[k]
        k = (k + 1) % len(cir_arr) #seting k's value to 3,4,5,6,7,8,0
    return lin_arr

print(linearizingCircularArray(circular_0,3,7))

circular_0 = [20, None, None, 10, 20, 30, 40, 50, 10]  # circular array which had starting index at 3 & size 7


def resizingCircularArray(cir_arr, start, size, new_capacity):
   # Linearized the circular array and makes [10, 20, 30, 40, 50, 10, 20, None, None, None, None, None]
   new_arr = [None] * new_capacity
   k = start
   for i in range(size):
      new_arr[i] = cir_arr[k]
      k = (k + 1) % len(cir_arr)

   """This makes [None, None, None, 10, 20, 30, 40, 50, 10, 20, None, None]"""
   # Creating a circular array
   list_0 = [None] * len(new_arr)
   k = start
   for i in new_arr:
      list_0[k] = i
      k = (k + 1) % len(new_arr)
   return list_0


print(resizingCircularArray(circular_0, 3, 7, 12))

cir_arr = [20, None, None, 10, 20, 30, 40, 50, 10]  # circular array which had starting index at 3 & size 7


def resizingCircularArray(cir_arr, start, size, new_capacity):
   # Linearized the circular array and makes [10, 20, 30, 40, 50, 10, 20, None, None, None, None, None]
   new_arr = [None] * new_capacity
   k = start
   for i in range(size):
      new_arr[i] = cir_arr[k]
      k = (k + 1) % len(cir_arr)

   """This makes [None, None, None, 10, 20, 30, 40, 50, 10, 20, None, None]"""
   # Creating a circular array
   list_0 = [None] * len(new_arr)
   k = start
   for i in new_arr:
      list_0[k] = i
      k = (k + 1) % len(new_arr)
   return list_0


def insert(cir_arr, start, size, elem, pos):  # pos means the index after the starting index
   if size == len(cir_arr):
      cir_arr = resizingCircularArray(cir_arr, start, size, size + 1)

   """From [20, None, None, 10, 20, 30, 40, 50, 10] , 
   we converted this to [10, 20, None, 10, 20, 30, 40, 10, 50]
   how?
   Nshift=3 thus will loopp for 3 times
   fr=0 to=1 cir_arr[1]=cir_arr[0]  [20,20,None,10,20,30,40,50,10]
   fr=8 to=0  cir_arr[0]=cir_arr[8] [10,20,None,10,20,30,40,50,10]
   fr=7  to=8 cir_arr[80=cir_arr[7] [10,20,None,10,20,30,40,50,50]
   now just set the value :
   cir_arr[7]=10
   Thus it will be [10,20,None,10,20,30,40,10,50]

   """
   nShifts = size - pos  # for pos 3, nshift=7-4
   fr = (start + size - 1) % len(cir_arr)  #
   to = (fr + 1) % len(cir_arr)
   for i in range(nShifts):  # will loop for nshift times
      cir_arr[to] = cir_arr[fr]
      to = fr
      fr = fr - 1
      if fr == -1:
         fr = len(cir_arr) - 1
   # Setings the index where we want to update the value
   idx = (start + pos) % len(cir_arr)
   cir_arr[idx] = elem
   size += 1
   return cir_arr


print(insert(cir_arr, 3, 7, 10, 4))





#cir_arr=[20, None, None, 10, 20, 30, 40, 50, 10] #circular array which had starting index at 3 & size 7


def removeByLeftShift(cir_arr, start, size,pos):
         #check index validity
         nShift = size - pos - 1
         idx = (start + pos) % len(cir_arr)
         removed = cir_arr[idx]
         to = idx
         fr = (to + 1) % len(cir_arr)
         for i in range(nShift):
              """fr=8 to=7 cir_arr[7]=cir_arr[8] [20, None, None, 10, 20, 30, 40, 10, 10]
                 for 0 to=8 cir_arr[80=cir_arr[0] [20, None, None, 10, 20, 30, 40, 10, 20]
                 fr=1 to=0 
                 Now, setting cir_arr[0]=None"""
              cir_arr[to] = cir_arr[fr]
              to = fr
              fr = (fr + 1) % len(cir_arr)
         cir_arr[fr-1] = None #Now, setting cir_arr[0]=None
         size -= 1
         return cir_arr

print(removeByLeftShift(cir_arr,3,7,4))


cir_arr=[20, None, None, 10, 20, 30, 40, 50, 10] #circular array which had starting index at 3 & size 7

# Remove value from circular array by right and changed the starting index of circular
def removeByRightShift(cir_arr, start, size,pos):
    """nShift=4
    to=7 for=6 cir_arr[7]=cir_arr[6] [20, None, None, 10, 20, 30, 40, 40, 10]
    to=6 fr=5                        [20, None, None, 10, 20, 30, 30, 40, 10]
    to=5 fr=4                        [20, None, None, 10, 20, 20, 30, 40, 10]
    to=4 fr=3                        [20, None, None, 10, 10, 20, 30, 40, 10]
    cir_arr[3]=None                  [20, None, None, None, 10, 20, 30, 40, 10]"""
    nShift = pos
    idx = (start + pos) % len(cir_arr)
    removed = cir_arr[idx]
    to = idx
    fr = (to - 1)
    if fr == -1:
        fr = len(cir_arr) - 1
    for i in range(nShift):
        print(fr)
        print(to)
        cir_arr[to] = cir_arr[fr]
        to = fr
        fr -= 1

        if fr == -1:
            fr = len(cir_arr) - 1
    cir_arr[start] = None
    start = (start + 1) % len(cir_arr)
    size -= 1
    return cir_arr

print(removeByRightShift(cir_arr,3,7,4)