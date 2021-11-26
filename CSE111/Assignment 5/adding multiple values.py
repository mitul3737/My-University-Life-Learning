class A(object):
    def __init__(self,value):
        self.value = value

    def __add__(self,other):#calling the class again and using new value
        return A(self.value + other.value)

    def __str__(self):#as called print() so,
        return "{}".format(self.value)

a1= A(10)
a2=A(20)
a3=A(30)
print(a1 + a2 + a3)
