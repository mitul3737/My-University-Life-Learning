A=[] #creating a list
def F(n):
 if (n==0 or n==1):
    return 1
 else:
    return F(n-1)+F(n-2)
def FM(n):
 if(A[n] > 0):
    return A[n]
 if(n == 0 or n==1):
    return 1
 else:
    return A[n].append(FM(n-1)+FM(n-2))


def CalcFib():
 A.insert(0,1)
 A.insert(1,1)
 for i in range(2,100): #Set the fibonacci limit to 100 index. You can change it too to your own benefit
    A.insert(i,A[i-1]+A[i-2])


CalcFib()
#The fibonacci series is: 0,1,1,2,3,5,8,13,21,........... which follows f(n)=f(n-1)+f(n-2)
var=input("Which fibonacci number  do you want to know? Kindly enter the index number: ")
"""For example
Which fibonacci number  do you want to know? Kindly enter the index number: 0
1"""
print(F(int(var)))
