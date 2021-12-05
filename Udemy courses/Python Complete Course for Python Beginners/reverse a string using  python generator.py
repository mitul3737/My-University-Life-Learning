#reverse a string
def reverse_string(my_string):
    length=len(my_string)
    for i in range(length-1,-1,-1):
        yield my_string[i]


for char in reverse_string("WORLD"):
    print(char)