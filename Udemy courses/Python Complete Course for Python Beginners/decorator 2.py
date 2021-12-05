def my_smart_div(func):
    def inner_func(x,y):
        print("I am dividing ",x," and ",y)
        if y==0:
            print("Oops! Division by Zero is illegal")
            return
        return func(x,y)
    return inner_func # YOU CANNOT use inner_func()

#Generally , we decorate a function and reassign it as , go_divide=my_smart_div(go_divide)
@my_smart_div #when the decoration function is called, it will take go_divide() as  func and work
def go_divide(a,b):
    return a/b

print(go_divide(20,2))
print(go_divide(20,0))
