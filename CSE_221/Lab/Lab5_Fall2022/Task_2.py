# Task-2

import math
import heapq

file = open('input2.txt', 'r')

num = file.readline()
lines = file.readlines()

dict1 = {}
dict2 = {}
dict3 = {}

numm = -1
# count = [0]
# while count<int(num):
lis = [dict1, dict2, dict3]
lis2 = []

for i in range(len(lines)):

    var_x = lines[i].strip('\n')
    ver = var_x.split()
    #print(ver)
    if len(ver) == 2: #only if we have ver length 2
        numm += 1
        lis2.append(int(ver[0])) #lists which has 2 values
        #print(lis2)
        for i in range(1, int(ver[0]) + 1):
            #print(lis[numm][i])
            lis[numm][i] = []
            #print(lis[numm][i])
            """[][]......."""

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


#print(lis)
"""[{1: []}, {1: [[2, 10]], 2: [[1, 10]]}, {1: [[2, 1], [4, 2]], 2: [[1, 1], [3, 4], [5, 5]], 3: [[5, 1], [2, 4], [4, 2]], 4: [[1, 2], [3, 2]], 5: [[3, 1], [2, 5]]}]"""


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
    

    return dist[reach] 

#print(dict1)
""""{1: []}"""
#print(dict2)
"""{1: [[2, 10]], 2: [[1, 10]]}"""
#print(dict3)
"""{1: [[2, 1], [4, 2]], 2: [[1, 1], [3, 4], [5, 5]], 3: [[5, 1], [2, 4], [4, 2]], 4: [[1, 2], [3, 2]], 5: [[3, 1], [2, 5]]}"""


get1 = dijkstra(dict1, 1, lis2[0])
get2 = dijkstra(dict2, 1, lis2[1])
get3 = dijkstra(dict3, 1, lis2[2])

file_w = open('output2.txt','w')

file_w.write(f"{str(get1)}\n")

file_w.write(f'{str(get2)}\n')
file_w.write(f'{str(get3)} ')

file.close()
file_w.close()
