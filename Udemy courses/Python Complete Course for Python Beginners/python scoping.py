def outer_function():
    global a
    a=20
    def inner_function():
        global a
        a=30
        print('Third a=',a)
    inner_function()
    print('Fourth a=',a)

a=10
print('First a=',a)
outer_function()
print('Second a=',a)