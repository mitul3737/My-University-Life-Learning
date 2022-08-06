
"""Remember, linear arrays can never have None in middle...after none, there can not be any values inserted. They need to
        add values instead of None and thn add None if needed
        For ex:
        Linear_1=[1,2,3,4,None,None] is possible
        but Linear_2=[1,2,3,4,5,None,3,7,9] is not possible .
        This might be possible in circular arrays ... Thus in circular arrays codes, we just took self.size because we know
        that linear area values are consistent .
        for ex: Linear_1 has value 1,2,3,4

        #Converting Linear_1 to self.cir
        so, while we convert this Linear_1 to circular and assume the starting index for circular should be 2 and size is 4
        then the circular array will be : [None,None,1,2,3,4]
        Look carefully, the 1st value of linear array is in index 2 of circular array .
        Here we have values after None
        But in Linear_1 has no value after None

        Summary: Thus we will use self.size to iterate"""

class CircularArray:
    def __init__(self, lin, st, sz):
        # Initializing Variables
        self.start = st
        self.size = sz
        self.cir = [None] * len(lin)

        k = self.start  # Taking the starting index so that we can set the circular arrays starting value from there
        # Iterate through the linear array to create the circular array
        for x in lin:
            i = k % len(lin)
            self.cir[i] = x
            k += 1

    def printFullLinear(self):
        str_0 = ""  # taking a string variable
        # Iterate through the circular array and saving them in string to show in desired output format
        for i in self.cir:
            str_0 += str(i) + ", "
        print(str_0[:-2])

    def printBackward(self):
        str_0 = ""  # taking a string variable


        """Assume that you have a circular array=[40,None,10,20,30]
        We will insert first 40, then 30, then , 20 then 10 .we will not take None. Done!
        How to do that ? 
        We need index 0 , 4, 3,2 right? Why are not we thinking of index 1? Because the none is there and as we used
        self.size, and we have go all the values we needed . 
        """
        # setting the  k variable to 0
        k = (self.start + self.size - 1) % len(self.cir)
        for i in range(self.size):
            str_0 += str(self.cir[k]) + ", "  # Saving in string to get desired output
            k = k - 1  # first setting k to -1
            """Thus for a circular array which has length 5, we get the index 4,3,2 too"""
            if k == -1: # when we have k=-1 , we then set it to k=len(self.cir)-1 so that we get the last index
                k = len(self.cir) - 1
        print(str_0[:-2])


    def printForward(self):

        """For a linear array_1=[10,20,30,40,None]
        and converting it to circular array =[40,None,10,20,30] which has starting index 2
        Now to print forward from circular array, we need to have 10 ,20, 30,40 . So check the index of them from
        circular array. they are 2,3,4,0, Right?"""
        str_0 = ""
        k = self.start  # Setting the starting index to k (by following this step, for a staring index 2 and size 5, we have indexes for k =2)
        for i in range \
                (len(self.cir)):  # We are not using len(self.cir) cz we don't need to iterate all. We know where None starts
            if self.cir[k] != None:
                str_0 += str(self.cir[k]) + ", "
            k = (k + 1) % len(self.cir)  # changing the value
            """by following this step, for a staring index 2 and size 5, we have indexes for k =3,4,0"""
        print(str_0[:-2])


    def linearize(self):  # Medium

        """Assume that you have a circular object [40,None,10,20,30]
        it has the staring index at index 2 . So, after linearazing, we should have
        [10,20,30,40,None]
        so, from the circular index, we need index 2,3,4,0 where the size for circular array is 4"""
        lin_arr = [None] * self.size  # Initializing with empty spaces [None,None,None,............] in a new list
        k = self.start
        # adding the values of circlar array to the new list

        for i in range(self.size):
            lin_arr[i] = self.cir[k]
            k = (k + 1) % len(self.cir)
        self.cir = lin_arr  # Copied the new list to the circular array
        return self.cir


    def resizeStartUnchanged(self, newcapacity):  # Medium
        """If we have a circular array=[40,None,10,20,30]
        increase the size to 8 and , we need to have something like this [None,None,10,20,30,40,None,None]
        So, first we will make [None,None,None,None,None,None,None,None] and
        make it linear [10,20,30,40,None,None,None,None]
        Then we will again start taking inputs from the starting index to keep it same
        Then create a circular array again with the same starting index"""



        """Making [40,None,10,20,30,0 to [10,20,30,40,None,None,None,None]"""
        # linearization
        new_arr = [None] * newcapacity
        k = self.start
        for i in range(self.size):
            new_arr[i] = self.cir[k]
            k = (k + 1) % len(self.cir)
        # print(new_arr)


        """Making [10,20,30,40,None,None,None,None] to [None,None,10,20,30,40,None,None]"""
        # creating a circular array again
        k = self.start
        self.cir = [None] * newcapacity
        for x in new_arr:
            i = k % len(new_arr)
            self.cir[i] = x
            k += 1

    def palindromeCheck(self):  # Hard
        """From this linear array [10, 20, 30, 20, 10, None, None]
        from the linear array we made this circular array = [10,None,None,10,20,30,20]

       Our task is to check if the circular array is palindrome or not?
       Look carefully...we can make the circular to linear to a new list . Thus [10,20,30,20,10]
       Now we can check if that is equal from starting and end using list_0 == list_0[::-1]:
       Done!
    """
        # printing forward to get circular to linear
        list_0 = []
        k = self.start
        for i in range(self.size):
            list_0 += [self.cir[k]]
            k = (k + 1) % len(self.cir)
        # creating a list with valied inputs


        if list_0 == list_0[::-1]:  # Checking the list from beginning and back
            print("This array is a palindrome")
        else:
            print("This array is NOT a palindrome")


    """For a Linear array [10, 20, -30, 20, 50, 30, None]
    Starting index was 5, thus circular array [-30,20,50,30,None,10, 20]
    We will sort it in a new list =[-30,10,20,20,None,30,50]
    Now we will create a circular array having the same starting index=5
    Thus [20, 20, None, 30, 50, -30, 10] and save it to self.cir 
    """
    def sort(self):
        # print(self.cir)
        list_x = self.cir  # Copying the circular array
        for i in range(len(list_x)):
            for j in range(i + 1, len(list_x)):
                if list_x[i] != None and list_x[j] != None:
                    if list_x[i] > list_x[j]:
                        list_x[i], list_x[j] = list_x[j], list_x[i]
        # print(list_x) "ex: [-30, 10, 20, 20, None, 30, 50]"
        # Created a sorted list list_x
        cx = CircularArray(list_x, self.start, self.size)  # creating an object using that sorted list
        '''this creates a circular object sorted from beginning
        '''
        # print(cx.cir) """[20, 20, None, 30, 50, -30, 10]"""
        self.cir = cx.cir

    def equivalent(self, cir_arr):
        k = self.start
        l = cir_arr.start
        list_1 = []
        list_2 = []
        """For this 2 circular objects, we will just create 2 lists to store their values and then compare"""
        for i in range(len(self.cir)):
            if self.cir[k] != None:
                list_1 += [self.cir[k]]
            k = (k + 1) % len(self.cir)

        # making forward/linerized
        for i in range(len(cir_arr.cir)):
            if cir_arr.cir[l] != None:
                list_2 += [cir_arr.cir[l]]
            l = (l + 1) % len(cir_arr.cir)

        if list_1 == list_2:  # comparing those lists
            return True
        else:
            return False





    def intersection(self, c2):
        k = self.start
        l = c2.start
        list_1 = []
        list_2 = []
        list_3 = []

        def count_x(list, x):
            count_r = 0
            for i in list:
                if i == x:
                    count_r += 1
            return count_r

        # make forward code
        for i in range(len(self.cir)):
            if self.cir[k] != None:
                list_1 += [self.cir[k]]
            k = (k + 1) % len(self.cir)

        # making forward/linerized
        for i in range(len(c2.cir)):
            if c2.cir[l] != None:
                list_2 += [c2.cir[l]]
            l = (l + 1) % len(c2.cir)

        # Creating an unique list of all numbers
        unique_l = []
        for u in list_1:
            if u not in unique_l:
                unique_l += [u]

        # created unique list of all numbers, so that we don't need to worry to remove later
        for x in unique_l:
            max_0 = count_x(list_1, x)  # check the count of a number in list 1
            min_0 = count_x(list_2, x)  # check the count of number in list 2

            # check if the number exists in both list
            if max_0 > 0 and min_0 > 0:
                # if a number is equal times in bot sides
                """ex: list_1=[10,3,10,4]
                list_2=[5,10,10,9]
                here max_0 & min_0 for 10 is 2"""
                if max_0 - min_0 == 0:
                    for i in range(min_0):  # adding it that many times
                        "for the example upper, min_0=max_0=2 thus 100 should be twice here"
                        list_3 += [x]

                elif max_0 - min_0 > 0:
                    """ex: list_1=[10,10,20,50,60,1]
                    list_2=[10,4,6,3,1]
                    here max_0 for 10 is 2 and min_0 for 10 is 1
                    thus we have atleast one 10 in common"""
                    for i in range(max_0 - min_0):  # thus tood max_0-min_0=2-1=1 times
                        list_3 += [x]

                elif max_0 - min_0 < 0:
                    """ex: list_1=[10,20,20,10,4]
                    list_2=[20,20,20,10,5]
                    here max_0 for 20 is 2 and min_0 for 20 is 3 
                    Thus we need it 2 times"""
                    for i in range(max_0):  # max_0=2 and min_0=3 thus took max_0
                        list_3 += [x]

        return list_3

