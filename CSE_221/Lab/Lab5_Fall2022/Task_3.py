# Task -3
import math
import heapq

file = open('input2.txt', 'r')

num = file.readline()
lines = file.readlines()

dict1 = {}
dict2 = {}
dict3 = {}

numm = -1
lis = [dict1, dict2, dict3]
lis2 = []

for i in range(len(lines)):

    varr = lines[i].strip('\n')
    ver = varr.split()
    if len(ver) == 2:
        numm += 1
        lis2.append(int(ver[0]))
        for i in range(1, int(ver[0]) + 1):
            lis[numm][i] = []
    # fix it
    else:
        if int(ver[0]) in lis[numm] and int(ver[1]) not in lis[numm]:
            lis[numm][int(ver[0])].append([int(ver[1]), int(ver[2])])
            lis[numm][int(ver[1])] = [[int(ver[0]), int(ver[2])]]

        elif int(ver[0]) in lis[numm] and int(ver[1]) in lis[numm]:
            lis[numm][int(ver[0])].append([int(ver[1]), int(ver[2])])
            lis[numm][int(ver[1])].append([int(ver[0]), int(ver[2])])

        else:
            lis[numm][int(ver[0])] = [[int(ver[1]), int(ver[2])]]
            lis[numm][int(ver[1])] = [[int(ver[0]), int(ver[2])]]


# dist= {}
def dijkstra(dic, source, reach):
    # declaring everything
    dist = {}
    dist[source] = 0
    pq = []
    heapq.heapify(pq)
    # visited_set = []
    parent = {}

    for i in dic:
        if i != source:
            dist[i] = math.inf
        parent[i] = None

    # print(dist)
    # print(parent)
    heapq.heappush(pq, (0, source))
    while len(pq) != 0:
        u = heapq.heappop(pq)
        for v in dic[u[1]]:
            # print(pq)
            get = v

            if dist[get[0]] > get[1] + dist[u[1]]:  # v = [B , 4]  dic = [[B,4],[H,6]]
                temp = dist[get[0]]
                dist[get[0]] = get[1] + dist[u[1]]
                parent[get[0]] = u[1]

                # Inserting the value if the vertex haasn't been visited yet
                if temp == math.inf:
                    # print(dist)
                    # print(temp)
                    heapq.heappush(pq, (get[1], get[0]))

    way = []
    while reach != None:#untill we find the source, we keep on adding the parent of the vertex to the list
        #print(way)
        way.append(reach)
        reach = parent[reach]

    return way #hee senddng the way

#print(lis2)
"""[1, 2, 5]"""
get1 = dijkstra(dict1, 1, lis2[0])
get2 = dijkstra(dict2, 1, lis2[1])
get3 = dijkstra(dict3, 1, lis2[2])

get1.reverse()
get2.reverse()
get3.reverse()

lis3 = [get1,get2,get3]
file_w = open('output3.txt','w')

for i in lis3:
    for j in range(len(i)):
        file_w.write(str(i[j]))
        file_w.write(' ')
    file_w.write('\n')

file.close()
file_w.close()
