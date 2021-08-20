def foo_moo(val_1):
    if val_1%2==0 and val_1%3==0:
        val_0="FooMoo"
    elif val_1%2==0:
         val_0="Foo"
    elif val_1%3==0:
          val_0="Moo"
    else:
         val_0="Boo"

    return val_0
print(foo_moo(2))