# Tester class. Run this cell after completing methods in the upper cell and
# check the output

lin_arr1 = [10, 20, 30, 40, None]

print("==========Test 1==========")
c1 = CircularArray(lin_arr1, 2, 4)
c1.printFullLinear() # This should print: 40, None, 10, 20, 30
c1.printForward() # This should print: 10, 20, 30, 40
c1.printBackward() # This should print: 40, 30, 20, 10

print("==========Test 2==========")
c1.linearize()
c1.printFullLinear() # This should print: 10, 20, 30, 40

print("==========Test 3==========")
lin_arr2 = [10, 20, 30, 40, 50]
c2 = CircularArray(lin_arr2, 2, 5)
c2.printFullLinear() # This should print: 40, 50, 10, 20, 30
c2.resizeStartUnchanged(8) # parameter --> new Capacity
c2.printFullLinear() # This should print: None, None, 10, 20, 30, 40, 50, None

print("==========Test 4==========")
lin_arr3 = [10, 20, 30, 20, 10, None, None]
c3 = CircularArray(lin_arr3, 3, 5)
c3.printForward() # This should print: 10, 20, 30, 20, 10
c3.palindromeCheck() # This should print: This array is a palindrome

print("==========Test 5==========")
lin_arr4 = [10, 20, 30, 20, None, None, None]
c4 = CircularArray(lin_arr4, 3, 4)
c4.printForward() # This should print: 10, 20, 30, 20
c4.palindromeCheck() # This should print: This array is NOT a palindrome

