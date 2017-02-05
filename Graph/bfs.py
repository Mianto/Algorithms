from collections import defaultdict

class Graph:
	def __init__(self):
		self.graph = defaultdict(list)

	def addEdge(self, vertex, edge):
		self.graph[vertex].append(edge)

	def BFS(self, vertex):
		visited = [False]*(len(self.graph)+ 3)

		queue = list()
		queue.append(vertex)

		visited[vertex] = True
		
		while queue:
			s = queue.pop(0)
			print s,

			for x in self.graph[s]:
				if visited[x]==False:
					queue.append(x)
					visited[x] = True
					

g = Graph()
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(3, 4)
g.addEdge(1, 5)
g.addEdge(5, 6)

g.BFS(1)