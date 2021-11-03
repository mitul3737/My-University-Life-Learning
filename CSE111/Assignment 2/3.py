mit_0=input("").strip(")(").split(",")
num3=int(mit_0[0])
num4=int(mit_0[1])
num5=int(mit_0[2])



def function_name(min_0, max_0, div_0):
    sum_0=0
    for i in range(min_0,max_0):
        if i %div_0==0:

            sum_0+=i
    return sum_0
print(function_name(num3,num4,num5))
