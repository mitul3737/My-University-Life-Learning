from multipledispatch import dispatch
class my_calculator():

    @dispatch(int,int)#when we have 2 input, it will work
    def product(self,a,b):
        print(a*b)

    @dispatch(int,int,int)#working for 3 integers
    def product(self,a,b,c):
        print(a*b)
    @dispatch(float,float,float)#working for 3 floats
    def product(self,a,b,c):
        print(a*b*c)
    @dispatch(float,int)#working for a int and a float
    def product(self,c,d):
        print(c*d)
c1=my_calculator()
c1.product(4,5)
c1.product(4,7,6)
c1.product(4.0,5.0,3.0)
c1.product(4.0,3)