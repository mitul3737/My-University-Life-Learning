file=open("task4.txt","r")
f1=open("output4.txt","w")
var=file.readline().split(" ")
while var!=['0', '0']: #checks if we have 0 0
    a,b=int(var[0]),int(var[1]) #appoints 2 values to 1 and b
    count_0=0
    for i in range(a,b+1): #checking all values from a to b
        if pow(i,.5)%1==0:#checks if i is a perfect square
            count_0+=1
    print(count_0)
    f1.write(str(count_0)+"\n")
    var = file.readline().split(" ") #checks values


