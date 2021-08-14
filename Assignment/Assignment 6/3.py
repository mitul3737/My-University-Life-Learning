
def foo_moo(val_1):
    if val_1%2==0 and val_1%3==0:
        print('"FooMoo"')
    elif val_1%2==0:
        print('"Foo"')
    elif val_1%3==0:
         print('"Moo"')
    else:
         print('"Boo"')

    return " "
print(foo_moo(int(input(""))))