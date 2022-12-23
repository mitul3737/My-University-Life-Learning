import math
import heapq

file = open('input1.txt', 'r')

lines = file.readlines()

dict = {}

for i in range(len(lines)):
    var_x = lines[i].strip('\n')
    ver = var_x.split()


    # if ver[0] in dic:
    #     dic[ver[0]].append([ver[1],int(ver[2])])
    # else:
    #     dic[ver[0]] = [[ver[1],int(ver[2])]]
    # fix it
    if ver[0] in dict and ver[1] not in dict:
        dict[ver[0]].append([ver[1], int(ver[2])])
        dict[ver[1]] = [[ver[0], int(ver[2])]]


    elif ver[0] in dict and ver[1] in dict:
        dict[ver[0]].append([ver[1], int(ver[2])])
        dict[ver[1]].append([ver[0], int(ver[2])])

    else:
        dict[ver[0]] = [[ver[1], int(ver[2])]]
        dict[ver[1]] = [[ver[0], int(ver[2])]]


dist = {}


def dijkstra(dic, source):
    # declaring everything
    dist[source] = 0
    pq = []
    heapq.heapify(pq)
    visited_set = []
    parent = {}

    for i in dic:
        if i != source:
            dist[i] = math.inf
        parent[i] = None
    #print(dist)
    #print(parent)
    """{'Motijheel': 0, 'A': inf, 'B': inf, 'H': inf, 'G': inf, 'I': inf, 'C': inf, 'F': inf, 'D': inf, 'E': inf,
     'MOGHBAZAR': inf, 'J': inf, 'K': inf, 'L': inf}
    {'Motijheel': None, 'A': None, 'B': None, 'H': None, 'G': None, 'I': None, 'C': None, 'F': None, 'D': None,
     'E': None, 'MOGHBAZAR': None, 'J': None, 'K': None, 'L': None}"""


    #dic={'Motijheel': [['A', 3]], 'A': [['Motijheel', 3], ['B', 4], ['H', 6]], 'B': [['A', 4], ['G', 2], ['C', 7]], 'H': [['A', 6], ['I', 5], ['G', 3]], 'G': [['B', 2], ['F', 2], ['H', 3], ['J', 1]], 'I': [['H', 5], ['J', 7]], 'C': [['B', 7], ['F', 7], ['D', 3]], 'F': [['C', 7], ['G', 2], ['MOGHBAZAR', 4]], 'D': [['C', 3], ['E', 1]], 'E': [['D', 1]], 'MOGHBAZAR': [['F', 4], ['K', 7], ['L', 2]], 'J': [['G', 1], ['I', 7], ['K', 6]], 'K': [['J', 6], ['L', 4], ['MOGHBAZAR', 7]], 'L': [['K', 4], ['MOGHBAZAR', 2]]}
    #pq=0
    heapq.heappush(pq, (0, source))
    #pushing the source node in the priority queue
    while len(pq) != 0: #unless it is empty
        u = heapq.heappop(pq)

        for v in dic[u[1]]:
            # print(pq)

            get = v
            #print(get)
            if dist[get[0]] > get[1] + dist[u[1]]:  # v = [B , 4]  dic = [[B,4],[H,6]]
                #print(get[0])
                #print(get[1])
                #print(dist[u[1]])


                temp = dist[get[0]]#saving the unvisited nodes 1st value in temp


                dist[get[0]] = get[1] + dist[u[1]] #update the value
                parent[get[0]] = u[1] #update parents

                # Inserting the value if the vertex haasn't been visited yet cZ if it has inf , it means we did not visit it yet.
                if temp == math.inf:
                    # print(dist)
                    # print(temp)
                    heapq.heappush(pq, (get[1], get[0])) #pushing to priority queue

    #print('parent:', parent)
    #print('distance', dist)
    """parent: {'Motijheel': None, 'A': 'Motijheel', 'B': 'A', 'H': 'A', 'G': 'B', 'I': 'H', 'C': 'B', 'F': 'G', 'D': 'C',
             'E': 'D', 'MOGHBAZAR': 'F', 'J': 'G', 'K': 'J', 'L': 'MOGHBAZAR'}
    distance
    {'Motijheel': 0, 'A': 3, 'B': 7, 'H': 9, 'G': 9, 'I': 14, 'C': 14, 'F': 11, 'D': 17, 'E': 18, 'MOGHBAZAR': 15,
     'J': 10, 'K': 16, 'L': 17}"""
    way = [] #The way we need
    reach = 'MOGHBAZAR' #target #change if needed <<<<<----------------
    while reach != None: #as the parents of the source was None, w wil start from destination and add till we  find our parents (source)

        way.append(reach) #adding our target to the way
        reach = parent[reach] #finding the parent of the target
    return parent,dist,way #returning parents ,distances and the way


paren , distance , path= dijkstra(dict, 'Motijheel') #oour source was Motijheel
"""print('parent:', paren)
print('distance', distance)
print('path', path)"""

#Inputing the data to check outputs
val1 = distance['MOGHBAZAR']
val2 = paren['MOGHBAZAR']
path.reverse() ##print way in reverse order



file_w = open('output1.txt','w')
file_w.write(f"Parent: {str(val2)}")
file_w.write('\n')
file_w.write(f'Dstance: {str(val1)}')
file_w.write('\n')
for i in path:
    file_w.write(str(i))
    file_w.write(' ')


file.close()
file_w.close()
