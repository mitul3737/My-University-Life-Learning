#1_a
f = open("input1_a.txt", "r")
f1 = open("output1_a.txt", "w")
n = f.readline().split(" ")


def Adjacency_Matrix(n):
    listGraph = []
    for i in range(0, int(n[0]) + 1):
        listGraph.append([0] * (int(n[0]) + 1))

    for i in range(0, int(n[1].strip("\n"))):
        x = f.readline()
        list_100 = x.split(" ")
        a = int(list_100[0])
        b = int(list_100[1])
        c = int(list_100[2].strip("\n"))
        listGraph[a][b] = c
        # listGraph[b][a] = 1 #for undirected graph
        # print(listGraph)
    return listGraph


def printGraph(listGraph):
    for i in listGraph:
        for k in i:
            # print(k, end=" ")
            f1.write(str(k) + " ")
        f1.write("\n")


printGraph(Adjacency_Matrix(n))
f.close()
f1.close()


#1_b
f = open("input1_b.txt", "r")
f1=open("output1_b.txt","w")
n = f.readline().split(" ")
def Adjacency_list(n):
    listGraph = []
    for i in range(0, int(n[0])+1):
      listGraph.append([0] * (int(n[0])+1))

    for i in range(0, int(n[1].strip("\n"))):

        x = f.readline()
        list_100 = x.split(" ")
        a = int(list_100[0])
        b=int(list_100[1])
        c = int(list_100[2].strip("\n"))
        if listGraph[a][b]!=0:
            listGraph[a][b].append(c)
            #print(listGraph)
        else:
            listGraph[a][b]=[]
            listGraph[a][b].append(c)
            # listGraph[b][a] = 1 #for undirected graph
            #print(listGraph)

    return listGraph

def printGraph(listGraph):
    for i in range(0,(len(listGraph))):
        list_1 = []
        for k in range(0,len(listGraph[i])):
            if listGraph[i][k] != 0:
                    #depending on the value of weights (multiple or one weight, we create tupples)
                    for j in range(0,len(listGraph[i][k])):
                        list_1.append((k,listGraph[i][k][j]))

        if len(list_1) == 0:
            #print(i,":")
            f1.write(str(i)+":"+"\n")

        if len(list_1) != 0:
            f1.write(str(i)+":")
            #print(i,":",end=" ")
            for j in range(0,len(list_1)):
                if j == len(list_1)-1:
                    #print(list_1[j]) #just print the last value
                    f1.write(str(list_1[j])+"\n")
                else:
                    f1.write(str(list_1[j])+",")
                    #print(list_1[j],end=" ") #add values side by side



printGraph(Adjacency_list(n))
f.close()
f1.close()

#2
input_file = open('input2.txt', 'r')
f2=open('output2.txt', 'w')
n, e = map(int, input_file.readline().split())  # taking values and splitting up
adj = [[] for i in range(n + 1)]
# print(adj)

for i in range(e):
    # u,v,w=map(int,input_file.readline().split())
    # adj[u].append((v,w)) #in the node u, saving connection v and saving their weights.
    u, v = map(int, input_file.readline().split())
    adj[u].append((v, 0))  # setting weight as 0
# print(adj)
from queue import Queue


def BFS(source):
    visit = [0] * (n + 1)
    # print(source)
    q = Queue()
    q.put(source)  # queue push
    # after vising the source, colour the source
    visit[source] = 1
    while not q.empty():
        u = q.get()  # pop
        #print(u, end=" ")
        f2.write(str(u)+" ")
        for v in range(len(adj[u])):
            child = adj[u][v][0]
            # weight=adj[u][v][1]
            # check if the child is already visited or not.
            if visit[child] == 0:
                q.put(child)
                visit[child] = 1


BFS(1)#value to start BFS

input_file.close()
f2.close()




##3
f1=open('input3.txt', 'r')
f2=open('output3.txt', 'w')
N, M=[int(x) for x in f1.readline().split()]
G=[None]*(N+1)


for i in range(len(G)):
  G[i]=[]


for i in range(M):
  u, v=[int(x) for x in f1.readline().split()]
  # creating undirected graph
  if v not in G[u]:
    G[u].append(v)
  if u not in G[v]:
    G[v].append(u)

color=[None]*(N+1) #created color array to store the color of each node
visited=[] #Stores if it is visited or not.

def colourInit(G):
  for i in range(len(G)):
    color[i] = 0

def DFS(G,s):
  color[s] = 1
  visited.append(s)
  for v in G[s]:
    if color[v] == 0:
      DFS(G,v)

