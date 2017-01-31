# From the implementation of Union-find Data Structure
from collections import defaultdict

class Graph:
	def __init__(self):
		self.graph = defaultdict(list)

	def add_edge(self, vertex, edge):
		self.graph[vertex].append(edge)

	def find_parent(self, parent, i):
		if parent[i] == -1:
			return i
		elif parent[i] != -1:
			self.find_parent(parent, parent[i])

	def union(self, parent, x, y):
		x_set = self.find_parent(parent, x)
		y_set = self.find_parent(parent, y)
		parent[x_set] = y_set

	def is_cyclic(self):
		V = [-1]*len(self.graph)

		for i in self.graph:
			for j in self.graph[i]:
				x = self.find_parent(parent, x)
				y = self.find_parent(parent, y)

				if x == y:
					return True
				self.union(parent, x, y)

def main():	
	g = Graph()
	g.add_edge(0, 1)
	g.add_edge(0, 2)
	g.add_edge(1, 2)
	g.add_edge(2, 0)
	g.add_edge(2, 3)
	g.add_edge(3, 3)

	if g.is_cyclic:
		print "Graph is Cyclic"
	else:
		print "Not Cyclic"

if __name__ == '__main__':
	main()