print("==========Test 6==========")
lin_arr5 = [10, 20, -30, 20, 50, 30, None]
c5 = CircularArray(lin_arr5, 5, 6)
c5.printForward() # This should print: 10, 20, -30, 20, 50, 30
c5.sort()
c5.printForward() # This should print: -30, 10, 20, 20, 30, 50

print("==========Test 7==========")
lin_arr6 = [10, 20, -30, 20, 50, 30, None]
c6 = CircularArray(lin_arr6, 2, 6)
c7 = CircularArray(lin_arr6, 5, 6)
c6.printForward() # This should print: 10, 20, -30, 20, 50, 30
c7.printForward() # This should print: 10, 20, -30, 20, 50, 30
print(c6.equivalent(c7)) # This should print: True

print("==========Test 8==========")
lin_arr7 = [10, 20, -30, 20, 50, 30, None, None, None]
c8 = CircularArray(lin_arr7, 8, 6)
c6.printForward() # This should print: 10, 20, -30, 20, 50, 30
c8.printForward() # This should print: 10, 20, -30, 20, 50, 30
print(c6.equivalent(c8)) # This should print: True

print("==========Test 9==========")
lin_arr8 = [10, 20, 30, 40, 50, 60, None, None, None]
c9 = CircularArray(lin_arr8, 8, 6)
c6.printForward() # This should print: 10, 20, -30, 20, 50, 30
c9.printForward() # This should print: 10, 20, 30, 40, 50, 60
print(c6.equivalent(c9)) # This should print: False

print("==========Test 10==========")
lin_arr9 = [10, 20, 30, 40, 50, None, None, None]
c10 = CircularArray(lin_arr9, 5, 5)
c10.printFullLinear() # This should print: 40, 50 , None, None, None, 10, 20, 30
lin_arr10 = [5, 40, 15, 25, 10, 20, 5, None, None, None, None, None]
c11 = CircularArray(lin_arr10, 8, 7)
c11.printFullLinear() # This should print: 10, 20, 5, None, None, None, None, None, 5, 40, 15, 25
output = c10.intersection(c11)
print(output) # This should print: [10, 20, 40]