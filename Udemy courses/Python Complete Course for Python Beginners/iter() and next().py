#iter() method
list_1=[44,77,11,33]
iter_1=iter(list_1) #creating iterator object by calling iter class
print(iter_1)

#next() method
print(next(iter_1)) #now using next class while using iter_1 object to get 1st value
print(next(iter_1)) # to get 2nd value as used 2nd time

print(iter_1.__next__()) #get 3rd value