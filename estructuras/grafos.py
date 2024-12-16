class Vertex:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

    def add_neighbor(self, neighbor, weight = 1):
        self.neighbors.append((neighbor, weight))

class Graph:
    def __init__(self, directed=False):
        self.vertexList= {}
        self.directed = directed

    #Agregar un nodo al grafo 
    def add_vertex(self, vertex):
        if vertex not in self.vertexList:
            self.vertexList[vertex] = Vertex(vertex)
    
    #Agregar una arista al grafo
    def add_edge(self, u, v, weight = 1):
        if u not in self.vertexList:
            self.add_vertex(u)
        if v not in self.vertexList:
            self.add_vertex(v)

        self.vertexList[u].add_neighbor(self.vertexList[v], weight)
        if not self.directed:
            self.vertexList[v].add_neighbor(self.vertexList[u], weight)
        
    #Mostrar el grafo
    def display(self):
        for vertex in self.vertexList:
            neighbors = [(neighbor.value, weight) for neighbor, weight in self.vertexList[vertex].neighbors]
            print(f'{vertex} -> {neighbors}')


def main():
    #grafo no dirigido
    grafo1 = Graph()
    grafo1.add_vertex('A')
    grafo1.add_vertex('B')
    grafo1.add_vertex('C')
    grafo1.add_vertex('D')
    grafo1.add_edge('A', 'B', 5)
    grafo1.add_edge('A', 'C', 3)
    grafo1.add_edge('A', 'D', 2)
    grafo1.add_edge('B', 'C', 1)
    grafo1.add_edge('B', 'D', 4)
    grafo1.add_edge('C', 'D', 6)
    grafo1.display()
    print()
    # grafo dirigido
    grafo2 = Graph(directed=True)
    grafo2.add_vertex('A')
    grafo2.add_vertex('B')
    grafo2.add_vertex('C')
    grafo2.add_vertex('D')
    grafo2.add_edge('A', 'B', 5)
    grafo2.add_edge('A', 'C', 3)
    grafo2.add_edge('A', 'D', 2)
    grafo2.add_edge('B', 'C', 1)
    grafo2.add_edge('B', 'D', 4)
    grafo2.add_edge('C', 'D', 6)
    grafo2.display()

main()