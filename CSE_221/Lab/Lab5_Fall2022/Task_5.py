# task-5

import math
import heapq

file = open('input5.txt', 'r')

# num = file.readline()
lines = file.readlines()

dic1 = {}
dic2 = {}
dic3 = {}
dic4 = {}

numm = -1
# count = [0]
# while count<int(num):
lis = [dic1, dic2, dic3, dic4]
lis2 = []
lis3 = []

for i in range(len(lines)):

    varr = lines[i].strip('\n')
    ver = varr.split()
    if i == 0:
        continue
    elif len(ver) == 1:
        continue

    elif len(ver) == 2:
        numm += 1
        lis2.append(int(ver[0]))
        for i in range(1, int(ver[0]) + 1):
            lis[numm][i] = []
    # fix it
    else:
        if int(ver[0]) in lis[numm]:
            lis[numm][int(ver[0])].append([int(ver[1]), int(ver[2])])
        else:
            lis[numm][int(ver[0])] = [[int(ver[1]), int(ver[2])]]


# dist= {}
def dijkstra(dic, source, reach):
    # declaring everything
    dist = {}
    dist[source] = 0
    pq = []
    heapq.heapify(pq)
    # visited_set = []
    parent = {}
    alt = 0
    for i in dic:
        if i != source:
            dist[i] = -math.inf
        parent[i] = None

    # print(dist)
    # print(parent)
    heapq.heappush(pq, (0, source))
    while len(pq) != 0:
        u = heapq.heappop(pq)
        for v in dic[u[1]]:
            # print(pq)
            get = v

            temp = dist[get[0]]
            if dist[u[1]] > get[1]:
                alt = get[1]
            else:
                alt = dist[u[1]] + get[1]
            # if dist[get[0]] < get[1] + dist[u[1]]:  # v = [B , 4]  dic = [[B,4],[H,6]]
                # temp = dist[get[0]]
            if alt > dist[get[0]]:
                # dist[get[0]] = get[1] + dist[u[1]]
                dist[get[0]] = alt
                parent[get[0]] = u[1]

                # Inserting the value if the vertex haasn't been visited yet
                if temp == -math.inf:
                    # print(dist)
                    # print(temp)
                    heapq.heappush(pq, (-1*(get[1]), get[0]))

    # print('parent:', parent)
    # print('distance', dist)
    # print()
    # way = []
    # while reach != None:
    #     print(reach)
    #     way.append(reach)
    #     reach = parent[reach]

    
    return parent, dist

#print(lis2)
"""[1, 2, 2, 4]"""
p1,d1 = dijkstra(dic1, 1, lis2[0])
p2,d2 = dijkstra(dic2, 1, lis2[1])
p3,d3 = dijkstra(dic3, 2, lis2[2])
p4 ,d4 = dijkstra(dic4, 1, lis2[3])

paren = [p1,p2,p3,p4]
distance =[d1,d2,d3,d4]
file_w = open('output5.txt','w')
for i in distance:
    for j in i:
        val = i[j]
        if val == -math.inf:
            file_w.write(str(-1))
            file_w.write(' ')
        # print(val,end=' ')
        else:
            file_w.write(str(val))
            file_w.write(' ')
    file_w.write('\n')


file.close()
file_w.close()

"""with open('output5.txt','r') as file1:
    var = file1.read()
    print(var)"""
