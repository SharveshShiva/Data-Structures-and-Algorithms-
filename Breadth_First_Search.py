class Graph:
    def __init__(self):
        self.graph = {}                             

    def addVertex(self, vertex):
        if vertex not in self.graph:                 
            self.graph[vertex] = []                  
    def addEdge(self, src, dest):
        self.addVertex(src)                          
        self.addVertex(dest)
        
        self.graph[src].append(dest)                
        self.graph[dest].append(src)

    def printGraph(self):
        for vertex in self.graph:
            print(f"{vertex}: {self.graph[vertex]}")

    def bfs(self, start_vertex):
        visited = set()                               
        queue = []                                  

        queue.append(start_vertex)                    
        visited.add(start_vertex)                     

        while queue:
            vertex = queue.pop(0)                     
            print(vertex, end=" ")                    

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:           
                    queue.append(neighbor)            
                    visited.add(neighbor)             
if __name__ == "__main__":
    G1= Graph()
    G1.addEdge('A', 'D')
    G1.addEdge('D', 'C')
    G1.addEdge('B', 'C')
    G1.addEdge('C', 'A')

    G1.printGraph()

    print("\nTraversal starting from vertex A:")
    G1.bfs('B')
    print("\nTraversal starting from vertex B:")
    G1.bfs('A')
    print("\nTraversal starting from vertex C:")
    G1.bfs('C')
    print("\nTraversal starting from vertex D:")
    G1.bfs('D')
