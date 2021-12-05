#Demonstration
def make_decorated(func):
    def inner_function():
        print("I got decorated")
        func()
    return inner_function()
@make_decorated #make decorated will be used
def simple_func():
    print("I am a simple function")

simple_func()  #calling the simple_func()




'''

#Demonstration
def make_decorated(func):
    def inner_function():
        print("I got decorated")
        func()
    return inner_function()
def simple_func():
    print("I am a simple function")

decor=make_decorated(simple_func)
decor()  #calling decor

'''