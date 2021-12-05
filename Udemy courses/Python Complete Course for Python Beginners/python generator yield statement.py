def my_generator():
    n=1
    print("This is printed first")
    yield n #yielt pauses the function all its state and later continues from there
    #important to use next()

    n+=1
    print("This is printed second")
    yield n
    n+=1
    print("This is printed at last")
    yield n


a=my_generator()
#Iterrating using text
next(a)
next(a)
next(a)
print("Using for loop..")
#Iterating using for loop
for item in my_generator():
    print(item)