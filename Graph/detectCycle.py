from collections import defaultdict

class Graph:
	def __init__(self):
		self.graph=defaultdict(list)

	def add_edge(self, vertex, edge):
		self.graph[vertex].append(edge)

	def DFSUtil(self, vertex, visited):
		visited[vertex] = True
		li = list()
		li.append(vertex)

		for i in self.graph[vertex]:
			if visited[i] == False:
				visited[i] = True
				li.append(i)
		return li

	def cycle_detector(self):
		V = len(self.graph)
		visited = [False]*V
		vertex_list = list()

		for i in range(V):
			if visited[i] == False:
				vertex_list.append(self.DFSUtil(i, visited))
		# print vertex_list
		for x in vertex_list:
			if len(x)>1:
				return True
		else: return False


def main():
	g = Graph()
	g.add_edge(0, 1)
	g.add_edge(0, 2)
	g.add_edge(1, 2)
	g.add_edge(2, 0)
	g.add_edge(2, 3)
	g.add_edge(3, 3)

	print g.cycle_detector()

if __name__ == '__main__':
	main()
 		