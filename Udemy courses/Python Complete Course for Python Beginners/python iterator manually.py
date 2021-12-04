#making an iterator
class Pow_of_two:
    def __init__(self,max=0):
        self.max=max
    def __iter__(self):
        self.n=0
        #print("self.n value:",self.n)
        return self
    def __next__(self):
        if self.n<=self.max:
            #print("self.n",self.n)
            #print("self.max",self.max)
            result=2**self.n # 2^(self.n)
            self.n+=1
            return result
        else:
            raise StopIteration

#print(Pow_of_two.__doc__)
a=Pow_of_two(4) #a is an object of Pow_of_two
i=iter(a) #using the object a in iter method
print(next(i))
print(next(i))
print(next(i))


"""process :
a object
i object of next method 
print(next(i)) which is print(next(4))
self.n=0
self.max=4
result =2^0
return 2^0
again,
self.n=1
self.max=4
result =2^1
return 2^1

self.n=2
self.max=4
result =2^2
return 2^2"""
