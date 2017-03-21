from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, vertex, edge):
        self.graph[vertex].append(edge)

    def bfs_shortest_path(self, start, end):
        explored = []
        queue = [[start]]

        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node not in explored:
                neighbours = self.graph[node]

                for neighbour in neighbours:
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)
                    if neighbour == end:
                        return new_path

                explored.append(node)
        return 'No path found between ' + str(start) + ' and ' + str(end)


def main():
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(0, 3)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    print g.bfs_shortest_path(0, 3)


if __name__ == "__main__":
    main()