colourInit(G)
DFS(G, 1) # s=source vertex

str_out=''
for i in visited:
  str_out+=f'{i} '

f2.write(str_out[:-1])
f1.close()
f2.close()



# 4
f1=open('input4.txt', 'r')
f2=open('output4.txt', 'w') #output file
N, M=[int(x) for x in f1.readline().split()]
G=[None]*(N+1) #creating an array

# creating list of list
for i in range(len(G)):
  G[i]=[]


for i in range(M):# appending the connections
  u, v=[int(x) for x in f1.readline().split()]
  G[u].append(v)

#creating an stack to store the nodes
stack=[]
cycle=False #setting the variable cycle to false

#using DFS to find cycle
def DFS(G,s): # s=index=node
  global cycle
  if s not in stack:
    stack.append(s)
    for v in G[s]:
      if v not in stack:
        DFS(G,v)
        stack.pop()
      else: # if a node is already in stack, it means cycle is present
        cycle=True
        break
    return cycle

flag=DFS(G, 1) # s=source vertex starting from this
if flag:
  f2.write('YES')
else:
  f2.write('NO')

f1.close()
f2.close()


# 5

f1=open('input5.txt', 'r')
f2=open('output5.txt', 'w')
N, M, D=[int(x) for x in f1.readline().split()]
G=[None]*(N+1)


for i in range(len(G)):# creating list of list
  G[i]=[]


for i in range(M):# appending the connections
  u, v=[int(x) for x in f1.readline().split()]
  if v not in G[u]:# creating undirected graph
    G[u].append(v)
  if u not in G[v]:
    G[v].append(u)

parent=[None]*(N+1)
time=[0]*(N+1) # shortest time from the source vertex

def BFS(G, s): # s=index=node
  color=[0]*(N+1)
  q=[] # queue
  color[s]=1
  q.append(s)
  while len(q)!=0:
    u=q.pop(0)
    for v in G[u]: # for all adjacent values of a specific vertex
      if color[v]==0:
        color[v]=1
        q.append(v)
        parent[v]=u
        time[v]=time[u]+1

BFS(G, 1) #using BFS to find the shortest path from the source vertex


path=[D] # shortest path from the source vertex to D in reverse order

ancestor_0=None
index=D
while ancestor_0!=1:
  if parent[D]!=None:
    ancestor_0=parent[index]
    path.append(ancestor_0)
    index=ancestor_0
  else:
    break
path=path[::-1] # list reversed to find the actual path
path_str=''
for i in path:
  path_str+=f'{i} '

str_out=''
str_out+=f'Time: {time[D]}\nShortest Path: {path_str}'

f2.write(str_out[:-1])
f1.close()
f2.close()


# 6

f1=open('input6.txt', 'r')
f2=open('output6.txt', 'w')
R, H=[int(x) for x in f1.readline().split()]

# adjacency matrix created bordered by '#'
# or else, while traversing 'i-1', 'i+1', 'j-1' and 'j+1' gives error of index out of range
ll=[]
row=['#']*(H+2) # first and last row
ll.append(row)
all=f1.read().split('\n')
for line in range(len(all)):
  line_lst=['#']
  for letter in all[line]:
    line_lst.append(letter)
  line_lst.append('#')
  ll.append(line_lst)
ll.append(row)

# '#' -> -1
# '.' & 'D' -> 0 (unvisited)
# '.' & 'D' -> 1 (visited)
flag=[]
for i in range(R+2):
  line_lst=[]
  for j in range(H+2):
    if ll[i][j]=='#':
      line_lst.append(-1)
    else:
      line_lst.append(0)
  flag.append(line_lst)

def DFS(i, j):
  if ll[i][j]=='D':
    if [i, j] not in loc: # to prevent addition of one diamond more than once
      loc.append([i, j])
  # recursive flood fill with 4 directions
  trav=[[i-1, j], [i+1, j], [i, j+1], [i, j-1]]
  # traversing to -> top, bottom, right, left
  for k in trav:
    if flag[k[0]][k[-1]]==0:
      flag[i][j]=1
      DFS(k[0], k[1])

maxi=0
for i in range(R+2):
  for j in range(H+2):
    if ll[i][j]=='.' and flag[i][j]==0: # only executes on unvisited '.' and excludes all '#' and visited points
      loc=[] # saves the location of all diamonds within a specific region/boundary
      DFS(i, j)
      if len(loc)>maxi:
        maxi=len(loc)

f2.write(str(maxi))
f1.close()
f2.close()