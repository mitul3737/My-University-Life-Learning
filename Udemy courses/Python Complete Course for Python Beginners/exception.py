try:
    a=int(input("Please enter the first number: "))
    b=int(input("Please enter the second number: "))
    if (a<0): # for negative numbers
        raise TypeError
    c=a/b
    print("{} / {} = {}".format(a,b,c))
except ZeroDivisionError:
    print("Division by zero is not positive")
except ValueError: # if not given digits or number
    print("The data types are not proper")
except TypeError: # for negative numbers case
    print("The data is not in  range")
except NameError: # if used new variable
    print("The data  items are not defined")

