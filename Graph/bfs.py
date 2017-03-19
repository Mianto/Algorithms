from collections import defaultdict, deque


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, vertex, edge):
        self.graph[vertex].append(edge)

    def BFS(self, vertex):
        visited = [False] * (len(self.graph) + 3)

        queue = list()
        queue.append(vertex)

        visited[vertex] = True

        while queue:
            s = queue.pop(0)
            print s,

            for x in self.graph[s]:
                if not visited[x]:
                    queue.append(x)
                    visited[x] = True

    # Another implementation of bfs without using visited
    # but returning a list of vertices
    def bfs_as_connected(self, vertex):
        queue = deque()
        queue.append(vertex)
        explored = []

        while queue:
            node = queue.popleft()
            if node not in explored:
                explored.append(node)
                neighbours = self.graph[node]

                for neighbour in neighbours:
                    queue.append(neighbour)
        return explored


g = Graph()
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(3, 4)
g.addEdge(1, 5)
g.addEdge(5, 6)

g.BFS(1)
print g.bfs_as_connected(1)
