class Graph:
	def __init__(self):
		self.vertices_dict = dict()
		self.num_vertices = 0

	def __iter__(self):
		return iter(self.vertices_dict.values())

	def add_vertex(self, node):
		self.num_vertices += 1
		new_vertex = Vertex(node)
		self.vertices_dict[node] = new_vertex
		return new_vertex

	def add_edge(self, frm, to, weight = 0):
		if frm not in self.vertices_dict:
			self.add_vertex(frm)
		if to not in self.vertices_dict:
			self.add_vertex(to)

		self.vertices_dict[frm].add_neighbor(self.vertices_dict[to], weight)

	def get_vertex(self, n):
		if n in self.vertices_dict:
			return self.vertices_dict[n]
		else:
			return None

	def get_vertices(self):
		return self.vertices_dict.keys()


class Vertex():
	def __init__(self, node):
		self.id = node
		self.adjacent_vertices = dict()

	def add_neighbor(self, neighbor, weight):
		self.adjacent_vertices[neighbor] = weight

	def get_weight(self, neighbor):
		return self.adjacent_vertices[neighbor]

	def get_id(self):
		return self.id

	def get_connection(self):
		return self.adjacent_vertices.keys()


def main():
	g = Graph()
	li =['a', 'b', 'c'] 
	for x in li:
		g.add_vertex(x)

	g.add_edge('a', 'c', 4)
	g.add_edge('a', 'b', 6)
	g.add_edge('b', 'd' ,1)
	g.add_edge('d', 'c', 3)


	for v in g:
		for w in v.get_connection():
			print v.get_id() + ' is connected to ' + w.get_id() +" with weight " + str(v.get_weight(w))


if __name__ == '__main__':
	main()

