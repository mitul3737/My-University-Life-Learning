# CSE221 Lab 03 Graphs
def readFile():
    # reading file from as input
    # change the file name according to yours
    f = open("graph.txt", "r")

    # first line of input contains the number of vertices in the graph
    n = f.readline()
    # strip() gets rid of the new line
    # try printing n without strip()
    print(n.strip())
    n = n.strip()
    print(type(n))
    # n is of type string. we need to convert it to int
    n = int(n)
    print(type(n))

    # the second line of the file contains the number of connections
    c = f.readline()
    c = c.strip()
    c = int(c)
    print(c)

    buildGraphUsingDictionary(5, f)

    buildGraphUsingListofLists(5, f)


# we want to build an adjacency list like the following
# A -> B,C
# One vertex can be connected to multiple vertices
# which means multiple values are associated with one vertex
# one data structure that can be used is a dictionary of lists
# {A:[B,C]}
def buildGraphUsingDictionary(c, f):
    graph = {}
    counter = 0
    while (counter <= c):
        line = f.readline()  # reading each line
        a, b = line.split(",")  # splitting the vertices
        b = b.strip()  # getting rid of \n from the end
        a = int(a)
        b = int(b)
   

        if (a in graph):
            graph[a].append(b)
        else:
            graph[a] = [b]
        #  print(a)
        #  print(b)
        counter += 1
        print(graph)

    printGraph(graph, None)


# TO DO
# This method must be completed by you
# You should code in such a way that the output should be
# 1 -> 2,4
# 2 -> 4
# 3 -> 1,4
# 4 -> 2
# notice this method takes both the graphs as parameters
# this means you have print the same output in the same style for both the datastructures
# if graph is none then print from listGraph
# if listGraph is none then print from graph


def printGraph(graph, listGraph):
    if (graph != None):
        print(graph)
    elif listGraph!=None:
        for i in listGraph:
            for k in i:
                print(k, end=" ")
            print("\n")



# TO DO
# I have shown you how to build a graph using a dictionary of list
# now your job is to build a graph using list of lists [[E,B],[C,D]]
# it means A -> E,B and B -> C,D
def buildGraphUsingListofLists(c, f):
    listGraph = []  # do not change the name of the variable
    # your code
    for i in range(0, c + 1):
        listGraph.append([0] * (c+1))
    f = open("graph.txt", "r")
    n = f.readline()
    m=f.readline()
    m=int(m)



    for i in range(0, m):
        x = f.readline()
        list_100 = x.split(",")
        a = int(list_100[0])
        b = int(list_100[1].strip("\n"))
        listGraph[a][b] = 1
        listGraph[b][a] = 1

    """for x in range(0,m):
      x=''
      x=f.readline()
      list_100=x.split(",")
      a=int(list_100[0])
      b=int(list_100[1])
      demo=List_0[a]
      if b not in demo:
        demo.append(b)

    print(List_0)"""

    printGraph(None, listGraph)

readFile()
# ======================Program starts here.========================
# read file using the readFile() method readFile()




