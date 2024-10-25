class Graph:
    def __init__(self):
        self.graph = {}
        self.directed = False

    def add_vertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self,src,dest):
        self.add_vertex(src)
        self.add_vertex(dest)


        self.graph[src].append(dest)

        if not self.directed:
            self.graph[dest].append(src)

    def display(self):
        for vertex in self.graph:
            print(vertex,":",self.graph[vertex])


G = Graph()
G.add_edge('A','C')
G.add_edge('A','D')
G.add_edge('A','C')
G.add_edge('B','C')
G.add_edge('C','D')

G.display()


