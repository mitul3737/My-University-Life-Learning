#   Created by Elshad Karimov
#   Copyright © 2021 AppMillers. All rights reserved.

from collections import defaultdict


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def addNode(self, value):
        self.nodes.add(value)

    def addEdge(self, fromNode, toNode, distance):
        self.edges[fromNode].append(toNode)
        self.distances[(fromNode, toNode)] = distance


def dijkstra(graph, initial):
    visited = {initial: 0}
    path = defaultdict(list)

    nodes = set(graph.nodes)

    while nodes:
        minNode = None
        for node in nodes:
            if node in visited:
                if minNode is None:
                    minNode = node
                elif visited[node] < visited[minNode]:
                    minNode = node
        if minNode is None:
            break

        nodes.remove(minNode)
        currentWeight = visited[minNode]

        for edge in graph.edges[minNode]:
            weight = currentWeight + graph.distances[(minNode, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge].append(minNode)

    return visited, path


customGraph = Graph()
customGraph.addNode("A ")
customGraph.addNode("B")
customGraph.addNode("C")
customGraph.addNode("D")
customGraph.addNode("E")
customGraph.addNode("F")
customGraph.addNode("G")
customGraph.addNode("H")
customGraph.addNode("I")
customGraph.addNode("J")
customGraph.addNode("K")
customGraph.addNode("L")
customGraph.addNode("Motijheel")
customGraph.addNode("MOGHBAZAR")

customGraph.addEdge("Motijheel", "A", 3)
customGraph.addEdge("A", "B", 4)
customGraph.addEdge("A", "H", 6)
customGraph.addEdge("B", "G", 2)
customGraph.addEdge("H", "I", 5)
customGraph.addEdge("B", "C", 7)
customGraph.addEdge("C", "F", 7)
customGraph.addEdge("C", "D", 3)
customGraph.addEdge("D", "E", 1)
customGraph.addEdge("F", "G", 2)
customGraph.addEdge("F", "MOGHBAZAR", 4)
customGraph.addEdge("G", "H", 3)
customGraph.addEdge("G", "J", 1)
customGraph.addEdge("I", "J", 7)
customGraph.addEdge("J", "K", 6)
customGraph.addEdge("L", "L", 4)
customGraph.addEdge("L", "MOGHBAZAR", 7)
customGraph.addEdge("L", "MOGHBAZAR", 2)

print(dijkstra(customGraph, "MOGHBAZAR"))

# See change the distance from d to e to 1 and from b to e to 6.
# then to get to e from a ,
# shortest path should be a b d e
# but your code is giving a b e