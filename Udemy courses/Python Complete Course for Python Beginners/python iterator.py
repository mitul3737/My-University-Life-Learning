#iterable things return these or uses them:
#__iter__()
#__next__()
#1)
lst_0=[44,77,11,33]
our_iterator=iter(lst_0)
print(next(our_iterator)) #returns 44
print(next(our_iterator)) #returns 77
print(our_iterator.__next__()) #returns 11
print(our_iterator.__next__())#returns 33


#2)
class Power_of_two:
    def __init__(self,max=0):
        self.max=max
    def __iter__(self):
         self.n=0
         return self
    def __next__(self):
        if self.n<=self.max:
            result=2**self.n
            self.n+=1
            return result
        else:
            raise  StopIteration

print(Power_of_two.__doc__)
a=Power_of_two(4)
i=iter(a)
print(next(i)) #or print(i.__next__())
print(next(i))
print(next(i))
