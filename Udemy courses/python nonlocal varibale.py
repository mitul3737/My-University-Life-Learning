def outer():
    x="local"
    def inner():
        nonlocal x #making the x variable of outer() global
        x="hola"
        print("inner",x)

    inner()
    print("outer:",x)

outer()