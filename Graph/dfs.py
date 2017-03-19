from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, vertex, edge):
        self.graph[vertex].append(edge)

    def DFSutil(self, vertex, visted):
        visted[vertex] = True
        li = list()
        li.append(vertex)

        for i in self.graph[vertex]:
            if not visted[i]:
                visted[i] = True
                li.append(i)
        return li

    def dfs(self, vertex):
        visted = [False] * (len(self.graph) + 1)
        return self.DFSutil(vertex, visted)

    def dfs_graph(self):
        V = len(self.graph)
        visted = [False] * V
        li = list()
        for i in range(V):
            if not visted[i]:
                li.append(self.DFSutil(i, visted))
        return li

    def dfs_as_path(self, source, destination):
        V = len(self.graph) + 1
        visited = [False] * V
        visited[source] = True
        li = list()
        current = source
        for i in self.graph[current]:

            print self.graph[2]
            if current == destination:
                return li
                break
            elif not visited[i]:
                li.append(i)
                visited[i] = True
                current = i


def main():
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(0, 3)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    print g.dfs(0)
    print g.dfs_graph()
    print g.dfs_as_path(1, 3)


if __name__ == '__main__':
    main()
