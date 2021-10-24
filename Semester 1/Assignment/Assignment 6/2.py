val_0 = int(input(""))
val_1 = val_0
def fibonacci(val_0):
    fir = 0  # first element of series
    sec = 1
    print(fir,sec,end=" ")
    for x in range(2,val_0+1):
            sum=fir+sec
            if sum <=val_1:
               print(sum,end=" ")
               fir=sec
               sec=sum
    return  " "
print(fibonacci(val_0))