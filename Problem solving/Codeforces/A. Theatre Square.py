x=input().split(" ")
x1=[]
for i in x:
    x1.append(int(i))
ans=(x1[0]+x1[2]-1)//x1[2]* ((x1[1]+x1[2]-1)//x1[2])
print(ans)

