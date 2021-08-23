tup=input("").strip(")(").split('), (')

n_tup_1=()
tup_1=[]
for i in tup:
    #print(i)
    i=i.split(", ")
    #print(i)
    x_tup=()
    for j in i:
        j=int(j)
        y_tup=(j,)
        x_tup+=y_tup
        #print(x_tup)
    tup_1.append(x_tup)
#print((tuple(tup_1)))
tup=tup_1

#tup=((33, 22, 11), (30, 45, 56, 45,20), (81, 90, 39, 45), (1, 2, 3, 4,5,6))

avg_list=[]
for i in tup:
    sum = 0
    cnt=0
    for j in i:
            sum += j
            cnt += 1
    avg = sum / cnt
    avg_list.append(avg)


print(f"Average: {avg_list}")
comp=avg_list[0]
j=0
for i in avg_list:
    j+=1
    if i>=comp:
        comp=i
        spec=j


print(f"Tuple with maximum sum : {tup[spec-1]}")







