#1

file = open('input1.txt', 'r')
f1 = open("output1.txt", "w")
a1=file.readline()
lines = file.readlines()
#print(lines)
list_0=[]


#adding values from file
for i in range(len(lines)):
    varr = lines[i].strip('\n')
    ver = varr.split()
    list_0.append(ver)


#sort based on finished time
def Sort(sub_li):
    l = len(sub_li)
    for i in range(0, l):
        for j in range(0, l-i-1):
            if (int(sub_li[j][1]) > int(sub_li[j + 1][1])):
                tempo = sub_li[j]
                sub_li[j]= sub_li[j + 1]
                sub_li[j + 1]= tempo
    return sub_li


def task(list_x):
    val = 0
    time = 0
    task = 0
    list_oo = [] #saving working times
    for i in list_x: #looping through list of all working times
        # print(i)
        if int(i[0]) >= val:
            val = 0
            add = int(i[0]) + (int(i[1]) - int(i[0]))

            val += add
            # print(val)
            # print(i)
            list_oo.append(i)
            task += 1
    return task, list_oo

#initiative
val, list_d = task(Sort(list_0))

#print results
print(val)
for i in list_d:
    print(i[0], "", i[1])


f1.write(str(val)+ "\n")
for i in list_d:
    f1.write(i[0] + " " + i[1] + "\n")

file.close()
f1.close()


#2
file = open('input2.txt', 'r')
f1= open("output2.txt", "w")
a1 = file.readline().split(" ")
var = a1[0]
var_1 = a1[1].split("\n")
men = var_1[0]
#print(var)
#print(men)
lines = file.readlines()
#print(lines)
list_0 = []

for i in range(len(lines)):
    varr = lines[i].strip('\n')
    ver = varr.split()
    list_0.append(ver)

#Now sort the list
def Sort(sub_li):
    l = len(sub_li)
    for i in range(0, l):
        for j in range(0, l-i-1):
            if (int(sub_li[j][1]) > int(sub_li[j + 1][1])):
                tempo = sub_li[j]
                sub_li[j]= sub_li[j + 1]
                sub_li[j + 1]= tempo
    return sub_li

list_sort=Sort(list_0)#sorting the list



list_x = []
#list of list for different mens
for i in range(0, int(men)):
    list_x.append([])

#print(list_x)

task=0 #assuming tasks to be 0
for x in range(0,int(var)):
    for y in range(0,(len(list_x))):
       if list_sort[x] not in list_x[y]: #not there
           #2cases
            if list_x[y] == []: #empty
                list_x[y].append(list_sort[x])
                task += 1
                break
            else: #not empty
                if list_sort[x][0] >= list_x[y][len(list_x[y])-1][1]:
                    list_x[y].append(list_sort[x])
                    task+=1
                    break

print(task)
f1.write(str(task)+ "\n")

file.close()
f1.close()



#3
file = open('input3.txt', 'r')
f1 = open("output3.txt", "w")
var=file.readline()
lines = file.readline().split(" ")


list_0=[]
for i in range(len(lines)):
    list_0.append(int(lines[i]))
#print(list_0)

call=file.readline()
#print(call)

list_stack=[]

def sort(list_0):
    for i in range(len(list_0)):
        for j in range(len(list_0)-1):
            if list_0[j]>list_0[j+1]:
                tempo=list_0[j]
                list_0[j]=list_0[j+1]
                list_0[j+1]=tempo
    return list_0

works=""
jack_work=0
jill_work=0


sorted_work=sort(list_0)#sort the work
for x in call:
    if x=="J":
        work=sorted_work.pop(0) #J picks the smallest value and thus we pop it too to print it
        list_stack.append(work)
        jack_work+=work
        works+=str(work)+" "
    elif x=="j":
        work_x=sort(list_stack).pop()#j checks the max value and thus we pop it
        works+=str(work_x)+" "
        jill_work+=work_x

print(works)
print(f"Jack will work for {jack_work} hours")
print(f"Jill will work for {jill_work} hours")
f1.write(works)
f1.write(f"Jack will work for {jack_work} hours")
f1.write(f"Jill will work for {jill_work} hours")
file.close()
f1.close()


#4
file=open("input4.txt","r")
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
