from collections import defaultdict


class Graph:
	def __init__(self):
		self.graph=defaultdict(list)

	def add_edge(self, vertex, edge):
		self.graph[vertex].append(edge)
		self.graph[edge].append(vertex)

	def is_cycleUtil(self, vertex, visited, parent):
		visited[vertex] = True

		for i in self.graph[vertex]:
			if visited[i] == False:
				self.is_cycleUtil(i, visited, vertex)
				return True
			elif parent != i:
				return True
		return False

	def is_cyclic(self):
		visited = [False]*len(self.graph)

		for i in range(len(self.graph)):
			if visited[i] == False:
				if self.is_cycleUtil(i, visited, -1):
					return True
		return False

def main():
	g = Graph()
	g.add_edge(0, 1)
	g.add_edge(0, 2)
	g.add_edge(1, 2)
	g.add_edge(2, 0)
	g.add_edge(2, 3)
	g.add_edge(3, 3)

	if g.is_cyclic():
		print "Cycle is present"
	else:
		print "Cycle is not present"

if __name__ == '__main__':
	main()